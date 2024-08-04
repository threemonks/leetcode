# System Design Template

business requirements
Target users (phone, web etc)
Agree on p0 (mvp) requirements

functional requirements
Consistency or Availability?
Real-time or batch?
Read heavy or write heavy?

back of envelope calculations (focus on QPS and latency)
Latency estimation
QPS
Memory
Storage

High level diagram
API
Rest vs GraphQL or SOAP
Talk about throttling, auth

Database schema
How to partition
How to build index
Avoid hotspot
Avoid consistently updating one record

Deep dive
Scale each component
Consistency vs Availability
Components to be considered; how they could help
DNS
CDN
Load Balancer

Database (SQL vs NoSQL)
Use SQL unless a clear advantage for NoSQL
Main/Follower
Async        vs sync replication
Write once, read everywhere; write everywhere, read once
Shard key
Index

Cache
Cacheability. I.e. data repetition.
Memory requirement
Staleness effect