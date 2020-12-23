"""
96. Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Constraints:

1 <= n <= 19

"""
import math
from functools import lru_cache
from typing import List

"""
recursive with memoization
time O(n^2)
space O(n)
"""
from functools import lru_cache


class Solution0:
    def numTrees(self, n: int) -> int:

        @lru_cache(None)
        def helper(l, r):
            """
            how many unique BSTs covers range 1...n, and has r as root
            """
            nonlocal n
            # print('l=%s r=%s' % (l, r))
            if l >= r:  # base case, one node value or empty tree has only one valid BST structure
                return 1
            ans = 0
            # iterate root from l to r
            for i in range(l, r + 1):
                ans += helper(l, i - 1) * helper(i + 1, r)

            return ans

        return helper(0, n - 1)


"""
dp
dp[n] := number of unique BST tree structure given n unique numbers
To build BST, we need to first pick a root, let's say we pick number k as root, then all numbers 1... k-1 goes to left tree, and all numbers k+1 ... n goes to right tree. So number of unique left tree strucutre is dp[k-1], number of unique right tree structure is dp[n-k-1], and total number of tree structure is the product of these two counts

首先我们考虑根节点的选择。如果我们选择数字k作为根节点，那么左子树必然由节点 1,...,k-1 组成，左子树必然由节点 k+1,...,n 组成。接下来左右子树的构建就是一个递归问题。构建完左右子树之后，以k为根节点的BST的个数就是左子树个数乘以右子树个数（两两组合）。

我们可以用dp的解法。令dp[k]表示给定n个节点可以构成多少个BST。根据上面的思路，我们先loop作为根节点的数值，然后递归调用dp

dp[n] = 0;
for (int k=1; k<=n; k++)
  dp[n] += dp[k-1]*dp[n-1-k]; 
以上得到的序列h[0]=1, h[1]=1, h[2]=3, h[3]=5, ...就是著名的Catalan数。

Catalan数递归公式和通项公式：

h(n) =  h(n-1) * (4n-2)/(n+1)
h(n) =  C(2n,n) - C(2n, n-1),  其中C是组合数
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # empty tree
        dp[1] = 1  # with just one node, there's only one way to construct BST tree

        for i in range(2, n + 1):  # solve dp[0], dp[1] ... to dp[n]
            for k in range(1, i + 1):  # iterate pick root 1... i, sum all number of unique BST structures
                dp[i] += dp[k - 1] * dp[i - k]

        return dp[n]


def main():
    sol = Solution()
    assert sol.numTrees(3) == 5, 'fails'

if __name__ == '__main__':
   main()