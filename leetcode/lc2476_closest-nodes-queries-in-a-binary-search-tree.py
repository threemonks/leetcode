"""
2476. Closest Nodes Queries in a Binary Search Tree
Medium

19

16

Add to List

Share
You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.



Example 1:


Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
Output: [[2,2],[4,6],[15,-1]]
Explanation: We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].
Example 2:


Input: root = [4,null,9], queries = [3]
Output: [[-1,4]]
Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].


Constraints:

The number of nodes in the tree is in the range [2, 10^5].
1 <= Node.val <= 10^6
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 10^6
"""
# Definition for a binary tree node.
import bisect
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

"""
convert binary search tree to sorted list nums

also sort queries with its index

scan sorted list nums to get mini <= qi <= maxi
"""


class Solution0:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = []

        stack = []

        while root or stack:
            # go to left most leaf
            while root:
                stack.append(root)
                root = root.left
            # now process
            root = stack.pop()
            nums.append(root.val)
            # process right
            root = root.right

        nums = sorted(nums)
        n = len(nums)

        # print(f"{nums = }")

        q = sorted([(query, idx) for idx, query in enumerate(queries)])
        # print(f"{q = }")
        m = len(q)

        mins = []
        i = 0  # i is pointer on nums, j is pointer on q
        for j in range(m):
            # print(f"{i = } {j = } {nums = } {q = } {mins = }")
            local_min = -1
            while i < n and nums[i] <= q[j][0]:
                local_min = max(local_min, nums[i])
                i += 1
            mins.append((local_min, q[j][1]))
            if i - 1 >= 0:  # we might need to re-use this value for next j
                i -= 1

        # print(f"{mins = }")
        mins_ids = [(idx, mn) for mn, idx in mins]
        mns = [mn for idx, mn in sorted(mins_ids)]

        maxs = []
        i = n - 1  # i is pointer on nums, j is pointer on q # scan nums from large to small
        for j in range(m - 1, -1, -1):  # scan queries from right to left (large to small)
            # print(f"{i = } {j = } {nums = } {q = } {maxs = }")
            local_max = math.inf
            while i >= 0 and nums[i] >= q[j][0]:
                local_max = min(local_max, nums[i])
                i -= 1
            maxs.append((local_max if local_max < math.inf else -1, q[j][1]))
            if i + 1 <= n - 1:
                i += 1

        # print(f"{maxs = }")
        maxs_ids = [(idx, mx) for mx, idx in maxs]
        mxs = [mx for idx, mx in sorted(maxs_ids)]
        return zip(mns, mxs)

"""
Binary Search
"""

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = []

        stack = []

        while root or stack:
            # go to left most leaf
            while root:
                stack.append(root)
                root = root.left
            # now process
            root = stack.pop()
            nums.append(root.val)
            # process right
            root = root.right

        nums = sorted(nums)
        n = len(nums)
        m = len(queries)
        # print(f"{nums = } {queries = }")
        ans = []
        for query in queries:
            idx = bisect.bisect_left(nums, query)
            # print(f"{query = } {idx = }")
            if 0 <= idx < n and nums[idx] == query:  # found value, so it is lower bound and upper bound
                ans.append([query, query])
            else:  # no matching value found
                pair = [-1, -1]
                if idx > 0:  # nums[idx-1] < query <= nums[idx], but no matching value here
                    pair[0] = nums[idx - 1]
                if idx < n:
                    pair[1] = nums[idx]
                ans.append(pair)

        return ans


def main():
    sol = Solution()
    assert sol.closestNodes(root = [6,2,13,1,4,9,15,None,None,None,None,None,None,14], queries = [2,5,16]) == [[2,2],[4,6],[15,-1]], 'fails'

    assert sol.closestNodes(root = [4,None,9], queries = [3]) == [[-1,4]], 'fails'

if __name__ == '__main__':
   main()