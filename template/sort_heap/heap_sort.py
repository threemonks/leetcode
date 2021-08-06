from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def min_heapify(nums, n, i):
            # min heapify array nums of size n, at root i
            # this assume both left and right subtree of i is already properly heapified
            l = 2 * i + 1  # left children
            r = 2 * i + 2  # right children

            # find largest among i, l, and r
            largest = i
            # if left child is larger than root
            if l < n and nums[l] < nums[largest]:
                largest = l

            # if right child is larger than root
            if r < n and nums[r] < nums[largest]:
                largest = r

            if largest != i:
                # swap largest and i
                nums[largest], nums[i] = nums[i], nums[largest]
                # and recursively heapify the affected subtree
                min_heapify(nums, n, largest)

        def heap_sort(nums):
            # sort nums using min_heap
            n = len(nums)

            # build min heap first, only need to start build from n//2 to 0
            for i in range(n // 2, -1, -1):
                min_heapify(nums, n, i)

            # one by one extract element from heap
            for i in range(n - 1, 0, -1):
                # move current root to end, which will be sorted and excluded from further heapify and sort
                nums[i], nums[0] = nums[0], nums[i]
                # now heapify reduced heap of size i=n-1
                min_heapify(nums, i, 0)

            # min_heap sorts in descending order
            return nums[::-1]

        return heap_sort(nums)