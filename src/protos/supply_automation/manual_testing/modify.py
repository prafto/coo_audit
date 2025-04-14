import re
from typing import Optional

FILE1 = "protos/supply_automation/scenario_service_v1.proto"
FILE2 = "protos/supply_automation/run_mobilizer_service_v1.proto"

def modify(file_in: str, file_out: Optional[str] = None) -> None:
    with open(file_in, "r") as f:
        lines = f.readlines()

    savedline: Optional[str] = None
    newlines = []
    for i, line in enumerate(lines):
        if re.search(r'option \(.* = {$', line):
            savedline = line
            continue
        if savedline:
            if re.match(r'\s*};$', line):
                newlines.append(re.sub(r'{$', '{};',  savedline))
                savedline = None
            continue
        line = re.sub(r' \[\(doordash.+\];', ';', line)
        if re.match(r'\s*option \(.*\) = ', line):
            line = re.sub(r'{.*}', '{}', line)
        newlines.append(line)

    with open(file_out or file_in, "w") as f:
        f.writelines(newlines)

def test():
    modify(
        file_in = "protos/supply_automation/manual_testing/TEST_IN",
        file_out = "protos/supply_automation/manual_testing/TEST_OUT",
    )

if __name__ == "__main__":
    modify(FILE1)
    modify(FILE2)
