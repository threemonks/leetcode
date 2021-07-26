"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.

"""
import collections
from datetime import datetime

"""
Design
brutal force Least Recently Used
"""


class LRUCache0:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = dict()
        self.lru_ts = dict()

    def get(self, key: int) -> int:
        ret = self.data.get(key, -1)
        if key in self.data:
            self.lru_ts[key] = datetime.now()

        return ret

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.lru_ts[key] = datetime.now()
        if len(self.data) > self.capacity:
            lru_key = None
            for key in self.data:
                if key not in self.lru_ts:
                    lru_key = key
                    break
                if not lru_key or lru_key not in self.lru_ts or self.lru_ts[lru_key] > self.lru_ts[key]:
                    lru_key = key
            self.data.pop(lru_key, None)
            self.lru_ts[lru_key] = 0

        # Your LRUCache object will be instantiated and called as such:

"""
Design

use dict to store {key: val}
use OrderedDict to store last_access_ts and key, in OrderedDict, item is ordered by insert time, so there's a O(1) time method move_to_end(key) that would update last_access_ts for a given key to last (latest).

OrderedDict uses DoublyLinkedList underlying

"""
from collections import OrderedDict

class LRUCache0:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nums = OrderedDict() # store key: val, but order by last add time/access time

    def get(self, key: int) -> int:
        if key in self.nums:
            self.nums.move_to_end(key)
            return self.nums[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.nums[key] = value
        self.nums.move_to_end(key) # in case it is already in middle
        if len(self.nums) > self.capacity:
            self.nums.popitem(last=False)

"""
Design

implement DoublyLinkedList, the head is the least recently used, that will be evicted first
newly added item will be added at end
use dummy head/tail to make add/remove operation easier

mistakes1:
1. we use len(self.cache) > self.capacity to check if exceeding limit, so we always need to add key into self.cache first before adding the double linked list, so that check for exceeding capacity inside _add_node can properly detect exceeding capacity.
2. _add_node calls _remove_node if exceeding capacity
3. _add_node handles adding to self.cache
4. _remove_node handles removing from self.cache
"""
class DLinkedNode:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

    def __repr__(self):
        return '{%s: %s}' % (self.key, self.val)

class LRUCache:

    def _move_to_end(self, node):
        # move key to end of dlink
        # node.prev <-> node <-> node.next
        # => node.prev <-> node.nxt
        self._remove_node(node)
        # and dummy_tail.prev <-> node <-> dummy_tail
        self._add_node(node)

    def _add_node(self, node):
        # add node at end, right before dummy tail
        # and dummy_tail.prev <-> node <-> dummy_tail
        node.prev, node.nxt = self.tail.prev, self.tail
        self.tail.prev.nxt = node
        self.tail.prev = node
        self.cache[node.key] = node

        # make sure not exceeding capacity
        if len(self.cache) > self.capacity:
            # remove first value from dlink
            self._remove_node(self.head.nxt)

    def _remove_node(self, node):
        # remove specific node
        # node.prev <-> node <-> node.next
        # => node.prev <-> node.nxt
        node.prev.nxt, node.nxt.prev = node.nxt, node.prev
        # remove from self.cache
        del self.cache[node.key]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # dictionary hold {key: node} with value

        # dummy head/tail
        self.head = DLinkedNode(0, 0)
        self.tail = DLinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # print('get key=%s cache=%s' % (key, self.cache))
        if key not in self.cache:
            return -1
        else:
            # move to end
            self._move_to_end(self.cache[key])
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # print('put key=%s value=%s cache=%s' % (key, value, self.cache))
        if key in self.cache:
            # update value and move node to end
            self.cache[key].val = value
            self._move_to_end(self.cache[key])
        else:
            # add a new one
            node = DLinkedNode(key, value)
            self._add_node(node)


def main():
    obj = LRUCache(2)
    obj.put(1,1)
    obj.put(2,2)
    assert obj.get(1) == 1, 'fails'
    obj.put(3,3)
    assert obj.get(2) == -1, 'fails'
    obj.put(4,4)
    assert obj.get(1) == -1, 'fails'
    assert obj.get(3) == 3, 'fails'
    assert obj.get(4) == 4, 'fails'

if __name__ == '__main__':
   main()