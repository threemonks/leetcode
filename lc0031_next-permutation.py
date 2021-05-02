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

步骤
1. 从右边开始找到第一个不符合递增的数字nums[i]，from right end, first nums[i]<nums[i+1]
   如果找不到，则整个数组是降序，没有next permutation，直接整个数组反序
2. 从右边开始找到大于nums[i]但是尽可能小的数字nums[j]，就是从右边第一个大于nums[i]的数字，因为该段子数组是从右往左递增
3. 交换这两个数字，swap nums[i] and nums[j]
4. 把i+1到数组右端后缀子数组反序, reverse nums[i+1:]

how to understand it:
step-1: find the first digit (pivot) that can be swapped to make permutation bigger (pivot element before longest non-increasing suffix)
step-2: find the digit bigger but closest to nums[k] (right most successor)
step-3: swap(nums[k], nums[l])
step-4: sort the subarray nums[k+1:end], why we can just reverse instead of sort?
        because we know nums[k+1:end] must be non-increasing, reason:
        1. at step 1, we know nums[k+1:end] is non-decreasing
        2. before swap in step 3, we know nums[l-1] >= nums[l] > nums[k] >= nums[l+1]
        3. so after swap, we still have nums[l-1] > nums[k] >= nums[l+1], so we can reverse it

example:
2,3,6,5,4,1 
1. find last number nums[i]=3 that can be swapped to make larger (first non-ascending from right most to left)
   if cannot find, the entire array is descending, no next, just reverse the whole thing
2. find first number nums[j] from right that is larger then nums[i]=3 but as small as possible: 4, first one that's larger than 4 from right, since that part is increasing while going to left
3. swap nums[i]=3 and nums[j]=4
4. reverse nums[i+1:] (need to sort it asecnding, but since it was ascending from right, or descending, but after swap, it is still descending)
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return

        def swap(i, j):
            nonlocal nums
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        def reverse(l, r):
            # reverse subarray between l and r
            nonlocal nums
            i, j = l, r
            while i < j:
                swap(i, j)
                i += 1
                j -= 1

        # 1 . find first decreasing nums[i] from right such that nums[i] < nums[i+1]
        i = n-2
        while i>=0 and nums[i+1] <= nums[i]:
            i -= 1

        # print('i=%s' % i)
        # if i is -1, the entire array is ascending, no next, just reverse entire array
        if i < 0 and nums[0] > nums[1]:
            reverse(0, n-1)
            return

        if i >= 0:
            # 2. from right, find first nums[j] that is larger than nums[i], but as small as possible, i.e., first number that's larger than nums[i] from right
            j = n-1
            while j>=0 and nums[j] <= nums[i]:
                j -= 1

            # 3. swap nums[i] and nums[k]
            swap(i, j)

        # 4. reverse nums[i+1:]
        reverse(i+1, n-1)


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