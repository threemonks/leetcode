"""
1130. Minimum Cost Tree From Leaf Values
Medium

Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.



Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4


Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).

"""
import math
from functools import lru_cache
from typing import List

"""
idea

We are asked to build an optimal binary tree, with all its leaves in-order traverse represented by array arr, but we don't know which leaf node belong to left subtree and which leaf node goes to right subtree.
Since the given leaf nodes are in-order traverse, there will be a pivot point where all left side of it goes to left subtree, all right of it goes to right subtree. For each subtree, if we know the minimum sum, we can use it to build the parent tree.
So the original problem can be broken down into subproblems via the pivot point. Then we have the following transition function, where res(i, j) repreents minimum non-leaf nodes sum with leaf nodes represented by arr[i,j]

for k = i ... j:
    res(i,j) = min(res(i,k) + res(k+1,j) + max(arr[i:k])*max(arr[k+1:j]))

"""

"""
DP topdown with caching

time O(N^3) - cache stack with two indicies, l, r, plus within the helper function, we have k loop from l to r
space O(N^2) - cache stack with two indcies, l, r
"""
class Solution0:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        @lru_cache(None)
        def helper(l, r):
            nonlocal arr
            if l >= r:
                return 0
            res = math.inf
            for k in range(l, r):
                res = min(res, helper(l, k) + helper(k + 1, r) + max(arr[l:k + 1]) * max(arr[k + 1:r + 1]))

            return res

        return helper(0, len(arr) - 1)


"""
DP (brutal force)

intution:

We are asked to build an optimal binary tree, with all its leaves in-order traverse represented by array arr, but we don't know which leaf node belong to left subtree and which leaf node goes to right subtree.
Since the given leaf nodes are in-order traverse, there will be a pivot point where all left side of it goes to left subtree, all right of it goes to right subtree. For each subtree, if we know the minimum sum, we can use it to build the parent tree.
So the original problem can be broken down into subproblems via the pivot point. Then we have the following transition function, where res(i, j) repreents minimum non-leaf nodes sum with leaf nodes represented by arr[i,j]

for k = i ... j:
    res(i,j) = min(res(i,k) + res(k+1,j) + max(arr[i:k])*max(arr[k+1:j]))

time O(N^3)
space O(N^2)
"""
class Solution1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[math.inf for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for l in range(2, n+1): # length from 2 to n
            for i in range(n+1-l): # starting index i, from 0 to maximum allowed by length l
                j = i+l-1 # ending index j
                dp[i][j] = math.inf
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+max(arr[i:k+1])*max(arr[k+1:j+1]))

        return dp[0][n-1]

"""
Greedy

https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/951938/Don't-overthink-about-trees.-It's-a-DPGreedy-problem.
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/349098/From-O(N2)-to-O(n).-Greedy

Intution
1. Since given array is the inorder traversal of tree leaves. Their order won't change. You can only decide which 2 consecutive nodes you wanna combine to make a new node by their product.
2. Each time we cacluate a value for a non-leaf node, we discard the smaller leave and keep the large leave, because the smaller leave will be "shadowed" by the large leave forever. To minimize the cost, we want to save the large leaves to the last, and use the small leaves first.
3. So at each step, we pick the least product of two neighboring nodes a[i]*a[i+1], add the sum to result, and drop the smaller of the two
4. and repeat 3
5. until there's only one number left in the array

O(N^2)

"""

class Solution2:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        nums = arr[:]
        while len(nums) > 1:
            i = nums.index(min(nums))
            res += min(nums[i-1:i] + nums[i+1:i+2])*nums.pop(i)

        return res

"""
Monotonic decreasing stack

steps:
1. At each step, if a smaller value comes up, push into stack
2. if a larger value comes up, we use the smallest value at top of stack (stack[-1]) to calculate a product between that number and its two neighbors (stack[-1] and nums[i]), add this product to result, then pop the smallest value at top of stack, 
3. if after poping stack[-1], new stack top stack[-1] is still smaller than this new value nums[i], repeat above process until we can put this large value into stack.
4. the process ends until there's only value left.

Why decreasing stack - Because we use small leaf once and discard them, large leaf stays.

O(N)
"""
import math
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        stack = [math.inf] # add sentinel value
        for a in arr:
            while stack[-1] <= a:
                b = stack.pop()
                res += b * min(a, stack[-1])
                # print('a=%s stack=%s res=%s' % (a, stack, res))
            stack.append(a)

        # print('stack=%s' % stack)
        while len(stack) > 2: #finish processing any numbers in stack until there's only one left # one sentinel value
            res += stack.pop() * stack[-1]


        return res



def main():
    sol = Solution()
    assert sol.mctFromLeafValues([6,2,4]) == 32, 'fails'

if __name__ == '__main__':
   main()