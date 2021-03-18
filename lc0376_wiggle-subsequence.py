"""
376. Wiggle Subsequence
Medium
"""
from typing import List

"""
DP

dp0[i] := length longest wiggle subsequence ending at i with i, with last ascending
dp1[i] .... last descending

dp1[i] = max(dp0[j]+1 if nums[i] < nums[j] for j from 0...i-1)
dp0[i] = max(dp1[j]+1 if nums[i] > nums[j] for j from 0...i-1)

base case:
dp0[0] = 1
dp1[0] = 1

time O(N^2)
space O(N)

mistakes:
1. n <= 1: return 1
2. both dp0[i] and dp1[i] should have default value 1, since any single char is a valid wiggle sequence

"""


class Solution0:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        dp0 = [1 for _ in range(n)]
        dp1 = [1 for _ in range(n)]

        dp0[0], dp1[0] = 1, 1

        for i in range(1, n):
            for j in range(0, i):
                dp1[i] = max(dp1[i], dp0[j] + 1 if nums[i] < nums[j] else 0)
                dp0[i] = max(dp0[i], dp1[j] + 1 if nums[i] > nums[j] else 0)
                # print('i=%s j=%s dp0=%s dp1=%s' % (i, j, dp0, dp1))

        return max(dp0[-1], dp1[-1])


"""
DP

observation:
any element could either go up (nums[i] > nums[i-1]), down (nums[i] < nums[i-1]), or flat (nums[i]==nums[i-1])
so we can have dp derived in one pass

up[i] := wiggle sequence ending at i with last element going up
down[i] := wiggle sequence ending at i with last element going down

if nums[i] > nums[i-1]:
    up[i] = down[i-1]+1 # add i
    down[i] = down[i-1] # skip i
elif nums[i] < nums[i-1]:
    down[i] = up[i-1]+1 # add i
    up[i] = up[i-1] # skip i
elif nums[i] == nums[i-1]:
    up[i] = up[i-1] # have to skip i since no change
    down[i] = down[i-1]

time O(N)
space O(N) - could further reduce to O(1) by using one var dp0 dp1 instead of array
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1 for _ in range(n)]
        down = [1 for _ in range(n)]

        up[0], down[0] = 1, 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            elif nums[i] == nums[i - 1]:
                up[i] = up[i - 1]  # have to skip i since no change
                down[i] = down[i - 1]

        return max(up[-1], down[-1])


def main():
    sol = Solution()
    assert sol.wiggleMaxLength(nums = [1,7,4,9,2,5]) == 6, 'fails'

    assert sol.wiggleMaxLength(nums = [1,17,5,10,13,15,10,5,16,8]) == 7, 'fails'

    assert sol.wiggleMaxLength(nums = [1,2,3,4,5,6,7,8,9]) == 2, 'fails'

if __name__ == '__main__':
   main()