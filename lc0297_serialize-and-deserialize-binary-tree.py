"""
297. Serialize and Deserialize Binary Tree
Hard

"""
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
DFS Preorder traverse to serialize

for deserialize, since we used preorder to serialize, we process following pattern root, left, right, with left and right size being equal
in this serialization, all leaf node would have two empty children marked by special char '#'

Note: this is natural serialization

"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        res = ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tokens = deque(data.split(','))

        def helper(q):
            s = q.popleft()
            if s == '#':
                return None

            root = TreeNode(int(s))
            root.left = helper(q)
            root.right = helper(q)

            return root

        return helper(tokens)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


def main():
    from lc_tools import deserialize
    codec = Codec()
    codec.deserialize(codec.serialize(deserialize("""[1,2,3,null,null,4,5]""")))

if __name__ == '__main__':
   main()