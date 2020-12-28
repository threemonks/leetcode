"""
862. Shortest Subarray with Sum at Least K
Hard

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.



Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""
import collections
from typing import List
"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/189039/Detailed-intuition-behind-Deque-solution
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary

Key observation:

If we accumulate array A to obtain B, then B[l] <= B[r] - K indicates sum(A[l:r]) >= K. Given B[r], the problem is equivalent to finding the nearest previous element B[l] such that B[l] <= B[r] - K.

We maintain a increasing queue here because, given a new B[i], the larger element on the left are inferior than B[i] as a candidate to make some future element B[j] >= B[i] + K (j > i).

One extra optimization learnt from @lee215 is that we can also pop up the element on the left side <= B[i] - K of the increasing queue because, given current element B[i], if a future element B[j] > B[i], then B[j] - K would be within the queue after the removal of such elements <= B[i] - K; Otherwise, if a future element B[j] > B[i] then it never appears in the final results.

The deque:
The deque stores the possible values of the start pointer in increasing order. Unlike the sliding window, values of the start variable will not necessarily be contiguous.

Why is it increasing :
from @lee215 If B[i] <= B[d.back()] and moreover we already know that i > d.back(), it means that compared with d.back(),
B[i] can help us make the subarray length shorter and sum bigger. So no need to keep d.back() in our deque.

from @Sarmon So that when we move the start pointer and we violate the condition, we are sure we will violate it if we keep taking the other values from the Deque. In other words, if the sum of the subarray from start=first value in the deque to end is smaller than target, then the sum of the subarray from start=second value in the deque to end is necessarily smaller than target.
So because the Deque is increasing (B[d[0]] <= B[d[1]]), we have B[i] - B[d[0]] >= B[i] - B[d[1]], which means the sum of the subarray starting from d[0] is greater than the sum of the sub array starting from d[1].

Why do we have a prefix array and not just the initial array like in sliding window :
Because in the sliding window when we move start (typically when we increment it) we can just substract nums[start-1] from the current sum and we get the sum of the new subarray. Here the value of the start is jumping and one way to compute the sum of the current subarray in a constant time is to have the prefix array.

Why using Deque and not simply an array :
We can use an array, however we will find ourselves doing only three operations:
1- remove_front : when we satisfy our condition and we want to move the start pointer
2- append_back : for any index that may be a future start pointer
3- remove_back : When we are no longer satisfying the increasing order of the array
Deque enables doing these 3 operations in a constant time.

Complexity:
Every index will be pushed exactly once.
Every index will be popped at most once.

Time O(N)
Space O(N)

"""
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        elif len(A) == 1:
            return 1 if A[0] >= K else -1

        res = []
        n = len(A)
        B = [0] * n # presum
        B[0] = A[0]
        for i in range(1, n):
            B[i] = B[i-1] + A[i]
        B = [0] + B # add sentinel value 0
        # print('B=%s' % B)
        res = n+1
        q = collections.deque() # store index of possible start value of subarray in increasing order
        for i in range(n+1):
            # pop all elements j from end of q where B[q[j]] > B[i]
            # to keep deque increasing
            while len(q) and B[q[-1]] >= B[i]:
                q.pop()
            # pop out all elements j from front of deque where B[i] - B[q[j]] >= K, since all previous elements also met A[i]-A[q[j]]>=K, but has smaller index, therefore the resulting subarray between those element and j will be longer
            while len(q) and B[i]-B[q[0]]>=K:
                res = min(res, i-q.popleft())
            q.append(i)
            # print('i=%s q=%s res=%s' % (i, q, res))

        return res if res <= n else -1

def main():
    sol = Solution()
    assert sol.shortestSubarray([1], 1) == 1, 'fails'

    assert sol.shortestSubarray([1,2], 4) == -1, 'fails'

    assert sol.shortestSubarray([2,-1,2], 3) == 3, 'fails'


if __name__ == '__main__':
   main()