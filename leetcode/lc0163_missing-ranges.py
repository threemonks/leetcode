"""
163. Missing Ranges
Easy

588

2200

Add to List

Share
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
Example 2:

Input: nums = [], lower = 1, upper = 1
Output: ["1"]
Explanation: The only missing range is [1,1], which becomes "1".
Example 3:

Input: nums = [], lower = -3, upper = -1
Output: ["-3->-1"]
Explanation: The only missing range is [-3,-1], which becomes "-3->-1".
Example 4:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
Example 5:

Input: nums = [-1], lower = -2, upper = -1
Output: ["-2"]


Constraints:

-109 <= lower <= upper <= 10^9
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.
"""
from typing import List

"""
Array

note:
1. special case nums=[], or lower<nums[0] or upper > nums[-1]
2. check if nums[i]==nums[i-1]+1, if not, that's a missing range.
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower < upper:
                return ["%s->%s" % (lower, upper)]
            elif lower == upper:
                return ["%s" % lower]

        n = len(nums)
        ans = []
        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])

        for i, num in enumerate(nums):
            if i <= 0:
                continue
            # if nums[i] - nums[i-1] > 1, these are missing ranges
            if nums[i] - nums[i - 1] > 1:
                ans.append([nums[i - 1] + 1, nums[i] - 1])

        if upper > nums[-1]:
            ans.append([nums[-1] + 1, upper])

        return [str(a[0]) if a[0] == a[1] else "%s->%s" % (a[0], a[1]) for a in ans]

def main():

    sol = Solution()

    assert sol.findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99) == ["2","4->49","51->74","76->99"], 'fails'

    assert sol.findMissingRanges(nums = [], lower = 1, upper = 1) == ["1"], 'fails'

    assert sol.findMissingRanges(nums = [], lower = -3, upper = -1) == ["-3->-1"], 'fails'

    assert sol.findMissingRanges(nums = [-1], lower = -1, upper = -1) == [], 'fails'

    assert sol.findMissingRanges(nums = [-1], lower = -2, upper = -1) == ["-2"], 'fails'

if __name__ == '__main__':
   main()
