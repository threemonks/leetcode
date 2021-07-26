"""
450. Delete Node in a BST
Medium

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?



Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-10^5 <= key <= 10^5
"""

"""
BST
recursively delete and merge

time O(log(N))
space O(log(N))
"""

class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        n = len(nums)
        if n <= k:
            return "0"

        stack = []
        pop_count = 0

        for i, num in enumerate(nums):
            while stack and num < stack[-1] and pop_count < k:
                stack.pop()
                pop_count += 1
            stack.append(num)
            # print(stack)
        # if there's more digits left in stack than needed
        while stack and pop_count < k:
            stack.pop()
            pop_count += 1

        # print(stack)
        res = ''.join(stack).lstrip('0')
        return res if res else "0"

        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        def successor(root):
            root = root.right
            while root.left:
                root = root.left
            return root

        def predecessor(root):
            root = root.left
            while root.right:
                root = root.right
            return root

def main():
    sol = Solution()
    assert sol.removeKdigits("1432219", 3) == "1219", 'fails'

    assert sol.removeKdigits("10200", 1) == "200", 'fails'

    assert sol.removeKdigits("10", 2) == "0", 'fails'

    assert sol.removeKdigits("112", 1) == "11", 'fails'

if __name__ == '__main__':
   main()