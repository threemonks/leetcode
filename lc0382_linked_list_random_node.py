"""
382. Linked List Random Node
Medium

https://leetcode.com/problems/linked-list-random-node/
"""
import random

"""
keep a counter count, for each new call to getRandom, we return the new value with probability 1/count
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res, count = -1, 0
        curr = self.head
        while curr:
            count += 1
            if random.randint(1, count) == 1:
                res = curr.val
            curr = curr.next

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


def main():
    head = ListNode(1, next=ListNode(2, next=ListNode(3)))
    sol = Solution(head)
    assert sol.getRandom() in [1, 2, 3], 'fails'

if __name__ == '__main__':
   main()