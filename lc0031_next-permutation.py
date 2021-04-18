"""
31. Next Permutation
Medium

5336

1832

Add to List

Share
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""
from typing import List

"""
Next Permutation (lexcigological order)

1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index , just reverse
2. Find the largest index l > k such that nums[k] < nums[l]
3. Swap nums[k] and nums[l]
4. Reverse the sub-array nums[k + 1:]

how to understand it:
step-1: easy, find the first digit that can be swapped to make permutation bigger (pivot element before longest non-increasing suffix)
step-2: easy, find the digit bigger but closest to nums[k]
step-3: swap(nums[k], nums[l])
step-4: sort the subarray nums[k+1:end], why we can just reverse instead of sort?
        because we know nums[k+1:end] must be non-increasing, reason:
        1. at step 1, we know nums[k+1:end] is non-decreasing
        2. before swap in step 3, we know nums[l-1] >= nums[l] > nums[k] >= nums[l+1]
        3. so after swap, we still have nums[l-1] > nums[k] >= nums[l+1], so we can reverse it

example:
2,3,6,5,4,1 
1. find last number nums[i]=3 that can be swapped to make larger (first non-ascending from right most to left)
   if cannot find, the entire array is ascending, no next, just reverse the whole thing
2. find first number nums[j] from right that is larger then nums[i]=3 but as small as possible: 4
3. swap nums[i]=3 and nums[j]=4
4. reverse nums[i+1:] (need to sort it asecnding, but since it was ascending from right, or descending, but after swap, it is still descending)
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def reverse(l, r):
            # reverse nums[l...r]
            nonlocal nums
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # find last number that is smaller than it's following number
        idx1 = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx1 = i
                break
        # print('idx1=%s' % idx1)
        if idx1 == -1:
            reverse(0, n - 1)
            return

        # find smallest number to right of idx1 that is larger than nums[idx1]
        idx2 = -1
        for j in range(n - 1, idx1, -1):
            if nums[j] > nums[idx1] and (idx2 == -1 or nums[j] < nums[idx2]):
                idx2 = j

        # swap idx1 and idx2
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

        # reverse nums[idx1+1:]
        reverse(idx1 + 1, n - 1)


def main():
    sol = Solution()
    nums = [1,3,2]
    sol.nextPermutation(nums)
    assert nums == [2, 1, 3]

    nums = [1,2,3]
    sol.nextPermutation(nums)
    assert nums == [1, 3, 2]

    nums = [3,2,1]
    sol.nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [1,1,5]
    sol.nextPermutation(nums)
    assert nums == [1, 5, 1]

    nums = [1]
    sol.nextPermutation(nums)
    assert nums == [1]

if __name__ == '__main__':
   main()