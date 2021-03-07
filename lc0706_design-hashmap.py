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
Hash Table

1. define a data structure to hold the data - LinkedList
2. define hashing function 
3. use chaining when collision happens, mulitple key hashed into same hash value, we add it to a LinkedList on that hash key
4. load factor and re-hashing - do we need to define load factor, and rehash all values if exceeding load factor threshold

mistakes:
1. need to chain to handle hash collision
2. null pointer check
"""


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def __repr__(self):
        return '{%s: %s)' % (self.key, self.val)


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 7  # use prime number as capacity for hashing
        self.data = [None for _ in range(self.capacity)]

    def hashcode(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed = self.hashcode(key)
        if not self.data[hashed]:
            self.data[hashed] = ListNode(key, value)
        else:
            curr = self.data[hashed]
            prev = curr
            while curr:
                if curr.key == key:
                    curr.val = value  # update
                    # print('update key=%s value=%s data=%s' % (key, value, self.data))
                    return
                prev, curr = curr, curr.next

            # not found
            prev.next = ListNode(key, value)

        # print('put key=%s value=%s data=%s' % (key, value, self.data))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed = self.hashcode(key)
        curr = self.data[hashed]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        # not found
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashed = self.hashcode(key)
        curr = self.data[hashed]
        prev = curr
        if self.data[hashed] and self.data[hashed].key == key:
            self.data[hashed] = self.data[hashed].next
            # print('remove key=%s data=%s' % (key, self.data))
        while curr:
            if curr.key == key:
                prev.next = curr.next
                # print('remove key=%s data=%s' % (key, self.data))
                break
            prev, curr = curr, curr.next


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