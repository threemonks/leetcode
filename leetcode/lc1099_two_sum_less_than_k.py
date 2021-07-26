"""
1099. Two Sum Less Than K
Easy

https://leetcode.com/problems/two-sum-less-than-k/

"""
import math
from typing import List

"""
brutal force
"""
class Solution0:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        diff = math.inf
        best_sums = math.inf
        for i in range(n-1):
            for j in range(i+1, n):
                sums = nums[i]+nums[j]
                if sums < k and k-sums < diff:
                    diff = k - sums
                    best_sums = sums
                elif sums >= k:
                    break

        return best_sums if best_sums is not math.inf else -1

"""
Two Pointers
"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        answer = -1
        left, right = 0, n-1
        while left < right:
            sums = nums[left]+nums[right]
            if sums < k:
                answer = max(answer, sums)
                left += 1
            else:
                right -= 1

        return answer



def main():
    sol = Solution()
    assert sol.twoSumLessThanK(nums = [34,23,1,24,75,33,54,8], k = 60) == 58, 'fails'

    assert sol.twoSumLessThanK(nums = [10,20,30], k = 15) == -1, 'fails'


if __name__ == '__main__':
   main()