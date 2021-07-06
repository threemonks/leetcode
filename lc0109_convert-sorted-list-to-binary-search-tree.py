"""
109. Convert Sorted List to Binary Search Tree
Medium

3420

102

Add to List

Share
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]


Constraints:

The number of nodes in head is in the range [0, 2 * 10^4].
-10^5 <= Node.val <= 10^5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
LinkedList / BST

Since linked list is sorted ascending, which matches with BST inorder traversal, so the middle point of linkedlist would be root of balanced BST. So we can use divide conquer (after finding middle point using fast and slow pointers) and recursively build BST from each half of the linked list, then combine left and right subtree and root into one BST.

time: O(N*log(N)) - log(N) for divide & conquer, N for find mid point
space: O(1) # constant space
mistakes:
1. handle null input or single element input
"""


class Solution0:
    def find_mid(self, head):
        if not head or not head.next:  # single node
            return head

        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # now slow is pointing at middle point
        if prev:  # break the two lists
            prev.next = None

        return slow

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        mid = self.find_mid(head)
        left = self.sortedListToBST(head)
        if mid:
            right = self.sortedListToBST(mid.next)
        else:
            right = None
        return TreeNode(mid.val, left=left, right=right)


"""
LinkedList / BST

Convert LinkedList into array O(N), then we can find mid point O(1), then it takes O(log(N)) to build BST from array

time O(N)
space O(N)
"""


class Solution:
    def arrayToBST(self, nums):
        if not nums:
            return None

        n = len(nums)

        if n == 1:
            return TreeNode(nums[0])

        m = n // 2
        root = TreeNode(nums[m])
        root.left = self.arrayToBST(nums[:m])
        root.right = self.arrayToBST(nums[m + 1:])

        return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return self.arrayToBST(nums)
