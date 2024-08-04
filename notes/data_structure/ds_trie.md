## HashMap vs Trie vs Linked Structure

https://stackoverflow.com/questions/245878/how-do-i-choose-between-a-hash-table-and-a-trie-prefix-tree

* Trie:
- Pros
    1. Predictable O(k) lookup time where k is the size of the key
    2. Lookup can take less than k time if it's not there
    3. Supports ordered traversal
    4. No need for a hash function
    5. Deletion is straightforward
    6. You can quickly look up prefixes of keys, enumerate all entries with a given prefix, etc.

* Linked Structure
- Pros
    1. If there are many common prefixes, the space they require is shared.
    2. Immutable tries can share structure. Instead of updating a trie in place, you can build a new one that's different only along one branch, elsewhere pointing into the old trie. This can be useful for concurrency, multiple simultaneous versions of a table, etc.
    3. An immutable trie is compressible. That is, it can share structure on the suffixes as well, by hash-consing.

* Hash Table Pros & Cons
- Pros
    1. Everyone knows hashtables, right? Your system will already have a nice well-optimized implementation, faster than tries for most purposes.
    2. Your keys need not have any special structure.
    3. More space-efficient than the obvious linked trie structure
- Cons
  1. Hash calculation cost
  2. collision resulting in slowness / load factor / re
