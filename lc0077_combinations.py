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
backtrack/dfs
"""


class Solution0:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, k, path, res):
            """
            take first element from remaining nums, append to each element in partial combination (a path from tree root ([]) to current tree node) to get a new set of partial combinations, add this to result if length is k, and also use this as new partial combination into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)

            nums: remaining nums to explore/process
            k: number of elements in a result combination
            path: partial combintations (a path from tree root ([]) to current tree node) constructed so far after visiting leading parts of original array nums
            res: the result combinations created so far
            """
            if len(path) == k:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:], k, path + [nums[i]], res)

        nums = list(range(1, n + 1))
        res = []
        dfs(nums, k, [], res)
        print('res')

        return res


"""
Generation based on the mapping between binary bitmasks and the corresponding permutations / combinations / subsets
"""


class Solution:
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