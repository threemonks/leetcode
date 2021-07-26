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

time O(2^N) - total number of subsets of n elements is 2^N
space O(N)
"""


class Solution0:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)

        result = []

        self.backtrack(candidates, [], 0, target, result)

        return result

    def backtrack(self, candidates, path, idx, target, result):
        n = len(candidates)
        if target == 0:
            result.append(tuple(path))
        elif target < 0 or idx == n:
            return
        else:
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:  # skip to avoid duplicate
                    continue
                self.backtrack(candidates, path + [candidates[i]], i + 1, target - candidates[i], result)


"""
keep a running result, for next distinct element in available remaining elements (skip duplicate), 
choose or not choose this element to append to current running result, to get a new result.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)

        result = []

        self.backtrack(candidates, [], 0, target, result)

        return result

    def backtrack(self, candidates, path, idx, target, result):
        if target == 0:
            result.append(path)
            return
        elif target < 0 or idx == len(candidates):
            return
        else:
            self.backtrack(candidates, path + [candidates[idx]], idx + 1, target - candidates[idx], result)
            # skip duplicate elements
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            self.backtrack(candidates, path, idx + 1, target, result)


def main():
    sol = Solution()
    assert sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8) == [ [1,1,6], [1,2,5], [1,7], [2,6] ], 'fails'

    assert sol.combinationSum2(candidates = [2,5,2,1,2], target = 5) == [ [1,2,2], [5] ], 'fails'

if __name__ == '__main__':
   main()