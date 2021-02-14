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


# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict

"""
using OrderedDict
"""


class LRUCache1(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)

        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
using Dict and DoubleLinkedList
"""


class DLinkedNode(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(OrderedDict):

    def _add_node(self, node):
        """
        always add node right after the dummy head
        """
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.cache[node.key] = node
        self.size += 1
        if self.size > self.capacity:
            self._remove_node(self.tail.prev)

    def _remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del self.cache[node.key]
        self.size -= 1

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0

        # dummy head and tail
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self._move_to_head(self.cache[key])

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value  # update value
            self._move_to_head(self.cache[key])
        else:
            node = DLinkedNode(key=key, value=value)
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