"""
823. Binary Trees With Factors
Medium

"""
from typing import List

"""
DP

observation
1. individual elements are valid binary tree
2. let dp[i] := number of trees with i as root, then total number of such combinations are 
    dp[j] * dp[k] such that i,j,k all in arr, and i=j*k

Note:
  (1) use HashMap dp to record  number of trees with the int a as root
  (2) each integer A[i] will always have one tree with only itself
  (3) if A[i] has divisor (a) in the map, and if A[i]/a also in the map
     * then we can have a new tree with A[i] being root, 
     * a can be the root of its left subtree, and A[i]/a can be the root of its right subtree;
     * the number of such tree is map.get(a) * map.get(A[i]/a)
  (4) total number of trees are sum over all map values
"""


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        n = len(arr)
        MOD = 10 ** 9 + 7

        dp = dict()

        for idx, a in enumerate(arr):
            dp[a] = (sum([dp.get(a // b, 0) * dp[b] for b in arr[:idx] if b in dp and a % b == 0]) + 1) % MOD
            # print('idx=%s dp[a]=%s' % (idx, dp[a]))

        return sum(dp.values()) % MOD

def main():
    sol = Solution()
    assert sol.numFactoredBinaryTrees(arr = [2,4]) == 3, 'fails'

    assert sol.numFactoredBinaryTrees(arr = [2,4,5,10]) == 7, 'fails'

if __name__ == '__main__':
   main()