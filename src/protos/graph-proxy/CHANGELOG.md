Changelog for the Graph proxy. Add the latest release description at the top.
-------------------------
1.37.1
Changes:
Fix typo on target type
-------------------------
1.37.0
Changes:
Use Allowed Types in filter proto
-------------------------
1.36.0
Changes:
Bump pkg_common version to 0.0.2
-------------------------
1.35.0
Changes:
Add include_deleted in READ API
-------------------------
1.34.0
Changes:
Add soft delete support
-------------------------
1.33.0
Changes:
Change GraphProxyCdcEvent to take index instead of full entities
Release old deprecated field names back to namespace
-------------------------
1.32.0
Changes:
Change GraphProxyCdcEvent to take index instead of full entities
Release old deprecated field names back to namespace
-------------------------
1.31.0
Changes:
Add Tenant ID in response
-------------------------
1.30.0
Changes:
Register GraphProxyCdcEvent schema to Iguazu.
-------------------------
1.29.0
Changes:
Add back Kotlin support
-------------------------
1.28.0
Changes:
Add secondary index retrieval in getEntities()
Add edge property filtering
-------------------------
1.27.0
Changes:
Register GraphProxyCdcEvent schema to Iguazu.
-------------------------
1.26.0
Changes:
Enable cascade delete for edges connected to node for which delete is requested.
-------------------------
1.25.0
Changes:
Deprecated unused fields
-------------------------
1.24.0
Changes:
Add Application level CDC initial proto message, get ready for Iguazu.
Get ready to deprecated Error, and non-Node/EdgeIndex usage.
-------------------------
1.23.0
Changes:
Add DistributedContext to UpdateGraph
-------------------------
1.22.0
Changes:
Add GetEntities endpoint.
-------------------------
1.21.0
Changes:
Add mvcc timestamp to successful response in Upsert, Update and Delete rpc.
-------------------------
1.20.0
Changes:
Improve filter proto design
-------------------------
1.19.0
Changes:
Add level by level traversal and directional traversal flags.
-------------------------
1.18.0
Changes:
Add Level By Level in GetSubGraph API
-------------------------
1.17.0
Changes:
Remove streaming from UpsertSubGraph, DeleteSubGraph and UpdateSubGraph rpcs.
-------------------------
1.16.0
Changes:
Add UpdateSubGraph API.
-------------------------
1.15.0
Changes:
Add explicit using_transaction flag for UpsertSubGraph and DeleteSubGraph rpc
-------------------------
1.14.0
Changes:
**Revert** - Added tenantID to UpsertSubGraphRequest and DeleteSubGraphRequest
-------------------------
1.13.0
Changes:
Added tenantID to UpsertSubGraphRequest and DeleteSubGraphRequest.
-------------------------
1.12.1
1.12.0
Changes:
Add allowed_node_types/blocked_node_types in GetSubGraph rpc. Make allow and block filters of oneof type in the GetSubGraph rpc.
-------------------------
1.11.0
Changes:
This is to remove streaming input requests for GetSubGraph rpc.
-------------------------
1.9.0
Changes:
This is to add an anchor time to the API so that we can get the changes as_of_timestamp
-------------------------
1.5.0
Changes:
Use NodeIndex in EdgeIndex.  EdgeIndex needs the source and target types.
-------------------------
1.4.0
Changes:
Add WriteNode/WriteEdge message types for Write requests
-------------------------
1.3.0
Changes:
Add UniqueId type,
Add source/target UniqueIds for EdgeIndex,
Add UniqueId to Node/Edge messages,
Add source/target NodeIndexes for Edge,
Simplify/split out Result messages,
Simplify GetSubGraphRequest
-------------------------
1.2.0
Changes:
Update to fit latest repo
-------------------------
1.1.0
Changes:
Added the source and target types of the node for inserting an edge between them
------------------------
1.0.0
Changes:
Adding the first iteration of the graph proxy interface