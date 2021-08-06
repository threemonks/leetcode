"""
Rgular Segement Tree

"""
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = None
        self.left = None
        self.right = None


class SegmentTree:
    """
    Segment Tree for range sum

    """
    def __init__(self, nums):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start > end:  # nothing to build
            return None
        node = Node(start, end)
        if start == end:
            node.sum = nums[start]
        else:  # split and call build_tree on left and right range recursively
            mid = start + (end - start) // 2
            node.left = self.build_tree(nums, start, mid)
            node.right = self.build_tree(nums, mid + 1, end)
            node.sum = node.left.sum + node.right.sum
        return node

    def update(self, node, index, val):
        if node.start == node.end:  # leaf node, update directly
            node.sum = val
            return
        mid = node.start + (node.end - node.start) // 2
        if index <= mid:  # only in left subtree
            self.update(node.left, index, val)
        else:  # index > mid # only in right subtree
            self.update(node.right, index, val)

        # update sum of this node
        node.sum = node.left.sum + node.right.sum

    def sum_range(self, node, start, end):
        # empty rnage
        if start > end:
            return 0
        # exact range match
        if node.start == start and node.end == end:
            return node.sum
        mid = node.start + (node.end - node.start) // 2
        if end <= mid:  # only in left subtree
            return self.sum_range(node.left, start, end)
        elif start > mid:  # only in right subtree
            return self.sum_range(node.right, start, end)
        else:  # query both left and right subtree, then combine the result
            return self.sum_range(node.left, start, mid) + self.sum_range(node.right, mid + 1, end)

"""
https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

https://blog.csdn.net/u013351484/article/details/46698985

zkw线段树必须是点树，即完全闭区间
采用堆结构，构造一颗满二叉树（也可以说是完全二叉树）
而二叉树的最后一层则是各个节点。

ZKW Segement tree - array based
Note: use 2*n array to represent, n,...,2n-1 are leaf node, holding array value
      1,...,n-1 are parents
      tree[0] is not used
      each node at i, its parent is at index i//2
      its left and right child are at index 2*i, 2*i+1
"""

class ZKWSegTree:
    def __init__(self, nums):
        self.l = len(nums)
        # build tree by inserting nums at leaf
        self.tree = [0]*self.l + nums

        # update parent nodes
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) | 1]

    # function to update a tree node
    def update(self, i, value):
        # set value at position i
        n = self.l + i # all node values are at self.l to 2*self.l-1, so shift index by self.l
        self.tree[n] = value

        # # recursively update parents
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1] # n^1 will get corresponding left/right child, 0<->1
            n >>= 1

        # alternative, we can traverse to parent first, then update
        # n >>= 1
        # while n:
        #     self.tree[n] = self.tree[n>>1] + self.tree[(n>>1)|1] # n^1 will get corresponding left/right child, 0<->1
        #     n >>= 1

    # function to get sum on interval [l, r]
    # 一）ans = 0；
    # 二）如果left为偶数，ans就加上左子树的右结点的值；如果right为奇数，ans就加上右子树的左结点的值；
    # 三）left 和 right 分别除以2后(到父节点)，如果left > right，就退出循环
    def range_sum(self, l, r):
        left, right = self.l+l, self.l+r # shift index by self.l
        res = 0
        while left <= right:
            if left & 1: # 左节点为偶数，加入区间和，否则跳过
                res += self.tree[left]
                left += 1
            left >>= 1
            if (right & 1) == 0: # 右节点为奇数，加入区间和，否则跳过
                res += self.tree[right]
                right -= 1
            right >>= 1

        return res


# Driver Code
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # n is global
    n = len(a)

    # build tree
    zkwst = ZKWSegTree(a)

    # print the sum in range(1,2) index-based
    assert zkwst.range_sum(1, 2) == 5

    # modify element at 2nd index
    zkwst.update(2, 1)

    # print the sum in range(1,2) index-based
    assert zkwst.range_sum(1, 2) == 3

# This code is contributed by AnkitRai01
