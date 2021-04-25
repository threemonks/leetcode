"""
1838. Frequency of the Most Frequent Element
Medium

38

3

Add to List

Share
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.



Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105
"""
from typing import List

"""
Binary Search - in sorted nums, for left most j where with less than k ops, from nums[j] to nums[i] can all be changed to nums[i], thus obtaining max freq on nums[i]

since we are finding maximum possible freq, the order of the elements does not matter, so we can sort it, that will help us identify how to best use the k ops to increase max possible freq, by just increasing the ones immediatel proceeding numbers of the target number with highest freq. Trying to increase numbers earlier would be less optimal since they would require more ops for same freq increase.

Once we sort nums, for each number, we can do binary search to find the left most numbers we can also change to target num to get max freq.

Since for each num num[j] to change to nums[i], we need to use nums[i]-num[j] ops to achieve freq of nums[i], assume j is the left most element such that the total ops required between nums[j] to nums[i] be less than k, i.e.,

nums[i]-num[j] + nums[i]-nums[j+1] + ... + nums[i]-nums[i-1] <= k

this would give max freq of i-j+1 #(nums[i] itself does not need change)

Note that the above is 
(i-j)*nums[i] - sum(nums[j] ... nums[i-1]) <= k

this would be more efficient if we use prefix sum
presum[i] = nums[0]+nums[1]+...+nums[i]

then the above becomes
(i-j)*nums[i] - (presum[i-1]-presum[j-1]) <= k

双指针 单调性要求i增加时对应的j也增加
二分法 单调性要求i增加时所需要的值也单调增加

time O(Nlog(N))
"""


class Solution0:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        presum = [0] * (n + 1)  # dummy presum[0]
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]

        res = 1
        # iterate through nums,
        # for each nums[i], binary search to find its left most j where ops to make all nums[j] to nums[i] into nums[i] with less than k ops
        for i in range(1, n + 1):
            l, r = 1, i + 1
            while l < r:
                m = l + (r - l) // 2
                if (i - m) * nums[i - 1] - (
                        presum[i - 1] - presum[m - 1]) <= k:  # less than k ops, we can include more elements on left
                    r = m
                else:
                    l = m + 1
            res = max(res, i - l + 1)

        return res


"""
Sliding Window / Two Pointers / 双指针 滑动窗口

用指针i遍历排序后的数组nums，j是滑动窗口的左边界，在滑动窗口nums[j]...nums[i]内，保证 需要不多于k次操作可以将所有nums[j], nums[j+1], ..., nums[i-1]变成nums[i]

计算公式：

(i-j)*nums[i] - (presum[i-1]-presum[j-1]) < k

当i右移时，滑动窗口扩大，nums[i]变大，需要的操作次数增加，上述条件可能变得不满足，需要右移j，缩短窗口，使上述条件重新得到满足

time O(N)
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        presum = [0] * (n + 1)  # dummy presum[0]
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]

        j = 1
        res = 1
        for i in range(1, n + 1):
            while (i - j) * nums[i - 1] - (
                    presum[i - 1] - presum[j - 1]) > k:  # use nums[i-1] since we used dummy presum[0]
                j += 1
            # exit while when (i-j)*nums[i-1] - (presum[i-1]-presum[j-1]) <= k
            res = max(res, i - j + 1)

        return res

def main():
    sol = Solution()

    assert sol.maxFrequency(nums = [1,2,4], k = 5) == 3, 'fails'

    assert sol.maxFrequency(nums = [1,4,8,13], k = 5) == 2, 'fails'

    assert sol.maxFrequency(nums = [3,9,6], k = 2) == 1, 'fails'


if __name__ == '__main__':
   main()