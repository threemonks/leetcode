"""
1793. Maximum Score of a Good Subarray
Hard

"""
import math
from typing import List

"""
Two Pointers / Greedy

calculate min value of nums[i] from k to 1 as leftmin, and min value of nums[j] from k to n as rightmin
then use two pointers to calculate score[i][j] as min(leftmin[i], rightmin[j]) * (j-i+1)
at each step, we move the pointer that would give largest value at next step (greedy), since the one step will result length increase by 1 for either pointer move, so we want move the one that would result in larger value after move

       [1,4,3,7,4,5] k = 3
              K
leftmin 1 3 3 7
rightmin      7 4  4
time O(N)
space O(N)
"""

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        leftmin = [-1 for _ in range(n)]
        rightmin = [-1 for _ in range(n)]

        mn = math.inf
        for i in range(k, -1, -1):
            mn = min(mn, nums[i])
            leftmin[i] = mn

        mx = math.inf
        for j in range(k, n):
            mx = min(mx, nums[j])
            rightmin[j] = mx

        # print('leftmin=%s' % leftmin)
        # print('rightmin=%s' % rightmin)

        i, j = k, k
        score = -math.inf
        while i >= 0 and j < n:
            score = max(score, min(leftmin[i], rightmin[j])*(j-i+1))
            # if (nums[i-1] if i-1>=0 else 0) > (nums[j+1] if j+1<n else 0):
            if min((leftmin[i-1] if i-1>=0 else 0), rightmin[j])*(j-(i-1)+1) > min(leftmin[i], (rightmin[j+1] if j+1<n else 0))*((j+1)-i+1):
                # be greedy at each step
                # if decrease i gives larger result in next step, we decrease i
                i -= 1
            else:
                j += 1

        return score


def main():
    sol = Solution()
    assert sol.maximumScore(nums = [1,4,3,7,4,5], k = 3) == 15, 'fails'

    assert sol.maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0) == 20, 'fails'

if __name__ == '__main__':
   main()