"""
25. Reverse Nodes in k-Group
Hard
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
LinkedList reverse every k nodes group

1. create new LinkedList, for each node on original list, insert into head of new list
2. when finished k nodes, we have a length k reversed list, whose head will be returned as reversed new list head
3. before return, recursively call reverseKGroup on the k+1 node on original list, and attach the result back to the first reversed list
4. base case is:
    head == None => none
    len(list) < k => noop, return head

"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        l = 0
        p = head
        while p:
            p = p.next
            l += 1

        # dont swap if k is larger than remaining length
        if k > l:
            return head

        reversed_head = None
        reversed_tail = None
        curr = head
        i = 0
        while i < k:
            reversed_head = ListNode(curr.val, next=reversed_head)
            if not reversed_tail:
                reversed_tail = reversed_head  # record tail of new list, so that we can connect back to remaining list
            curr = curr.next
            i += 1

        reversed_tail.next = self.reverseKGroup(curr, k)

        return reversed_head