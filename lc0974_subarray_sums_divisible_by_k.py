"""
974. Subarray Sums Divisible by K
Medium

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.



Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

"""
from typing import List

"""
precaculate prefix sum to simplify calculating sum of current subarray
TLE
"""

class Solution0:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)

        cur_sum = 0
        ans = 0
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += A[j]
                if cur_sum % K == 0:
                    ans += 1
                # print('i=%s j=%s cur_sum=%s ans=%s' % (i, j, cur_sum, ans))

        return ans


"""
Array HashMap / Prefix-Sum
obsevation:
1. sum of subarray sum[A[i:j+1]] = presum[j] - presum[i-1] where presum[i] is prefix sum from index 0 to i
2. sum of subarray divisible by K, is equivalent to presum[i-1] divided by K has same remainder as presum[j] i.e., (presum[j] - presum[i-1]) % K == 0
   <=> presum[j]%K==0 and presum[i-1]%K==0
3. we could use hashmap to store how many times a given presum%K={0,1,2,3,4, .., K} pattern appeared, and when it appear again, we then got a valid subarray between this two index, plus all previous know counts of such modulo, i.e., if a modulo has appeared 3 times, and now it appears 4-th time, this will add 4 more valid subarrays
4. we could use array to store the counts a given modulo has appeared
"""


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)

        presum = 0
        counts = [0] * K
        counts[0] = 1  # 0 % K = 0, and empty subarray is valid subarray divisible by K
        ans = 0
        for i in range(n):
            presum += A[i]
            modulo = presum % K
            ans += counts[modulo]
            counts[modulo] += 1
            # print('i=%s presum=%s modulo=%s counts=%s ans=%s' % (i, presum, modulo, str(counts), ans))

        return ans

def main():
    sol = Solution()
    assert sol.subarraysDivByK([4,5,0,-2,-3,1]) == 7, 'fails'

if __name__ == '__main__':
   main()