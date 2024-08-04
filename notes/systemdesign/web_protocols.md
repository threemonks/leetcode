## REST vs RPC

https://www.smashingmagazine.com/2016/09/understanding-rest-and-rpc-for-http-apis/

RPC-based APIs are great for actions (that is, procedures or commands)

REST-based APIs are great for modeling your domain (that is, resources or entities), making CRUD (create, read, update, delete) available for all of your data.

REST is not only CRUD, but things are done through mainly CRUD-based operations. REST will use HTTP methods such as GET, POST, PUT, DELETE, OPTIONS and, hopefully, PATCH to provide semantic meaning for the intention of the action being taken.

RPC, however, would not do that. Most use only GET and POST, with GET being used to fetch information and POST being used for everything else. It is common to see RPC APIs using something like POST /deleteFoo, with a body of { “id”: 1 }, instead of the REST approach, which would be DELETE /foos/1.

## REST vs RPC


When done correctly, REST improves long-term evolvability and scalability at the cost of performance and added complexity. REST is ideal for services that must be developed and maintained independently, like the Web itself. Client and server can be loosely coupled and change without breaking each other.

RPC services can be simpler and perform better, at the cost of flexibility and independence. RPC services are ideal for circumstances where client and server are tightly coupled and follow the same development cycle.

However, most so-called REST services don't really follow REST at all, because REST became just a buzzword for any kind of HTTP API. In fact, most so-called REST APIs are so tightly coupled, they offer no advantage over an RPC design.

## API Architectural Styles: SOAP vs REST vs GraphQL vs RPC

|                       | RPC                                                                                                         | SOAP                                                                                                         | REST                                          | GraphQL                                      |
|:----------------------|:------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|:----------------------------------------------|:---------------------------------------------|
| Organized in terms of | local procedure calling                                                                                     | enveloped message structure                                                                                  | compliance with six architectural constraints | schema & type system                         |
| Format                | JSON, XML, Protobuf, Thrift, FlatBuffers                                                                    | XML only                                                                                                     | XML, JSON, HTML, plain text                   | JSON                                         |
| Learning curve        | Easy                                                                                                        | Difficult                                                                                                    | Easy                                          | Medium                                       |
| Community             | Large                                                                                                       | Small                                                                                                        | Large                                         | Growing                                      |
| Use cases             | command and action-oriented APIs; internal high performance communication in massive micro-services systems | Payment gateways, identity management CRM solutions, financial and telecommunication services, legacy system | Public APIs, simple resource-driven apps      | Mobile APIs, complex systems, micro-services |
