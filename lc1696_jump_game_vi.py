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


class Solution:
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
dp with heap to get max (store -dp in heap as heap is min heap, and we need to get max dp value at top)
    dp[i] = max(dp[i-k], dp[i-k+1], ..., dp[i-1])
time O(NK)
space O(N)
"""
import heapq


class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        q = [(-dp[0], 0)]
        heapq.heapify(q)

        for i in range(1, n):
            while q and q[0][1] + k < i:  # q[0] out of sliding window
                heapq.heappop(q)
            # print('after remove out of window q=%s' % (q))
            # -q[0][0] is max(dp[i-k], dp[i-k+1], ..., dp[i-1])
            dp[i] = -q[0][0] + nums[i]
            heapq.heappush(q, (-dp[i], i))
            # print('i=%s dp=%s q=%s' % (i, dp, q))

        return dp[n - 1]

def main():
    sol = Solution()
    assert sol.maxResult([1,-1,-2,4,-7,3], 2) == 7, 'fails'

    assert sol.maxResult([10,-5,-2,4,0,3], 3) == 17, 'fails'

    assert sol.maxResult([1,-5,-20,4,-1,3,-6,-3], 2) == 0, 'fails'


if __name__ == '__main__':
   main()