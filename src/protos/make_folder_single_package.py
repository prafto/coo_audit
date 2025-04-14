#!/bin/env python3

import json
import os
import pprint
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import PurePath
from typing import Any, Optional

pprinter = pprint.PrettyPrinter(indent=2)


@dataclass
class Release:
    tag: str = ""
    name: str = ""
    body: str = ""
    languages: list[str] = field(default_factory=list)
    team_slack: Optional[str] = None
    team_email: Optional[str] = None
    dependencies: Optional[list[str]] = None
    go_files: Optional[list[str]] = None
    skip_unchanged: Optional[str] = None
    register_schemas: Optional[list[str]] = None
    folder: str = ""

    def to_dict(self) -> dict[str, Any]:
        d = {
            "tag": self.tag,
            "name": self.name,
            "body": self.body,
            "languages": self.languages,
        }
        if self.team_slack is not None:
            d["team_slack"] = self.team_slack
        if self.team_email is not None:
            d["team_email"] = self.team_email
        if self.dependencies is not None:
            d["dependencies"] = self.dependencies
        if self.go_files is not None:
            d["go_files"] = self.go_files
        if self.skip_unchanged is not None:
            d["skip_unchanged"] = self.skip_unchanged
        if self.register_schemas is not None:
            d["register_schemas"] = self.register_schemas
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Release":
        return Release(
            d["tag"],
            d.get("name", ""),
            d.get("body", ""),
            d["languages"],
            d.get("team_slack", None),
            d.get("team_email", None),
            d.get("dependencies", None),
            d.get("go_files", None),
            d.get("skip_unchanged", None),
            d.get("register_schemas", None),
            "",
        )

    def bump_version(self):
        parts = [int(x) for x in self.tag.split(".")]
        parts[2] += 1
        self.tag = ".".join([str(x) for x in parts])

    def conditionally_bump_ver(self, prev_ver: str):
        if self.tag == prev_ver:
            self.bump_version()

    def write(self, f: str):
        with open(f, "w", encoding="utf-8") as fle:
            json.dump(self.to_dict(), fle, indent=2)

    @classmethod
    def read(cls, f: str) -> "Release":
        with open(f, "r", encoding="utf-8") as fle:
            js_dict = json.load(fle)
            return Release.from_dict(js_dict)


global_renames: list[tuple[str, str]] = list()


def get_package(f: str) -> str:
    with open(f, "r", encoding="utf-8") as fle:
        for line in fle.readlines():
            if line.startswith("package"):
                return line.split(" ")[1].strip().removesuffix(";")
    return ""


def fix_file(fle: str, dst: str):
    global_renames.append((fle, dst))
    subprocess.call(["git", "mv", fle, dst])


def move_files(packages: dict[str, list[str]], folder: str):
    for deplist in packages.items():
        package = deplist[0]
        files = deplist[1]
        try:
            os.mkdir(os.path.join(folder, package))
        except FileExistsError:
            pass
        for fle in files:
            dst = os.path.join(folder, package, os.path.basename(fle))
            fix_file(fle, dst)


def walk(release: Release, folder: str, starting_ver: str):
    for root, dirs, files in os.walk(folder):
        packages: dict[str, list[str]] = defaultdict(list)
        for fle in files:
            if fle.endswith(".proto"):
                package = get_package(os.path.join(root, fle))
                packages[package].append(os.path.join(root, fle))
        for d in dirs:
            walk(release, os.path.join(root, d), starting_ver)
        if len(packages.keys()) > 1:
            release.conditionally_bump_ver(starting_ver)
            move_files(packages, root)


def update_release_for_protofile(release: Release, fle: str):
    path = PurePath(fle)
    d = path.parent
    while (
        d.name != "services-protobuf"
    ):  # we shouldn't be looking any higher than the root of the repo
        try:
            rjson = d / "release.json"
            new_d = d.parent
            if new_d == d:
                break
            d = new_d
            r = Release.read(rjson.as_posix())
            if r.dependencies is not None:
                for idx, dep in enumerate(r.dependencies):
                    if release.folder in dep:
                        expected = f"{release.folder}=={release.tag}"
                        if dep != expected:
                            r.dependencies[idx] = expected
                            r.bump_version()
                            r.write(rjson.as_posix())
            return
        except FileNotFoundError:
            continue


def rename_imports(release: Release, renames: list[tuple[str, str]]):
    for root, _, files in os.walk("."):
        for fle in files:
            if fle.endswith(".proto"):
                fpath = os.path.join(root, fle)
                with open(fpath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                with open(fpath, "w", encoding="utf-8") as f:
                    for line in lines:
                        for rename in renames:
                            if rename[0] in line:
                                line = line.replace(f'"{rename[0]}"', f'"{rename[1]}"')
                                update_release_for_protofile(
                                    release, os.path.abspath(fpath)
                                )
                        f.write(line)


def fix_buf_yaml(renames: list[tuple[str, str]]):
    fpath = "buf.yaml"
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(fpath, "w", encoding="utf-8") as f:
        for line in lines:
            for rename in renames:
                if rename[0] in line:
                    line = line.replace(f"- {rename[0]}", f"- {rename[1]}")
            f.write(line)


def cleanup_folder(folder: str):
    release_file = f"{folder}/release.json"
    release = Release.read(release_file)
    cur_ver = release.tag
    if "go" not in release.languages:
        release.languages.append("go")
        release.conditionally_bump_ver(cur_ver)
    if release.go_files is not None and len(release.go_files) != 0:
        release.go_files = None
    release.folder = folder
    walk(release, folder, cur_ver)
    rename_imports(release, global_renames)
    release.write(release_file)
    fix_buf_yaml(global_renames)


def main():
    folder = sys.argv[1]
    cleanup_folder(folder)


if __name__ == "__main__":
    main()
