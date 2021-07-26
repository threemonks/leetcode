"""
1423. Maximum Points You Can Obtain from Cards
Medium

1581

70

Add to List

Share
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1.
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202


Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""
import math
from typing import List

"""
Sliding window

10^5 means DP will TLE

so instead of take total of k stones from each side, we can take n-k stones from anywhere, try to minimize the sum of n-k stones in the window

mistakes:
1. window [j, i+1] size k=i+1-j => i-j=k-1
"""


class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k1 = n - k

        total = sum(nums)

        minwsum = math.inf
        wsum = 0
        j = 0
        for i in range(n):
            wsum += nums[i]
            while i - j >= k1:
                wsum -= nums[j]
                j += 1

            if i - j == k1 - 1:
                minwsum = min(minwsum, wsum)

        return total - minwsum


def main():
    sol = Solution()

    assert sol.maxScore(nums = [1,2,3,4,5,6,1], k = 3) == 12, 'fails'

    assert sol.maxScore(nums = [2,2,2], k = 2) == 4, 'fails'

    assert sol.maxScore(nums = [9,7,7,9,7,7,9], k = 7) == 55, 'fails'

    assert sol.maxScore(nums = [1,1000,1], k = 1) == 1, 'fails'

    assert sol.maxScore(nums = [1,79,80,1,1,1,200,1], k = 3) == 202, 'fails'

if __name__ == '__main__':
   main()