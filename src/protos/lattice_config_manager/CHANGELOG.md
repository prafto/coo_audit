## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.1
- Add initial lattice-config-manager folder and files

### 0.0.3
- Onboard to schema-build-service

### 0.0.4
- Add initial service RPCs

### 0.1.0
- Add GraphConfig and PromptTemplate APIs

### 0.5.0
- Change PromptTemplate tag to tags

### 0.5.2
- Rename fields

### 0.6.0
- Update graph contracts

### 0.6.1
- Add metadata to Document

### 0.7.0
- Change field name from bind_constants to bindings

### 0.8.0
- Modify GraphConfig contract
- Rename Tag to ReturnDirectTag

### 0.9.0
- Modify PromptTemplate contract

### 0.9.1
- Add active_prompt_template model

### 0.9.5
- Add disable_expanded_view flag on GetGraph API

### 0.9.9
- Update Lattice UG endpoints and add list active_prompt_template api

### 0.9.11
- Add list prompt_template apis

### 0.9.12
- Add new condition type greater_than_or_equal

### 0.10.0
- Rename condition type

### 0.13.0
- Add APIs to update Nodes and Edges

### 0.14.0
- Add High Level APIs
- Remove unused proto

### 0.15.0
- Update agent_graph_version to Int64Value

### 0.16.0
- Remove delete agent graph attributes api
- Add new field is_hard_update in update agent graph request

### 0.16.1
- Add new message type
- Add message metadata to MessageWithReturnType
