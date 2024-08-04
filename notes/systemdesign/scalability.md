## [Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)

### Trade-offs
- Performance vs Scalability
  1. slow for single user -> performance problem
  2. fast for single user but slow under heavy load -> scalability problem
- Latency vs Throughput
  1. maximize throughput with acceptable latency
- Availability vs Consistency
  1. CAP theorem - Consistency, Availability, Partition tolerance
  2. Centralized System - ACID - Atomic, Consistent, Isolated, Durable (centralized system)
  3. Distributed System - Partition always exists, only get choose between Avaiability and Consistency
  4. NOSQL - BASE: Basically Available, Soft state, Eventually Consistent
- Availability Patterns
  1. Fail-over (Active-passive, Active-active)
  2. Replication
    * Master-Slave
    * Tree replication
    * Master-Master
    * Buddy Replication
  3. Replication
    * Active replication - push
    * Passive replication - Pull
- Scalability Patterns: State
  * Partitioning
  * HTTP Caching (Reverse Proxy, CDN,
  * RDBMS Sharding
  * NOSQL (Key-Value, Column, Document, Graph, Datastructure)
  * Distributed Caching
  * Data Grids
  * Concurrency
- BASE - Distributed databases:
  * Cassandra (Facebook)
  * Riak
  * Voldemort (Linkedin)
  * Dynomite
  * SimpleDB
  * Bigtable (Google)
  * Dynamo | SimpleDB (Amazon)
  * HBase (Yahoo)
- Types of NOSQL Stores:
  * Key-Value (Voldemort, Dynomite)
  * Column (Cassandra, Vertica, Sybase IQ)
  * Document (MongoDB, CouchDB)
  * Graph (Neo4J, AllegroGraph)
  * Datastructure (Redis, Hazelcast)

