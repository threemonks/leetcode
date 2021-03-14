"""
1793. Maximum Score of a Good Subarray
Hard

"""
import math
from typing import List

"""
Two Pointers / Greedy

calculate min value of nums[i] from k to 1 as left, and min value of nums[j] from k to n as right
then use two pointers to calculate score[i][j] as min(left, right) * (j-i+1)
at each step, we move the pointer that would give largest value at next step, since the one step will result length increase by 1 for either pointer move, so we want move the one that would result in larger value after move

time O(N)
space O(N)
"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [0 for _ in range(k + 1)]
        right = [0 for _ in range(n)]  # only use k...n part

        mn = math.inf
        for i in range(k, -1, -1):  # from middle to front
            left[i] = min(mn, nums[i])
            mn = left[i]
        # print(left)

        mn = math.inf
        for j in range(k, n):  # from middle to front
            right[j] = min(mn, nums[j])
            mn = right[j]
        # print(right)

        i, j = k, k
        score = -math.inf
        while i >= 0 and j < n:
            # print('i=%s j=%s' % (i, j))
            score = max(score, min(left[i], right[j]) * (j - i + 1))
            # if left[i] < right[j], use left[i] to calculate score, and move i to left
            if (left[i - 1] if i - 1 >= 0 else 0) < (right[j + 1] if j + 1 < n else 0):
                # print('use right[%s]=%s score=%s' % (j, right[j], score))
                j += 1
            else:
                # print('use left[%s]=%s score=%s' % (i, left[i], score))
                i -= 1

        return score


def main():
    sol = Solution()
    assert sol.maximumScore(nums = [1,4,3,7,4,5], k = 3) == 15, 'fails'

    assert sol.maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0) == 20, 'fails'

if __name__ == '__main__':
   main()