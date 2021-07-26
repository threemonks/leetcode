"""
179. Largest Number
Medium

3031

316

Add to List

Share
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 10^9
"""
from typing import List

"""
Sort

observation
"34" > "3" > "30"

so compare using customized comparator x, y: x+y>y+x (string contact)

mistakes:
1. need to strip leading 0, unless the number itself is 0
"""
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        def cmp(x, y):
            # compare two string using string concatenation
            if x+y > y+x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        return "".join(sorted(nums, key=cmp_to_key(cmp), reverse=True)).lstrip('0') or '0'

def main():
    sol = Solution()

    assert sol.largestNumber(nums = [10,2]) == "210", 'fails'

    assert sol.largestNumber(nums = [3,30,34,5,9]) == "9534330", 'fails'

    assert sol.largestNumber(nums = [1]) == "1", 'fails'

    assert sol.largestNumber(nums = [10]) == "10", 'fails'

if __name__ == '__main__':
   main()