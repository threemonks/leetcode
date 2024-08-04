### ACID vs BASE
* ACID (Consistency over Availability)
* BASE (Availability over Consistency)

### Load Balancer
1. load balancing (round robin, smart/dynamic, sticky session, layer 4 vs 7)
2. enable horizontal scaling
3. eliminate SPOF
4. SSL termination
5. session persistence
6. disadvantages of horizontal scaling
  * complexity, server should be stateless, now sticky sessions
  * more requirement on downstream server/service (DB)
7. disadvantage of load balancer:
  * could be performance bottleneck
  * increased complexity
  * SPOF or complexity with multiple load balancer

### Reverse Proxy Benefits
* increased security
* increased scalability and flexibility
* SSL termination
* compression
* caching
* static content

### Application Layer vs Web Layer
* allow web and application layer to scale independently
* MVC (model-view-controller), MVT (model-view-template)

### Service Discovery
* etcd, zookeeper

### Communications
* UDP vs TCP
* HTTP is based on TCP
* RPC - Google Protobuf, Facebook Thrift (HBase/Cassandra), Apache Avro - internal
* RESTful (Representational state transfer of resources) - public

### Storage
* RDBMS - ACID (atomicity, consistency, isolation, and durability)
* RDBMS to eliminate SPOF clustering vs sharding
* NoSQL - BASE (Basically Availabe, Soft state, Eventual Consistency)
  - for high vol read/write request
  - Key-value store / cache - for high performance, low latency, simple data models or rapidly-changing data,  - redis / memcache
    1. Pattern - read-through / write-through / write-around / write-back / cache-aside
    2. Placement: client side / separate cache layer / server side
    3. Replacement: expire/repalce - LRU / LFU /ARC
    4. DynamoDB
    5. keys in lexicographic order
  - Document Store - for flexibility and performance
    1. MongoDB, CouchDB, DynamoDB
  - Columnar Store - for distributed, high availability and high scalability, optimized for write large data sets
    1. Bigtable, Cassandra, HBase
    2. keys in lexicographic order
  - Graph DB - data models with complex relationship
    1. Neo4j
    2. via REST API

### CAP Theorem
- Consistency
- Availability
- Partition Tolerance
- CP - consistency and partition tolerance
- AP - availability and partition tolerance

#### Consistency Pattern
- Weak consistency
- Eventual Consistency
- Strong Consistency


#### Aailability patterns
- Failover mode
- - Active-passive
  - Active-active
- Replication
- - master-slave, master-master
- failover mode
* cold standby
* hot standby
* warm standby
* active-active

### B tree vs B+ tree
* B tree: internal nodes hold value
  - frequent keys closer to root access faster
* B+ tree: internal nodes does NOT hold value, leaf nodes have link to next left node
  - more key in memory, fewer cache miss
  - leaf node linked, faster to traverse, fewer cache miss

### Cloud Design Patterns
#### Availability patterns
* Health Endpoing Monitoring
* Queue-Based Load leveling
* Throttling
#### Data Management Patterns
* Cache-aside
* command and query responsibility Segregation
* Event sourcing: append-only store to record full series of event
* Index table
* materialized view
* sharding
* static content hosting / CDN

### Public API Choices
* JSON RPC
* GraphQL
* REST
* gRPC

### SQL vs NoSQL
- SQL: structured data, strict schema, join, transaction, relational data
- NoSQL: high read/write throughput, dynamic schema/structure, high data volume, high throughput
