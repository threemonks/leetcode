"""
560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""
import collections
from typing import List

"""
https://leetcode.com/problems/subarray-sum-equals-k/discuss/102106/Java-Solution-PreSum-+-HashMap/416171
"""
""""
Solution 1 Brute force. We just need two loops (i, j) and test if SUM[i, j] = k
Time complexity O(n^2), Space complexity O(1)
TLE
"""


class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i] = presum[i - 1] + nums[i]
        # print(presum)
        res = 0
        for i in range(n):
            for j in range(i, n):
                # print('%s:%s %s-%s=%s' % (i, j, presum[j], presum[i-1], presum[j] - presum[i-1]))
                if presum[j] - (presum[i - 1] if i - 1 >= 0 else 0) == k:
                    # print('%s:%s' % (i, j))
                    res += 1

        return res


"""
HashMap / Array

From solution 1, we know the key to solve this problem is SUM[i, j]. So if we know SUM[0, i - 1] and SUM[0, j], then we can easily get SUM[i, j]. To achieve this, we just need to go through the array, calculate the current sum and save number of all seen PreSum to a HashMap. Time complexity O(n), Space complexity O(n).
优化第二层循环思路：
优化的思路是：我直接记录下有几个 sum[j] 和 sum[i] - k 相等，直接更新结果，就避免了内层的 for 循环。我们可以用哈希表，在记录前缀和的同时记录该前缀和出现的次数。
https://zhuanlan.zhihu.com/p/107778275
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = collections.defaultdict(int)
        presum = 0
        i = 0
        res = 0
        counts[0] = 1  # handle corner case when
        for j in range(n):
            presum += nums[j]
            res += counts[presum - k]
            counts[presum] += 1

        return res

def main():
    sol = Solution()
    assert sol.subarraySum([1,1,1], 2) == 2, 'fails'

    assert sol.nextGreaterElement([1,2,3], 3) == 2, 'fails'

    assert sol.nextGreaterElement([3, 4, 7, -2, 2, 1, 4, 2], 7) == 6, 'fails'

if __name__ == '__main__':
   main()