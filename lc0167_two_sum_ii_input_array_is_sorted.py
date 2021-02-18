"""
167. Two Sum II - Input array is sorted
Easy

Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in increasing order.
-1000 <= target <= 1000
Only one valid answer exists.

"""
from typing import List

"""
hashmap

time O(N)
space O(N)
"""


class Solution0:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        index_map = dict()
        for i, num in enumerate(numbers):
            t = target - num
            if t in index_map:
                return sorted([i + 1, index_map[t] + 1])
            index_map[num] = i


"""
sorted => two pointers

time O(N)
space O(1)
"""


class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l, r = 0, n - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1


"""
sorted => binary search target-num

time O(Nlog(N))
space O(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i, num in enumerate(numbers):
            t = target - num
            # binary search to find t in numbers
            l, r = 0, n
            while l < r:
                m = l + (r - l) // 2
                if numbers[m] == t and i != m:
                    return sorted([i + 1, m + 1])
                elif numbers[m] < t:
                    l = m + 1
                else:  # numbers[m] > t
                    r = m

def main():

    sol = Solution()

    assert sol.twoSum(numbers = [2,7,11,15], target = 9) == [1,2], 'fails'

    assert sol.twoSum(numbers = [2,3,4], target = 6) == [1,3], 'fails'

    assert sol.twoSum(numbers = [-1,0], target = -1) == [1,2], 'fails'

if __name__ == '__main__':
   main()