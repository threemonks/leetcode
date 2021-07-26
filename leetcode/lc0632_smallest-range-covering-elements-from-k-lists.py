"""
632. Smallest Range Covering Elements from K Lists
Hard

1479

26

Add to List

Share
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
Example 3:

Input: nums = [[10,10],[11,11]]
Output: [10,11]
Example 4:

Input: nums = [[10],[11]]
Output: [10,11]
Example 5:

Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]


Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-10^5 <= nums[i][j] <= 10^5
nums[i] is sorted in non-decreasing order.

"""
import math
from collections import defaultdict
from typing import List
from sortedcontainers import SortedList
import heapq


"""
Sliding Window

flat nums into list of n*k array of tuple, each tuple has original value and original array index

use sliding window to find minimum window size that at least one value from each original array in nums

time (Nlog(N)) N=k*n=3500*50 = 1.5*10^

"""

class Solution0:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        arr = SortedList()  # sorted list of tuple (val, original arr index in nums)

        k, n = len(nums), len(nums[0])
        for i in range(k):
            for j in range(len(nums[i])):
                arr.add((nums[i][j], i))

        # print(arr)
        counts = defaultdict(int)  # counts of elements in each of original array in nums

        ans = None
        j = 0
        for i in range(len(arr)):
            # add number arr[i]
            counts[arr[i][1]] += 1
            # print('i=%s counts=%s' % (i, counts))
            while len(counts) >= k:
                if not ans or arr[i][0] - arr[j][0] < ans[-1] - ans[0]:  # update valid answer
                    ans = [arr[j][0], arr[i][0]]
                counts[arr[j][1]] -= 1  # drop j from left end of sliding window
                if counts[arr[j][1]] == 0:  # remove key when value drops to 0
                    counts.pop(arr[j][1])
                j += 1

        return ans


"""
PriorityQueue (Heap)

Use a priorityqueue to store one element from each array in nums, along with the group it come from. Always pop the smallest one, and replace it with another one from the same group as soon as you pop one out, to maintain that heap has one element from each group

Each time the smallest item in the heap is replaced with a larger one from the same group, the right boundary of answer would be the max of (the original right of answer,  this newly inserted larger one from group i), update ans if this range is smaller.

[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

[0,1], [4,0], [5, 2] => range [0,5]
pop [0, 1], then add [9,1] heap becomes
[4,0],[5,2],[9,1] => range [4, max(9, 5)], ignore
pop [4,0], then add [10,0] heap becomes
[5,2][9,1],[10,0] => range[5, max(10,9)], ignore
pop [5,2], then add [18,2], heap becomes
[9,1],[10,0],[18,2] => range[9, max(18, 10)], ignore
pop [9,1], then add [12,1], heap becomes
[10, 0], [12,1], [18,2] => range[10, max(18, 12)], ignore

time: O(k*nlog(k)) k is heap size, k=len(nums), n is average length of nums[i]
"""

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        pq = []
        right = -math.inf
        for i in range(k):
            row = nums[i]
            right = max(right, row[0])
            heapq.heappush(pq, [row[0], i, 0])

        ans = (-math.inf, math.inf)
        while pq:
            if right - pq[0][0] < ans[1] - ans[0]:  # update if better range found
                ans = pq[0][0], right
            # pop smallest, and replace with next element in the same group
            left, i, j = heapq.heappop(pq)
            if j + 1 == len(nums[i]):  # no more value from this group, terminate
                return ans
            v = nums[i][j + 1]
            right = max(right, v)

            # add this new/larger value into heap
            heapq.heappush(pq, [v, i, j + 1])


def main():
    sol = Solution()
    assert sol.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]) == [20, 24], 'fails'

    assert sol.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]]) == [1, 1], 'fails'

    assert sol.smallestRange(nums = [[10,10],[11,11]]) == [10, 11], 'fails'

    assert sol.smallestRange(nums = [[10],[11]]) == [10, 11], 'fails'

    assert sol.smallestRange(nums = [[1],[2],[3],[4],[5],[6],[7]]) == [1, 7], 'fails'

if __name__ == '__main__':
   main()