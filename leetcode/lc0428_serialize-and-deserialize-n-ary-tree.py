"""
428. Serialize and Deserialize N-ary Tree
Hard
"""
from collections import deque

"""
# Definition for a Node.

"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

"""
Tree

key points for N-ary tree serialize/deserialize
1. preorder DFS traverse
2. use special symbol # to indicate empty
3. to always store number of children right after root val

"""


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return '#'
        return ','.join([str(root.val), str(len(root.children))] + [self.serialize(child) for child in root.children])

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        tokens = data.split(',')
        q = deque(tokens)

        def helper(q):
            s = q.popleft()
            if s == '#':
                return None
            root = Node(s, children=[])
            num_children = int(q.popleft())
            if num_children:
                for i in range(num_children):
                    child = helper(q)
                    root.children.append(child)

            return root

        return helper(q)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
