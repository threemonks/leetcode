"""
137. Single Number II
Medium

3027

421

Add to List

Share
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""
from typing import List

"""
Bit Manipulation

for each bit index i=0...31, count and sum non-zero for each element, if we got sums non-zero bits in a given index i, if sum%3==1, set this bit (i) for ans: ans |= (counts%s<<i)

Finally, we need to deal with overflow cases in python: maximum value for int32 is 2^31 - 1, so if we get number more than this value we have negative answer in fact.

time O(32*N)
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i):
                    count += 1
            ans |= (count % 3) << i

        # handle overflow of 32bit in python
        if ans >= (1 << 31):
            return ans - (1 << 32)
        else:
            return ans

def main():
    sol = Solution()
    assert sol.singleNumber(nums = [2,2,3,2]) == 3, 'fails'

    assert sol.singleNumber(nums = [0,1,0,1,0,1,99]) == 99, 'fails'

if __name__ == '__main__':
   main()