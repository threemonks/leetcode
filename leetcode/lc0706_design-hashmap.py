"""
706. Design HashMap
Easy

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.

"""
"""
Design

Use LinkedList to hold data for given hash value

since key is always int, we can use key % size => array index
hash collision = > chain [key, val] pairs
consider load factor or not?

time: N = # of keys/buckets
      M = avg length of linkedlist
      O(M) for put, get, remove
      if N >> M, we can assume O(1) for put, get, remove
"""
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def __repr__(self):
        return '[{%s: %s} %s]' % (self.key, self.val, self.next)

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 101 # prime number
        self.data = [None for _ in range(self.size)] # holds linkedlist heads


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        if not self.data[idx]:
            # create new node as linkedlist head
            self.data[idx] = ListNode(key=key, val=value)
        else:
            # update if exists, else append
            cur = self.data[idx]
            prev = cur
            while cur:
                if cur.key == key:
                    cur.val = value
                    break
                prev = cur
                cur = cur.next

            if not cur: # didn't find after reached end, append here
                prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        cur = self.data[idx]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        if not cur:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # print('before remove self.data=%s' % self.data)
        idx = key % self.size
        if not self.data[idx]:
            return
        # process if first node key,value matchs
        if self.data[idx] and self.data[idx].key == key:
            self.data[idx] = self.data[idx].next
        else:
            # process if removed value is not head of linkedlist
            cur = self.data[idx]
            prev = cur
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    break
                prev = cur
                cur = cur.next

        # print('after remove self.data=%s' % self.data)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


def main():
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1, 'fails'
    assert obj.get(3) == -1, 'fails'
    obj.put(2, 1)
    assert obj.get(2) == 1, 'fails'
    obj.remove(2)
    assert obj.get(2) == -1, 'fails'


if __name__ == '__main__':
   main()