"""
77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n

"""
from typing import List

"""
dfs
1. take first element from remaining nums, append to each element in partial subset (a path from tree root ([]) to current tree node) to get a new set of subsets
2. add this new set of subsets to result if length of subset is k
3. also use this as new partial subset into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)
visualization:
https://medium.com/@CalvinChankf/a-general-approach-for-subsets-combinations-and-permutations-5c8fe3aff0ae

"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, path):
            nonlocal res
            if len(path) == k:
                res.append(path)
            elif len(path) < k:
                for j in range(i, n + 1):
                    dfs(j + 1, path + [j])

        dfs(1, [])

        return res


"""
start with [[]], take one char from beginning of remaining available strings, append to each of the running result to form a new set of results to add to existing running result, if the resulting set has expected length
"""


class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        result = []

        def dfs(nums, path):
            if len(path) == k:
                result.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]])

        dfs(nums, [])

        return result

"""
Generation based on the mapping between binary bitmasks and the corresponding permutations / combinations / subsets
"""


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # generate bitmask from 0...00 to 1...1 (n bits)
        nums = list(range(1, n + 1))
        res = []
        for bitmask in range(1 << n):
            # only use combs with k-bit ones
            if bin(bitmask).count('1') == k:
                # generate the corresponding combination, j-th means use that number
                curr = [nums[j] for j in range(n) if bitmask & (1 << (j))]
                res.append(curr)

        return res

def main():
    sol = Solution()
    assert sol.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], 'fails'

    assert sol.combine(1, 1) == [[1]], 'fails'

if __name__ == '__main__':
   main()