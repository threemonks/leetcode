"""
460. LFU Cache
Hard

1959

151

Add to List

Share
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.



Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3


Constraints:

0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.


Follow up: Could you do both operations in O(1) time complexity?

"""
"""
Design

use nums: {key: freq}
use freqs: {freq: OrderedDict {key: value}}

key points:
1. OrderedDict orders item by insert order
2. OrderedDict.move_to_end(key) moves an key to end (re-insert)
3. OrderedDict.popitem(last=False) removes oldest value (head)

"""
from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0  # total number of caches
        self.capacity = capacity
        self.nums = {} # key to freq
        self.freqs = defaultdict(OrderedDict)
        self.minfreq = 0  # the minimum freq, to help identify which dll to evict an cached item

    def _update(self, key, value=None):
        """
        update node when add(key) or put(key) and the key exists already
        1. remove node from self.freq[node.freq] doublylinkedlist
        2. update node.freq node.freq += 1
        3. add node to self.freq[node.freq] doublylinkedlist (this is old freq+1)
        4. if minfreq = old freq, and self.freqs[old freq].dllsize == 0: update minfreq to new freq = old freq + 1
        """
        freq = self.nums[key]
        # remove key from self.freqs[freq]
        self.freqs[freq].move_to_end(key)
        item = self.freqs[freq].popitem(last=True)
        newfreq = freq + 1
        # check minfreq
        if freq == self.minfreq and len(self.freqs[freq]) == 0:  # minfreq list is now empty
            self.minfreq = newfreq  # we know this node would move from freq to freq+1, so minfreq += 1
        # add key into self.freqs[newfreq]
        self.nums[key] = newfreq
        if value is not None:
            self.freqs[newfreq][key] = value # update to new value
        else:
            self.freqs[newfreq][key] = item[1] # dont' update value

    def get(self, key: int) -> int:
        # print('get key=%s self.nums=%s self.freqs=%s' % (key, self.nums, self.freqs))
        if key not in self.nums:
            # print('get key=%s returning %s' % (key, -1))
            return -1
        self._update(key, value=None)
        # print('get key=%s returning %s' % (key, self.freqs[self.nums[key]][key]))
        return self.freqs[self.nums[key]][key]

    def put(self, key: int, value: int) -> None:
        """
        if key exist, update freq and value in OrderedDict
        """
        # print('put key=%s value=%s self.nums=%s self.freqs=%s' % (key, value, self.nums, self.freqs))
        if self.capacity == 0:
            return
        if key in self.nums:
            self._update(key, value)
        else:
            # new key, evict one if cache full
            if self.size == self.capacity:
                # remove least frequently used item in self.freqs[self.minfreq]
                item = self.freqs[self.minfreq].popitem(last=False)
                del self.nums[item[0]]
                self.size -= 1
            self.freqs[1][key] = value
            self.size += 1
            self.nums[key] = 1
            self.minfreq = 1


"""
Design

use map to store key to node
dict of frequency {freq: doublylinkedlist of LRU of same freq}

key points:
1. self.minfreq keep track of minfreq, so when evicting least frequenty used, we can get it via self.freqs[self.minfreq]
2. keep freq inside node
3. keep doublylinkedlist size inside doublylinkedlist
4. keep total cache size in LFUCache self.size (to check capacity easily)
5. check capacity before adding new node
6. when updating node, move it from old freq list to new list, we need to update minfreq

mistakes:
1. use LFUCache.size instead of len(self.nums) to keep track of exceeding capacity or not

"""


class DLinkedNode:
    def __init__(self, key=-1, val=-1, prev=None, nxt=None):
        # use key=-1 and val=-1 to indicate dummy node
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt
        self.freq = 1

    def __repr__(self):
        return '{%s : %s (%s)}' % (self.key, self.val, self.freq)

