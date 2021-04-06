"""
331. Verify Preorder Serialization of a Binary Tree
Medium

One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.


For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".


Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: preorder = "1,#"
Output: false
Example 3:

Input: preorder = "9,#,#,1"
Output: false


Constraints:

1 <= preorder.length <= 10^4
preoder consist of integers in the range [0, 100] and '#' separated by commas ','.


Follow up: Find an algorithm without reconstructing the tree.
"""
"""
Binary Tree

observation:
We start with one slot, every number would consume one slot, andadd two slots (two children of a node), and any non-number ('#') would consume one slot, but add none.

At the end, we should have zero empty slot for this to be valid BST serialization

"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        tokens = preorder.split(',')
        for i, t in enumerate(tokens):
            # print('i=%s t=%s slots=%s' % (i, t, slots))
            slots -= 1
            if slots < 0:
                return False
            if t != '#':
                slots += 2

        return slots == 0


def main():
    sol = Solution()
    assert sol.isValidSerialization(preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#") is True, 'fails'

    assert sol.isValidSerialization(preorder = "1,#") is False, 'fails'

    assert sol.isValidSerialization(preorder = "9,#,#,1") is False, 'fails'


if __name__ == '__main__':
   main()
