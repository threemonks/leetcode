"""
count frequency of each unique values
for values in unique values from smallest to largest:
    append this value to output for the number of times we counted

Note:
    this is unstable, means same value in output might not preserve their original order in input

"""
import collections
from typing import List


def counting_sort(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    counter = collections.Counter(nums)
    counter = dict(counter)

    nummin, nummax = min(nums), max(nums)
    num = nummin
    i = 0
    while i < n and num <= nummax:
        while i < n and num in counter and counter[num] > 0:
            nums[i] = num
            i += 1
            counter[num] -= 1
        num += 1  # proceed to next unique value


def counting_sort_1(self, nums: List[int]) -> List:
    n = len(nums)
    counter = collections.Counter(nums)
    counter = dict(counter)

    nummin, nummax = min(nums), max(nums)
    num = nummin
    i = 0
    result = []
    while i < n and num <= nummax:
        while i < n and num in counter and counter[num] > 0:
            result.append(num)
            i += 1
            counter[num] -= 1
        num += 1  # proceed to next unique value

    return result