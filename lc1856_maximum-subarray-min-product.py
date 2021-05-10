"""
1856. Maximum Subarray Min-Product
Medium

67

1

Add to List

Share
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^7
"""
import math
from typing import List

"""
Monotonic increasing stack

因为subarray需要用最小值结算，假设栈顶元素是当前subarray的最小值，那怎么确定subarray左右边界？左边stack只有前一个元素更小，那边界就到这个更小值为止（不包括），右侧边界就是下一个检查的元素小于栈顶元素

       [3, 1, 5, 6, 4, 2]
presum [3  4  9  15 19 21 ]
[0(3)] => 3*(presum[0] - presum[stack[-2]] else 0)
[1(1)] => 1*(presum[1] - presum[stack[-2]] else 0)=4
[1(1), 2(5)]
[1(1), 2(5), 3(6)]
[1(1), 2(5), 3(6)] 4(4) => nums[3]*(presum[4-1]-presum[2]) = 36
[1(1), 2(5)] 4(4) => nums[2]*(presum[4-1]-presum[1]) = 5*11 = 55
[1(1), 4(4)]
[1(1), 4(4)] 5(2) =>nums[4]*(presum[5-1]-presum[1]) = 4*(19-4)= 60

monotonic increasing stack stores index of increasing subsequence

1. For each element nums[i] in array nums:
2. We use nums[i] as right boundary of subarray whose smallest value is st[-1]
    ans = max(ans, nums[st[-1]] * (presum[i-1], presum[st[-2]]))
3. subarray right boundary is i (exclusive), left bondary is st[-2],
4. How to build array which stores left boundary st[-2] which is the smaller value before st[-1]?
    Use stack st which keeps index of elements less than nums[i] so far
    if new number nums[i] less than or equal to st[-1], update answer and popout value at stack top st[-1]
    if new number nums[i] is smaller than st[-1] (whether it is after we popped larger numbers at stack end), we append nums[i] to stack

mistakes:
1.  using increasing stack as the previous smaller value determines the subarray boundary, so we need to know the previous smaller value index

"""


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n, MOD = len(nums), 10 ** 9 + 7
        presum = [0] * n
        cursum = 0
        for i in range(n):
            cursum += nums[i]
            presum[i] = cursum

        ans = -math.inf
        st = []
        for i in range(n):
            while st and nums[i] <= nums[st[-1]]:
                ans = max(ans, nums[st[-1]] * (presum[i - 1] - (presum[st[-2]] if len(st) >= 2 else 0)))
                st.pop()
            st.append(i)

        while st:  # process remaining items in stack
            ans = max(ans, nums[st[-1]] * (presum[n - 1] - (presum[st[-2]] if len(st) >= 2 else 0)))
            st.pop()

        return ans % MOD

def main():
    sol = Solution()

    assert sol.maxSumMinProduct(nums = [1,2,3,2]) == 14, 'fails'

    assert sol.maxSumMinProduct(nums = [2,3,3,1,2]) == 18, 'fails'

    assert sol.maxSumMinProduct(nums = [3,1,5,6,4,2]) == 60, 'fails'

if __name__ == '__main__':
   main()