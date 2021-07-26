"""
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

"""
from typing import List

"""
DFS tree traversal, and traverse all elements in order, at each node, only consider elements at or after current elements, not before, as considering elements before would cause duplicate

backtrack(remain, comb, start)
i) base case remain == 0, we have one result to add to final ist
ii) another base case, remain < 0, we exceed target value, stop exploration of this path
iii) otherwise, we explore sublists of candidates as i in [start ... n], for each candiate, we invoke recursive function itself with updated parameters
    *) add current candidate to the combination (path)
    *) with added candidate, remain targe to fulfill is less, remain-candidates[i]
    *) for next exploration, start from current cursor i
    *) at end of each exploration, we backtrack by removing candiate from combination (path)

time complexity (N^(T/M + 1)) - T is target value, M is minimum value among candidates, so the length of result comb set is bounded by T/M, this is also the maximum number of nodes of a N-ary tree of height T/M, which is N^(T/M + 1)
space O(T/M) - number of recusrive calls is T/M
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, path, start):
            if remain == 0:
                results.append(list(path))
                return
            elif remain < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(remain - candidates[i], path + [candidates[i]], i)

        backtrack(target, [], 0)

        return results


def main():
    sol = Solution()
    assert sol.combinationSum(candidates = [2,3,6,7], target = 7) == [[2,2,3],[7]], 'fails'

    assert sol.combinationSum(candidates = [2,3,5], target = 8) == [[2,2,2,2],[2,3,3],[3,5]], 'fails'

    assert sol.combinationSum(candidates = [2], target = 1) == [], 'fails'

    assert sol.combinationSum(candidates = [1], target = 1) == [[1]], 'fails'

    assert sol.combinationSum(candidates = [1], target = 2) == [[1,1]], 'fails'

if __name__ == '__main__':
   main()