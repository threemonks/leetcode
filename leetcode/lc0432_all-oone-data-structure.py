"""
432. All O`one Data Structure
Hard

776

94

Add to List

Share
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".


Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"


Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 3 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.


Follow up: Could you apply all the operations in O(1) time complexity?
"""
from sortedcontainers import SortedDict
from sortedcontainers import SortedDict

"""
SortedDict + DoubleLinkedList

and sorted doubly linkedlist of word set for counts {1: set('word1', 'word2')} -> {2: set('word3', 'word3')}, sort by count
also dict of word to linkedlist node {'word1': node1}
use a dummy head and tail for doubly linkedlist, for fast lookup of min/max

then use another dict/hashmap to store {word: node} that points to a node in the linkedlist, for each inc/dec, the count just change by 1, so we know in linkedlist the new node to add woud be just immediate previous/next

time O(1) for all operations
"""


class Node:
    """
    DoubleLinkedList Node, holding key/word sets
    """

    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt
        self.keys = set()

    def __repr__(self):
        return str(self.val) + ':' + str(self.keys)


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0, prev=self.head)
        self.head.nxt = self.tail
        # print('head.nxt=%s tail.prev=%s' % (self.head.nxt, self.tail.prev))

        self.key2node = {}  # key to node in doubly linkedlist node that contains this key

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # print('inc key=%s' % key)
        if key in self.key2node:
            node = self.key2node[key]
            count = node.val
            # new node would be the following one in linkedlist, if not, insert it
            if node.nxt.val == count + 1:
                # found node with val count+1, add keys
                node.nxt.keys.add(key)
                # update key2node map
                self.key2node[key] = node.nxt
            else:  # need to add a new node with val count + 1 after between node and node.nxt
                new_node = Node(count + 1)
                new_node.keys.add(key)
                # insert new_node between node and node.nxt
                new_node.prev, new_node.nxt = node, node.nxt
                node.nxt.prev = new_node
                node.nxt = new_node
                # update key2node map
                self.key2node[key] = new_node
            # remove oldcount
            node.keys.remove(key)
            # if node.keys == 0, we need to drop this node
            if len(node.keys) == 0:
                # drop node from linked list
                node_prev = node.prev
                node_nxt = node.nxt
                node_prev.nxt = node_nxt
                node_nxt.prev = node_prev
        else:  # add key with count 1
            if self.head.nxt.val == 1:  # if there's value 1, it must be in self.head.nxt
                self.head.nxt.keys.add(key)
                self.key2node[key] = self.head.nxt
            else:
                # add new node with value 1
                new_node = Node(1)
                new_node.keys.add(key)
                # insert it into linked list between self.head and self.head.nxt
                new_node.prev, new_node.nxt = self.head, self.head.nxt
                self.head.nxt.prev = new_node
                self.head.nxt = new_node
                self.key2node[key] = new_node

        # print('inc' + str(self.key2node))
        # print('inc head.nxt=%s tail.prev=%s' % (self.head.nxt, self.tail.prev))

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        # print('dec key=%s' % key)
        if key in self.key2node:
            node = self.key2node[key]
            count = node.val
            # add key to previous node with count-1 or new
            if count - 1 > 0:
                if node.prev and node.prev.val == count - 1:
                    node.prev.keys.add(key)
                    self.key2node[key] = node.prev
                else:
                    # count-1 does not exist in linkedlist, needs to add new node
                    new_node = Node(count - 1)
                    new_node.keys.add(key)
                    # insert new_node into linkedlist, between node and node.prev
                    new_node.prev, new_node.nxt = node.prev, node
                    node.prev.nxt = new_node
                    node.prev = new_node
                    # update key2node
                    self.key2node[key] = new_node
            else:
                # key no longer in linkedlist, remove from key2node map
                del self.key2node[key]

            # remove key from old node
            node.keys.remove(key)
            # drop this node if no keys in it
            if len(node.keys) == 0:
                # drop this node
                node_prev = node.prev
                node_nxt = node.nxt
                node_prev.nxt = node_nxt
                node_nxt.prev = node_prev

        else:
            raise Exception('this should not happen')

        # print('dec' + str(self.key2node))
        # print('dec head.nxt=%s tail.prev=%s' % (self.head.nxt, self.tail.prev))

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        # print('getMaxKey tail.prev=%s key2node=%s' % (self.tail.prev, self.key2node))
        if not self.tail.prev or not self.tail.prev.keys:
            return ""
        return next(iter(self.tail.prev.keys))  # read one value from set

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        # print('getMinKey head.nxt=%s key2node=%s' % (self.head.nxt, self.key2node))
        if not self.head.nxt or not self.head.nxt.keys:
            return ""
        return next(iter(self.head.nxt.keys))  # read one from set


"""
Hash Map

two dicts:
words {word: count}
counts {count: [word list]}

we need max count and min count by value, do we use heap? but how do we lookup key by value?

using SortedDict for counts, O(log(N)) inc and dec, O(1) getMin and getMax

using dict for words and array of list for counts, then it is O(1) for inc and dec, but O(log(N))

"""


class AllOne1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = dict()
        self.counts = SortedDict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # print('inc key=%s' % key)
        # print(self.words)
        # print(self.counts)
        if key in self.words:
            # remove old map in counts
            self.counts[self.words[key]].remove(key)
            if not self.counts[self.words[key]]:
                del self.counts[self.words[key]]
            # now increase count
            self.words[key] += 1
            # now update counts map
            if self.words[key] in self.counts:
                self.counts[self.words[key]].append(key)
            else:
                self.counts[self.words[key]] = [key]
        else:
            self.words[key] = 1
            if 1 in self.counts:
                self.counts[1].append(key)
            else:
                self.counts[1] = [key]

        # print(self.words)
        # print(self.counts)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        # print('dec key=%s' % key)
        # print(self.words)
        # print(self.counts)
        # remove counts map entry
        self.counts[self.words[key]].remove(key)
        if not self.counts[self.words[key]]:
            del self.counts[self.words[key]]
        # reduce counts
        self.words[key] -= 1
        if self.words[key] == 0:
            del self.words[key]
        else:
            # add this key to counts map with new count
            if self.words[key] in self.counts:
                self.counts[self.words[key]].append(key)
            else:
                self.counts[self.words[key]] = [key]
        # print(self.words)
        # print(self.counts)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        # print('getMaxKey')
        # print(self.words)
        # print(self.counts)

        if not self.counts:
            return ""
        return self.counts.peekitem(-1)[1][-1]

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        # print('getMinKey')
        # print(self.words)
        # print(self.counts)

        if not self.counts:
            return ""
        return self.counts.peekitem(0)[1][-1]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

def main():
        allOne = AllOne()
        allOne.inc("hello")
        allOne.inc("hello")
        assert allOne.getMaxKey() == 'hello', 'fails'
        assert allOne.getMinKey() == 'hello', 'fails'
        allOne.inc("leet")
        assert allOne.getMaxKey() == 'hello', 'fails'
        assert allOne.getMinKey() == 'leet', 'fails'

if __name__ == '__main__':
   main()