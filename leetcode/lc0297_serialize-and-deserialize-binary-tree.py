"""
297. Serialize and Deserialize Binary Tree
Hard

"""
# Definition for a binary tree node.

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
use preorder DFS traverse , use ',' to separate node, use special symbol, such as '#', to indicate null/no child

for deserialize, split string into list of tokens, recursively process remaining tokens, if first char is '#', return None, otherwise pop first char to construct root, then recursively construct left and right child/substree from remaining tokens.
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tokens = list(data.split(','))

        def helper(q):
            # recursively process the remaining tokens
            s = q.popleft()
            if s == '#':
                return None

            # root
            root = TreeNode(s)
            root.left = helper(q)
            root.right = helper(q)

            return root

        return helper(deque(tokens))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


def main():
    from leetcode.lc_tools import deserialize
    codec = Codec()
    codec.deserialize(codec.serialize(deserialize("""[1,2,3,null,null,4,5]""")))

if __name__ == '__main__':
   main()