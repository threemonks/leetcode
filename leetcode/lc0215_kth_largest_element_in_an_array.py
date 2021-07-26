"""
215. Kth Largest Element in an Array
Medium

https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List

"""
QuickSelection using partition algorithm used in quicksort / Divide and Conquer

time O(N)

mistakes:
1. in quick sort partition, when define start/end pointer, we leave pivot index/value outside of the pointer movement
2. if both left pointer value and right pointer value are on wrong side of pivot value, we swap them, then move both pointers towards middle
3. pivot_pos > len(nums)-k => pivot_pos is too far to right, so we need to check pivot_pos within left part
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        return self.helper(nums, 0, n - 1, k)

    def helper(self, nums, left, right, k):
        if left >= right:  # only one item left?
            print('nums=%s left=%s right=%s' % (nums, left, right))
            return nums[len(nums) - k]
        pivot_pos = self.partition(nums, left, right)
        if pivot_pos == len(nums) - k:  # found k-th largest
            return nums[pivot_pos]
        elif pivot_pos > len(nums) - k:  # too few items to right, k-th largest is in left part
            return self.helper(nums, left, pivot_pos - 1, k)
        else:  # too few items to left, k-th largest is in right part
            return self.helper(nums, pivot_pos + 1, right, k)

    def partition(self, nums, left, right):
        pivot_val = nums[right]
        start, end = left, right - 1
        while start <= end:
            if nums[start] <= pivot_val:
                start += 1
            elif nums[end] > pivot_val:
                end -= 1
            else:  # if both nums[start] and nums[end] are on wrong side of pivot_val, lets swap them
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # done looping, now put pivot_val to its correct position
        nums[start], nums[right] = nums[right], nums[start]

        return start


"""
Using Heap and Heapsort

time Nlog(k)
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

def main():
    sol = Solution()
    assert sol.findKthLargest([3,2,1,5,6,4], k = 2) == 5, 'fails'

    assert sol.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4) == 4, 'fails'


if __name__ == '__main__':
   main()