"""
992. Subarrays with K Different Integers
Hard

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.



Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""
import collections
from typing import List

"""
sliding window / two pointers (fast and slow pointers)
use sliding window / two pointers (fast and slow pointers) to solve for number of subarrays with at most K distinct numbers
Note
1) for each valid sliding window A[i:j], it adds j-1+1 valid new subarray to the result
2) K = 0 => 0 new subarray
then
    res = at_most_k(K) - at_most_k(K-1)
time O(N)
space O(N)
"""

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def at_most_k(K):
            if K == 0:
                return 0
            nonlocal A
            n = len(A)
            counts = collections.defaultdict(int)
            i = 0
            res = 0
            for j in range(n):
                counts[A[j]] += 1
                while i < j and len(counts) > K:
                    counts[A[i]] -= 1
                    if counts[A[i]] == 0:
                        counts.pop(A[i])
                    i += 1
                res += j - i + 1

            return res

        return at_most_k(K) - at_most_k(K - 1)


def main():
    sol = Solution()
    assert sol.subarraysWithKDistinct([1,2,1,2,3], 2) == 7, 'fails'

    assert sol.subarraysWithKDistinct([1,2,1,3,4], 3) == 3, 'fails'

if __name__ == '__main__':
   main()