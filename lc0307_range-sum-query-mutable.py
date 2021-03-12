"""
307. Range Sum Query - Mutable
Medium
"""
from typing import List


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = None
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start > end:  # nothing to build
            return None
        node = Node(start, end)
        if start == end:
            node.sum = nums[start]
            return node
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
        if start > end:
            return 0
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
Segment Tree
"""


class NumArray0:

    def __init__(self, nums: List[int]):
        self.segtree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segtree.update(self.segtree.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segtree.sum_range(self.segtree.root, left, right)


"""
Binary Index Tree (BIT)
"""


class BIT:
    def __init__(self, nums):
        n = len(nums)
        # init BIT as 0
        self.parent = [0] * (n + 1)

        # store actual values in bit_tree[] using add()
        for idx in range(n):
            self.add(idx, nums[idx])

    # returns sum of arr[0...index]. this function assumes that
    # the array is preprocessed and partial sums of array elements are stored in bit_tree[]
    def sum(self, idx):
        # sum all elements up to index idx
        # index in bit_tree is 1 more than index in arr[]
        idx = idx + 1
        result = 0
        while idx:
            result += self.parent[idx]
            idx -= idx & -idx  # find parent index, i.e., removing right most bit 1
        return result

    # updates a node in Binary Index Tree (bit_tree) at given index in bit_tree
    # the given value 'val' is added to bit_tree[i] and all of its ancestors in tree
    def add(self, idx, val):
        # index in bit_tree is 1 more than index in arr[]
        idx += 1
        while idx < len(self.parent):
            self.parent[idx] += val
            idx += idx & -idx  # go to parent


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bittree = BIT(nums)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.bittree.add(index, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.bittree.sum(right) - self.bittree.sum(left - 1)
    # Your NumArray object will be instantiated and called as such:


# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

def main():

    obj = NumArray([1, 3, 5])
    assert obj.sumRange(0, 2) == 9, 'fails'
    obj.update(1, 2)
    assert obj.sumRange(0, 2) == 8, 'fails'

if __name__ == '__main__':
   main()