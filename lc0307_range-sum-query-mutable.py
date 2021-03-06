"""
307. Range Sum Query - Mutable
Medium

1781

106

Add to List

Share
Given an array nums and two types of queries where you should update the value of an index in the array, and retrieve the sum of a range in the array.

Implement the NumArray class:

NumArray(int[] nums) initializes the object with the integer array nums.
void update(int index, int val) updates the value of nums[index] to be val.
int sumRange(int left, int right) returns the sum of the subarray nums[left, right] (i.e., nums[left] + nums[left + 1], ..., nums[right]).


Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 9 = sum([1,3,5])
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // return 8 = sum([1,2,5])


Constraints:

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 10^4 calls will be made to update and sumRange.
"""
from typing import List


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = None
        self.left = None  # left child
        self.right = None  # right child


class SegmentTree:
    def __init__(self, nums):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start > end:
            return None
        node = Node(start, end)
        if start == end:
            node.sum = nums[start]
        else:  # recusrively build tree on left and right subtree
            mid = start + (end - start) // 2
            node.left = self.build_tree(nums, start, mid)
            node.right = self.build_tree(nums, mid + 1, end)
            node.sum = node.left.sum + node.right.sum
        return node

    def update(self, node, index, val):
        if node.start == node.end:
            node.sum = val
            return
        # recursively try to locate index and update in left or right subtree
        mid = node.start + (node.end - node.start) // 2
        if index <= mid:  # only in left subtree
            self.update(node.left, index, val)
        else:  # only in right subtree
            self.update(node.right, index, val)
        # update sum of this node
        node.sum = node.left.sum + node.right.sum

    def sum_range(self, node, start, end):
        if start > end:
            return 0
        if node.start == start and node.end == end:
            return node.sum
        mid = node.start + (node.end - node.start) // 2
        if end <= mid:  # all in left subtree
            return self.sum_range(node.left, start, end)
        elif start > mid:  # all in right subtree
            return self.sum_range(node.right, start, end)
        else:  # spans both left and right subtree, needs to query both
            return self.sum_range(node.left, start, mid) + self.sum_range(node.right, mid + 1, end)


class NumArray0:

    def __init__(self, nums: List[int]):
        self.segtree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segtree.update(self.segtree.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segtree.sum_range(self.segtree.root, left, right)


"""
ZKW Segment tree

always construct complete binary tree, use 2*n size array to hold data, all values are stored at leaf node, parent nodes (0...l-1) holds range query sum/min/max,

"""


class ZKWSegmentTree:
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums  # insert numbers at leaf node
        # update parent nodes
        for i in range(self.l - 1, -1, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[
                (i << 1) | 1]  # sum two child nodes, (i<<1)|1 gets silbing node

    def update(self, i, val):
        n = self.l + i  # shift index
        self.tree[n] = val
        # update parent
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]  # n^1 gets its sibling 0<->1
            n >>= 1

    def sum_range(self, left, right):
        left, right = self.l + left, self.l + right  # shift index
        ans = 0
        while left <= right:
            if left & 1:  # 左边偶节点加入和
                ans += self.tree[left]
                left += 1
            left >>= 1
            if right & 1 == 0:  # 右边奇数节点加入和
                ans += self.tree[right]
                right -= 1
            right >>= 1

        return ans


class NumArray1:

    def __init__(self, nums: List[int]):
        self.st = ZKWSegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.sum_range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

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


class NumArray2:

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


"""
Fenwick Tree / BIT

Fenwick Tree stores sums

"""


class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)  # go to right sibling (add lowbit)

    def query(self, i):  # this sums from elements from 1, 2, ..., i
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)  # go to parent
        return s

    def _lowbit(self, i):
        return i & (-i)


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.fwt = FenwickTree(len(nums))
        for i, num in enumerate(nums):
            self.fwt.update(i + 1, num)

    def update(self, index: int, val: int) -> None:
        self.fwt.update(index + 1, val - self.nums[index])
        self.nums[index] = val  # update self.nums as well so we can get delta properly later on

    def sumRange(self, left: int, right: int) -> int:
        # print('sumrange left=%s right=%s' % (left, right))
        return self.fwt.query(right + 1) - self.fwt.query(left + 1 - 1)


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