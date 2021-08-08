"""
1964. Find the Longest Valid Obstacle Course at Each Position
Hard

3

0

Add to List

Share
You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

You choose any number of obstacles between 0 and i inclusive.
You must include the ith obstacle in the course.
You must put the chosen obstacles in the same order as they appear in obstacles.
Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.



Example 1:

Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,3,2], [1,2,2] has length 3.
Example 2:

Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [2], [2] has length 1.
- i = 1: [2,2], [2,2] has length 2.
- i = 2: [2,2,1], [1] has length 1.
Example 3:

Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [3], [3] has length 1.
- i = 1: [3,1], [1] has length 1.
- i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
- i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,1,5,6,4,2], [1,2] has length 2.


Constraints:

n == obstacles.length
1 <= n <= 10^5
1 <= obstacles[i] <= 10^7

"""
from typing import List

"""
Greedy + monotonic increasing stack + Binary Search
similar to Longest increasing subsequence

keep a mono increasing stack of longest increasing subsequence, 
when a new element is larger than stack[-1], append it
if new element is smaller than stack[-1], binary search to find the smallest number x that is >= new number, replace it with the new number
and output for this num is the number of elements in stack up to and include this inserted index

time O(nlogn)
"""
class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = []
        for num in nums:
            # binary search to find smallest number stack[i] >= num, then replace it with num
            left, right = 0, len(stack)
            while left < right:
                mid = left + (right-left)//2
                # print('left=%s right=%s mid=%s num=%s stack[mid]=%s stack=%s' % (left, right, mid, num, stack[mid], stack))
                if stack[mid] <= num:
                    left = mid + 1
                elif stack[mid] > num:
                    right = mid

            # when binary serach done, stack[left] should be smallest number >= num
            ans.append(left+1) # longest increasing subsequence length corresponding to num is left+1
            if left == len(stack): # needs to append at end
                stack.append(num)
            else: # can replace directly
                stack[left] = num

        return ans

def main():
    sol = Solution()

    assert sol.longestObstacleCourseAtEachPosition(nums = [1,2,3,2]) == [1,2,3,3], 'fails'

    assert sol.longestObstacleCourseAtEachPosition(nums = [2,2,1]) == [1,2,1], 'fails'

    assert sol.longestObstacleCourseAtEachPosition(nums = [3,1,5,6,4,2]) == [1,1,2,3,2,2], 'fails'

if __name__ == '__main__':
   main()