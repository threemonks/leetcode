"""
287. Find the Duplicate Number
Medium

7223

764

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1


Constraints:

2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
"""
from typing import List

"""
Hash Map / Set

Proof of must exist one duplicate:

pigeonhole principal:
if there's more pigeon than holes, then at least one pigeon hole must have at least two pigeons. So n+1 numbers, n distinct possible numbers, there must be at least one duplicate

time O(N)
space O(N)
"""


class Solution0:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)


"""
Two Pointers

use f(x) = nums[x], then nums with dup becomes a linked list with a cycle, and the ask is to find the entrance of the cycle

use two pointers (fast and slow)

1. phase 1, fast moves 2 steps each time, slow moves 1 step each time
2. phase 2, when the two pointers meet, move slow back to beginning, and change fast pointer to move at one step each time
   when they meet again, the meeting point is the entrance of cycle (and duplicate in nums)

"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]

        # phase 1
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # now both fast and slow are at their first intersection
        # we restart slow at beginning of nums[0], and change fast to move one step each from its current position
        slow = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return fast

def main():
    sol = Solution()
    assert sol.findDuplicate(nums = [1,3,4,2,2]) == 2, 'fails'

    assert sol.findDuplicate(nums = [3,1,3,4,2]) == 3, 'fails'

    assert sol.findDuplicate(nums = [1,1]) == 1, 'fails'

    assert sol.findDuplicate(nums = [1,1, 2]) == 1, 'fails'

if __name__ == '__main__':
   main()