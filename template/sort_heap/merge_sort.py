from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums_left, nums_right):
            # merge two sorted lists
            result = []
            i, j = 0, 0
            while i < len(nums_left) and j < len(nums_right):
                if nums_left[i] <= nums_right[j]:
                    result.append(nums_left[i])
                    i += 1
                else:
                    result.append(nums_right[j])
                    j += 1
            # if there's remaining item in one of the lists
            while i < len(nums_left):
                result.append(nums_left[i])
                i += 1
            while j < len(nums_right):
                result.append(nums_right[j])
                j += 1

            return result

        def divide(nums, left, right):
            # divide nums[left:right+1] into two parts, recursively
            # and call merge to sort the two parts
            # base case: if single element, return
            if left >= right:
                return [nums[left]]
            mid = left + (right - left) // 2
            left_result = divide(nums, left, mid)
            right_result = divide(nums, mid + 1, right)
            return merge(left_result, right_result)

        return divide(nums, 0, len(nums) - 1)
