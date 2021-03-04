"""
503. Next Greater Element II
Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

"""
from typing import List

"""
Stack
observation
1. to get next greater number from circular array (i.e., item before this index), loop through index 0 through 2*n, and use index % length as index instead of index to access value
2. using stack to hold all numbers whose next greater number hasn't been identified yet, pop out stack top when next value is greater than stack top value 

time O(n^2)
space O(n)
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)

        stack = [(0, nums[0])]  # stack stores (index, the value) tuple
        nums_ng = [-1] * n
        for i in range(1, 2 * n):
            while stack and stack[-1][1] < nums[i % n]:
                node = stack.pop(-1)
                nums_ng[node[0]] = nums[i % n]
            if i < n:
                stack.append((i % n, nums[i % n]))

        return nums_ng


def main():
    sol = Solution()
    assert sol.nextGreaterElements([1,2,1]) == [2, -1, 2], 'fails'

if __name__ == '__main__':
   main()