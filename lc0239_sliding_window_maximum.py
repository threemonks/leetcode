"""
239. Sliding Window Maximum
Hard

4834

204

Add to List

Share
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
import collections
from typing import List

"""
use monotonic queue (deque) to keep track of elements within sliding window, but keep only decreasing elements so that the leftmost (first) element is always the largest, and obtain O(1) add and removal, for each new element, we remove elements that is outside of sliding window, and remove all elements in deque that is smaller than current new element, and append first element (largest) to output (after we have visited at least k-1 element)

sliding window max notes:
1. sliding window max stores array index in the deque
2. when new element pops larger older element from the end of deque, it is compared by value (nums[i]<nums[q[-1]])
3. when old (front of queue) element goes out of focus gets kicked out, it is compared using index (q[0]+k<i)
4. after we kicked out smaller element from end of queue, we then add the new item
   q.append(nums[i])
5. we pops out element from front of queue when it is too old (out of window size k) for next i (iteration increases i)

Note:
  each element is processed exactly twice (added, and removed) so total time is O(N)
time O(N)
space O(k)
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        q = collections.deque()  # store index of numbers we are still interested in, basically items within the sliding window, and larger than current
        res = []
        max_idx = 0  # keep track of max num within sliding window
        for i in range(0, n):
            # clean up the deque (remove items not in the sliding window,
            if q and q[0] == i - k:
                q.popleft()
            # and remove items that is smaller than current item nums[i]
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
            if i >= k - 1:
                res.append(nums[q[0]])
            # print('i=%s q=%s nq=%s max_idx=%s res=%s' % (i, str(q), str([nums[i] for i in q]), max_idx, res))

        return res


"""
use a mononotic decreasing stack (list) instead of deque to hold interested elements in sliding window - much slower
time O(N*k) # list.pop() is not O(1)
"""

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        q = []  # store index of numbers we are still interested in, basically items within the sliding window, and larger than current
        res = []
        max_idx = 0  # keep track of max num within sliding window
        for i in range(0, n):
            # clean up the deque (remove items not in the sliding window,
            if q and q[0] == i - k:
                q.pop(0)
            # and remove items that is smaller than current item nums[i]
            while q and nums[i] > nums[q[-1]]:
                q.pop(-1)
            q.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
            if i >= k - 1:
                res.append(nums[q[0]])
            # print('i=%s q=%s nq=%s max_idx=%s res=%s' % (i, str(q), str([nums[i] for i in q]), max_idx, res))

        return res

def main():
    sol = Solution()
    assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7], 'fails'

    assert sol.maxSlidingWindow([1], 1) == [1], 'fails'

    assert sol.maxSlidingWindow([1,-1], 1) == [1,-1], 'fails'

    assert sol.maxSlidingWindow([9,11], 2) == [11], 'fails'

    assert sol.maxSlidingWindow([4,-2], 2) == [4], 'fails'

if __name__ == '__main__':
   main()