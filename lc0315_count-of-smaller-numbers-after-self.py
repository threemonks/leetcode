"""
315. Count of Smaller Numbers After Self
Hard

3392

106

Add to List

Share
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
import bisect
from typing import List

"""
SortedDict

sorteddict counts {num: count of numbers from n-1 to i} keep updating it as we go left, at each step, we binary search counts to find index of all keys < nums[i], sum all these values

TLE
"""
from sortedcontainers import SortedDict


class Solution0:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = SortedDict()
        ans = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            num = nums[i]
            pos = counts.bisect(num - 1)  # all numbers <= num-1
            # print('i=%s num=%s pos=%s' % (i, num, pos))
            ans[i] = sum(counts.values()[:pos])
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        return ans


"""
Segment Tree

1. as we process the original array from right to left, we store counts of each number in an hash table (could use array if we shift numbers range from -10^4 to 10^4 to 0 to 2*10^4)
2. we store this counts hashtable in segment tree, as we update the hashtable, we call range sum on segment tree, which will return count of numbers smaller than current number to right (since we only processed numbers on right so far)


time O(Nlog(N))

mistakes:
1. seg tree range is min(nums) - max(nums) - this is too large, we use
indicies = {v: idx for idx, v in enumerate(nums)}
and use seg tree range (0, len(indices))
2. to get all counts <nums[i], call range sum on [minn, nums[i]-1]
"""
from collections import defaultdict


class Node:
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s (%s - %s)' % (self.val, self.start, self.end)


class SegmentTree:
    def __init__(self, n):
        # build an empty tree with all value 0
        self.root = self.build_tree(0, n - 1)

    def build_tree(self, start, end):
        if start > end:
            return None
        root = Node(start, end, val=0)
        if start == end:
            return root
        else:
            mid = start + (end - start) // 2
            root.left = self.build_tree(start, mid)
            root.right = self.build_tree(mid + 1, end)
            return root

    def update(self, node, idx, val):
        # if out of bound, do nothing
        if idx < node.start or idx > node.end:
            return
        if node.start == node.end and node.start == idx:
            node.val = val
            return
        mid = node.start + (node.end - node.start) // 2
        if idx <= mid:
            self.update(node.left, idx, val)
        else:
            self.update(node.right, idx, val)

        node.val = node.left.val + node.right.val

    def range_sum(self, node, start, end):
        # empty range
        if start > end:
            return 0
        # exact range match
        if start == node.start and end == node.end:
            return node.val
        mid = node.start + (node.end - node.start) // 2
        # only in left subtree:
        if end <= mid:
            return self.range_sum(node.left, start, end)
        # only in right subtree:
        elif start >= mid + 1:
            return self.range_sum(node.right, start, end)
        else:  # need sum from both side
            return self.range_sum(node.left, start, mid) + self.range_sum(node.right, mid + 1, end)


class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        indices = {v: i for i, v in enumerate(sorted(set(nums)))}
        st = SegmentTree(len(indices))

        ans = []
        counts = defaultdict(int)  # stores counts of each number occurance from right end till current number
        for i in range(n - 1, -1, -1):
            ans.append(st.range_sum(st.root, 0, indices[nums[i]] - 1))
            counts[nums[i]] += 1
            st.update(st.root, indices[nums[i]], counts[nums[i]])

        return ans[::-1]


"""
ZKW Segment Tree (more efficient seg tree)

similar as above

Note: ZKW tree tree[0] is not used, node tree[i]'s parent is at tree[i//2], its left and right child is at tree[2*i], tree[2*i+1]

time O(Nlog(N))
mistakes1:
1. no need build method since all init to zero, value set by update.
2. 
"""
from collections import defaultdict


class ZKWSegmentTree:
    def __init__(self, n):
        self.n = n  # index shift, since leaf node index is from n to 2*n-1
        self.tree = [0] * (2 * n)  # all zero, no need to build
        # self.tree = self.build_tree([0]*n)

    #     def build_tree(self, nums):
    #         # insert nums at leaf node
    #         for i in range(self.n):
    #             self.tree[self.n+i] = nums[i]

    #         # build tree by calculating parent
    #         for i in range(self.n):
    #             self.tree[i] = self.tree[i<<1] + self.tree[(i<<1)|1]

    def update(self, i, val):
        # set value at position idx
        i += self.n
        self.tree[i] = val

        # update parent up to root
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]  # i^1 turns 0 to 1, 1 to 1, etc, get left/right child
            i >>= 1

    def range_sum1(self, left, right):
        """range is [left, right), i.e., right is exclusive """
        left, right = left + self.n, right + self.n

        res = 0
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.tree[right]

            left >>= 1
            right >>= 1

        return res

    def range_sum(self, left, right):
        """range is [left, right], i.e., both left and right are inclusive """
        left, right = left + self.n, right + self.n

        res = 0
        while left <= right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1 == 0:
                res += self.tree[right]
                right -= 1

            left >>= 1
            right >>= 1

        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        indices = {v: i for i, v in enumerate(sorted(set(nums)))}
        st = ZKWSegmentTree(len(indices))

        ans = []
        counts = defaultdict(int)  # stores counts of each number occurance from right end till current number
        for i in range(n - 1, -1, -1):
            # ans.append(st.range_sum1(0, indices[nums[i]]))
            ans.append(st.range_sum(0, indices[nums[i]] - 1))
            counts[nums[i]] += 1
            st.update(indices[nums[i]], counts[nums[i]])

        return ans[::-1]


"""
Sort and Binary Search

iterate array from right to left, for visited nums, add into new array, before add, search its insertion location using binary search, the insertion location index is # of numbers smaller to right

"""


class Solution3:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        ans = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            num = nums[i]
            idx = bisect.bisect_left(arr,
                                     num)  # when insert num at idx, all val to left < num, and all val to right >= num
            arr.insert(idx, num)
            ans[i] = idx

        return ans

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        indices = {v: i for i, v in enumerate(sorted(set(nums)))}
        st = SegmentTree(len(indices))

        ans = []
        counts = defaultdict(int)  # stores counts of each number occurance from right end till current number
        for i in range(n - 1, -1, -1):
            ans.append(st.range_sum(st.root, 0, indices[nums[i]] - 1))
            counts[nums[i]] += 1
            st.update(st.root, indices[nums[i]], counts[nums[i]])

        return ans[::-1]


"""
Sort and Binary Search

iterate array from right to left, for visited nums, add into new array, before add, search its insertion location using binary search, the insertion location index is # of numbers smaller to right

"""


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        ans = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            num = nums[i]
            idx = bisect.bisect_left(arr,
                                     num)  # when insert num at idx, all val to left < num, and all val to right >= num
            arr.insert(idx, num)
            ans[i] = idx

        return ans


def main():
    sol = Solution()
    assert sol.countSmaller(nums = [5,2,6,1]) == [2,1,1,0], 'fails'

    assert sol.countSmaller(nums = [-1]) == [0], 'fails'

    assert sol.countSmaller(nums = [-1,-1]) == [0, 0], 'fails'


if __name__ == '__main__':
   main()