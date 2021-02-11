"""
40. Combination Sum II
Medium

2452

85

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

from typing import List

"""
sort input array candidates, pick one number from front of remaining numbers, append to each of current running result, to form set of new results, if we find same number, we can skip to avoid duplicate, if the result set has desired sum (tracked by target==0), then add to answer result set.

time O(2^N)
space O(N)
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)

        results = []

        def backtrack(path, start, target):
            nonlocal candidates
            if target == 0:
                if tuple(path) not in results:
                    results.append(tuple(path))
            elif target < 0 or (len(path) and target < path[
                -1]):  # all remaining numbers are larger than target, no need to proceed
                return
            else:
                for i in range(start, n):
                    if i > start and candidates[i] == candidates[i - 1]:  # skip to avoid duplicate
                        continue
                    backtrack(path + [candidates[i]], i + 1, target - candidates[i])

        backtrack([], 0, target)

        return [list(r) for r in results]


def main():
    sol = Solution()
    assert sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8) == [ [1,1,6], [1,2,5], [1,7], [2,6] ], 'fails'

    assert sol.combinationSum2(candidates = [2,5,2,1,2], target = 5) == [ [1,2,2], [5] ], 'fails'

if __name__ == '__main__':
   main()