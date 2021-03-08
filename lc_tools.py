# Definition for a binary tree node.
import re
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q: return True
    if (p and not q) or (not p and q): return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def equal(self, other):
        while self and other and self.val == other.val:
            self = self.next
            other = other.next
        if not self and not other:
            return True
        return False

def print_linked_list(head):
    output = []
    node = head
    while node:
        output.append(node.val)
        node = node.next

    return "->".join([str(o) for o in output])

def deserialize_linked_list(s):
    arr = [int(c) for c in re.split('->', s)]
    pseudo_head = ListNode()
    curr = pseudo_head
    for a in arr:
        curr.next = ListNode(a)
        curr = curr.next

    return pseudo_head.next


"""
StefanPochmann

https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
"""

def serialize(root):
    s = ''
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            s += str(node.val) + ','
            queue += node.left, node.right
        else:
            s += 'null,'
    return '[' + s.strip('nul,') + ']'

def serialize1(root):
    vals = []
    queue = deque([root])
    todo = 1 if root else 0
    while todo:
        node = queue.popleft()
        if node:
            todo -= 1
            vals.append(str(node.val))
            for kid in node.left, node.right:
                queue.append(kid)
                if kid:
                    todo += 1
        else:
            vals.append('null')
    return '[' + ','.join(vals) + ']'

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))