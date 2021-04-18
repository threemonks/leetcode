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

class LRUCache0:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nums = collections.OrderedDict()  # store key: val, but order by last add time/access time

    def get(self, key: int) -> int:
        if key in self.nums:
            self.nums.move_to_end(key)
            return self.nums[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.nums[key] = value
        self.nums.move_to_end(key)  # in case it is already in middle
        if len(self.nums) > self.capacity:
            self.nums.popitem(last=False)


"""
Design

implement DoublyLinkedList, the head is the least recently used, that will be evicted first
newly added item will be added at end
use dummy head/tail to make add/remove operation easier

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
        node = self._remove_node(node)
        # and dummy_tail.prev <-> node <-> dummy_tail
        self._add_node(node)

    def _add_node(self, node):
        # add node at end, right before dummy tail
        # and dummy_tail.prev <-> node <-> dummy_tail
        dummy_tail_prev = self.dummy_tail.prev
        dummy_tail_prev.nxt, node.prev = node, dummy_tail_prev
        node.nxt, self.dummy_tail.prev = self.dummy_tail, node

        # make sure not exceeding capacity
        if len(self.nums) > self.capacity:
            # remove first value from dlink
            del_node = self.dummy_head.nxt
            self.dummy_head.nxt = del_node.nxt
            # remove from self.nums
            del self.nums[del_node.key]

    def _remove_node(self, node):
        # remove specific node
        # node.prev <-> node <-> node.next
        # => node.prev <-> node.nxt
        node_prev, node_nxt = node.prev, node.nxt
        node_prev.nxt = node_nxt
        node_nxt.prev = node_prev
        return node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nums = {}  # dictionary hold {key: node} with value

        # dummy head/tail
        self.dummy_head = DLinkedNode(0, 0)
        self.dummy_tail = DLinkedNode(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        # print('get key=%s nums=%s' % (key, self.nums))
        if key not in self.nums:
            return -1
        else:
            # move to end
            self._move_to_end(self.nums[key])
            return self.nums[key].val

    def put(self, key: int, value: int) -> None:
        # print('put key=%s value=%s nums=%s' % (key, value, self.nums))
        if key in self.nums:
            # move to end and update value
            self.nums[key].val = value
            self._move_to_end(self.nums[key])
        else:
            # add a new one
            node = DLinkedNode(key, value)
            self.nums[key] = node
            self._add_node(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

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