class DLinkedList:
    """
    represent a Least Recently Used (LRU) list, excluding dummy head/tail, the first element is the most recently used
    when expiring least recently used, remove this.tail.prev
    """

    def __init__(self):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.dllsize = 0

    def add_node(self, node):
        """
        add node to right after dummy head
        """
        node.prev, node.nxt = self.head, self.head.nxt
        self.head.nxt.prev = node
        self.head.nxt = node
        self.dllsize += 1

    def remove_node(self, node):
        node_prev = node.prev
        node_nxt = node.nxt
        node_prev.nxt = node_nxt
        node_nxt.prev = node_prev
        self.dllsize -= 1

        return node

    def evict_lru(self):
        """
        evict the item with least recent use time for given freq
        """
        return self.remove_node(self.tail.prev)

    def move_to_head(self, node):
        """
        move a node to head (just used, updating to most recently used)
        """
        node = self.remove_node(node)
        self.add_node(node)

    def __repr__(self):
        ans = ''
        cur = self.head.nxt
        while cur != self.tail:
            ans +=  str(cur)
            cur = cur.nxt

        return ans

class LFUCache1:

    def __init__(self, capacity: int):
        self.size = 0  # total number of caches
        self.capacity = capacity
        self.nums = {}
        self.freqs = defaultdict(DLinkedList)
        self.minfreq = 0  # the minimum freq, to help identify which dll to evict an cached item

    def _update(self, node):
        """
        update node when add(key) or put(key) and the key exists already
        1. remove node from self.freq[node.freq] doublylinkedlist
        2. update node.freq node.freq += 1
        3. add node to self.freq[node.freq] doublylinkedlist (this is old freq+1)
        4. if minfreq = old freq, and self.freqs[old freq].dllsize == 0: update minfreq to new freq = old freq + 1
        """
        freq = node.freq
        self.freqs[freq].remove_node(node)
        newfreq = freq + 1
        node.freq = newfreq
        # check minfreq
        if freq == self.minfreq and self.freqs[freq].dllsize == 0:  # minfreq list is now empty
            self.minfreq = newfreq  # we know this node would move from freq to freq+1, so minfreq += 1
        if newfreq not in self.freqs:
            self.freqs[newfreq] = DLinkedList()
        self.freqs[newfreq].add_node(node)

    def get(self, key: int) -> int:
        # print('get key=%s self.nums=%s self.freqs=%s' % (key, self.nums, self.freqs))
        if key not in self.nums:
            print('get key=%s returning %s' % (key, -1))
            return -1
        node = self.nums[key]
        self._update(node)
        print('get key=%s returning %s' % (key, node.val))
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        if key exist, update node value, and update node
        """
        # print('put key=%s value=%s self.nums=%s self.freqs=%s' % (key, value, self.nums, self.freqs))
        if self.capacity == 0:
            return
        if key in self.nums:
            node = self.nums[key]
            node.val = value
            self._update(node)
        else:
            # new key, evict one if cache full
            if self.size == self.capacity:
                # remove last in doublylinkedlist in the smallest frequency
                node = self.freqs[self.minfreq].evict_lru()
                del self.nums[node.key]
                self.size -= 1
            node = DLinkedNode(key=key, val=value)
            if 1 not in self.freqs:
                self.freqs[1] = DLinkedList()
            self.freqs[1].add_node(node)
            self.size += 1
            self.nums[key] = node
            self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def main():
    obj = LFUCache(2)
    obj.put(1,1)
    obj.put(2,2)
    assert obj.get(1) == 1, 'fails'
    obj.put(3,3)
    assert obj.get(2) == -1, 'fails'
    assert obj.get(3) == 3, 'fails'
    obj.put(4,4)
    assert obj.get(1) == -1, 'fails'
    assert obj.get(3) == 3, 'fails'
    assert obj.get(4) == 4, 'fails'

    # obj = LFUCache(0)
    # obj.put(0,0)
    # assert obj.get(0) == -1, 'fails'


if __name__ == '__main__':
   main()