"""
1696. Jump Game VI
Medium

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.



Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0


Constraints:

 1 <= nums.length, k <= 105
-104 <= nums[i] <= 104

"""
import collections
import math
from typing import List

"""
第二类序列型DP，定义 dp[i] := 跳转到第i个位置能得到的最大分数

状态转移方程

    dp[i] = max(dp[i-k], dp[i-k+1], dp[i-k+2], ..., dp[i-1])

这样时间复杂度是O(NK)。但N是10^5, k也是10^5,所以N*K是10^10，会超时(>10^9)，需要改进。

注意在dp[i-k]到dp[i-1]区间找最大值，而dp[i+1]是在dp[i-k+1]到dp[i]区间找最大值，两个区间大部分重叠，可以考虑用sliding window max 来优化寻找区间内最大值 。

我们关注当前滑动窗口，里面最大值用来更新窗口后面元素idx的dp值。

sliding window max标准解法是用dequeue，维护一个单调递减队列(monotonic decreasing deque)。如果有新元素比队尾元素更大，那他就更有竞争力（更新，更大）被用来更新后来的dp值。就舍弃队尾元素，直到新元素加入后保持队列单调递减。此外，如果队列首元素脱离了滑动窗口的范围，也需要舍弃。在每一循环，deque里面最大元素就是队首元素

sliding window max - use monotic decreasing deque

why do we use decreasing queue? because any element to be added is newer, and if it is also larger, than any element at end of queue can be discarded as they are older and smaller, will not contribute to future dp calculation.

time O(N)
space O(N)
"""


class Solution0:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        q = collections.deque()
        # dp存的是到当前位置的最佳score
        dp[0] = nums[0]
        q.append((0, dp[0]))

        for i in range(1, n):
            # 这个循环将queue最前端出了sliding window 的元素删除
            while q and q[0][0] + k < i:  # q[0] out of sliding window
                q.popleft()
            # print('after remove out of window q=%s' % (q))
            # q[0]里存的都是i的前k个元素里score最大的值的index，和对应的score值
            # 这里就可以得到dp[i]的值
            dp[i] = dp[q[0][0]] + nums[i]
            # 这个循环保证新加入的元素对应的dp 值比q里面其前面的值对应的score小，任何前面更小的score对应的index都会被踢出，然后才加入当前元素
            while q and dp[q[-1][0]] <= dp[i]:
                q.pop()
            q.append((i, dp[i]))
            # print('i=%s dp[%s]=%s q=%s' % (i, i, dp[i], q))

        return dp[n - 1]


"""
use one dp variable instead of array since we already store it into queue
time O(N)
space O(N)
"""


class Solution1:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        q = collections.deque()
        q.append((0, nums[0]))

        for i in range(1, n):
            while q and q[0][0] + k < i:  # q[0] out of sliding window
                q.popleft()
            # print('after remove out of window q=%s' % (q))
            dp = q[0][1] + nums[i]
            while q and q[-1][1] <= dp:
                q.pop()
            q.append((i, dp))
            # print('i=%s dp=%s q=%s' % (i, dp, q))

        return q[-1][1]


"""
DP

dp[i] := max score jump to index i, all init to -math.inf
base case:
dp[0] = nums[0]

then jump to index i+1
dp[i+1] = max (dp[i],
               dp[i-1],
               ...
               dp[i+1-k]
) + nums[i+1]

time O(NK) 10^10 TLE

mistakes:
1. dp[i] init to -math.inf
"""


class Solution0:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [-math.inf] * n
        dp[0] = nums[0]
        # print('dp[0]=%s' % dp[0])

        ans = -math.inf
        for i in range(1, n):
            for j in range(max(0, i - k), i):
                dp[i] = max(dp[i], dp[j] + nums[i])
                # print('i=%s j=%s dp[%s]=%s' % (i, j, i, dp[i]))

        # print(dp)
        return dp[n - 1]


"""
DP + Sliding window max (Mono Deque)

From above approach, we realized that dp[i] is determined by the max of dp[j] for j from i-k to i-1, so we can try to use a sliding window max monotonic decreasing deque to store dp value of window i-k to i-1, and we keep it monotonic decreasing, so it is O(1) time to get the max within window i-k to i-1.

steps:
1. for new element i, drop items from left of window if out of window size k, e.g., if dq[0] < i-k
2. dp[i] = dp[q[0]] + nums[i]
3. add dp[i] into dq while keep monotonic decreasing, i.e., any item in end of dq that is smaller than dp[i] should be popped before appending dp[i]

time O(Nlog(K))
"""
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [-math.inf] * n
        dp[0] = nums[0]
        # print('dp[0]=%s' % dp[0])
        dq = deque([0])
        for i in range(1, n):
            # drop items from left if sliding window size > k:
            while dq and dq[0] < i - k:
                dq.popleft()

            # update dp[i]
            dp[i] = dp[dq[0]] + nums[i]

            # append dp[i] into dq, while maintain monotonic decreasing, i.e., pop out any value from end of dq if dp[dq[-1]] < dp[i]
            while dq and dp[dq[-1]] < dp[i]:
                dq.pop()
            dq.append(i)

        return dp[n - 1]


"""
DP + Heap

From above approach, we realized that dp[i] is determined by the max of dp[j] for j from i-k to i-1, so we can try to store dp[i-k] to dp[i-1] into heap with its index, thus it takes O(log(K)) time to get max(dp[i-k...i-1]) to construct dp[i].

Note: we don't need to remove an item from heapq until we popped it out, then we check if it is outside i-k...i-1 window, if it does, drop it, and pop out another one from heapq.

time O(Nlog(N))
"""
import heapq


class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [-math.inf] * n
        dp[0] = nums[0]
        hq = [(-dp[0],
               0)]  # store dp value, and its index, we need to pop biggest dp value, so store -dp value, also need to keep track of index so we can expire it after we popped out and checked, if it is out of windows size k
        heapq.heapify(hq)

        for i in range(1, n):
            # drop items from left if sliding window size > k:
            while hq and hq[0][1] < i - k:
                heapq.heappop(hq)

            # update dp[i]
            dp[i] = -hq[0][0] + nums[i]

            # add new dp[i] into heapq
            heapq.heappush(hq, (-dp[i], i))

        return dp[n - 1]


def main():
    sol = Solution()
    assert sol.maxResult([1,-1,-2,4,-7,3], 2) == 7, 'fails'

    assert sol.maxResult([10,-5,-2,4,0,3], 3) == 17, 'fails'

    assert sol.maxResult([1,-5,-20,4,-1,3,-6,-3], 2) == 0, 'fails'


if __name__ == '__main__':
   main()