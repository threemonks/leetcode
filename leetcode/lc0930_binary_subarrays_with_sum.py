"""

930. Binary Subarrays With Sum
Medium

In an array A of 0s and 1s, how many non-empty subarrays have sum S?



Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.

"""

from typing import List

"""
Hashmap + prefix_sum

遍历每个元素A[j]，考察所有以A[j]结尾，满足条件和为S的子数组，有哪些可能起点i，计算可能起点i的个数

涉及数组subarray的和，转化为前缀和来处理，sum[i:j]=pre_sum[j]-pre_sum[i-1]，其中sum[i:j]=S，对于某个元素A[j]，pre_sum[j]已知，则以A[j]结尾，和为S的子数组个数，就是前缀和为pre_sum[j]-S=pre_sum[i-1]的i的个数，即

result += counts_dct[pre_sum[j]-S]


"""

import collections
class Solution0:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        counts_dct = collections.defaultdict(int) # number of subarray with sum to S, after check up to index j
        result = 0
        counts_dct[0] = 1
        pre_sum = [0]*len(A)
        for j in range(n):
            pre_sum[j] = (pre_sum[j-1] if j-1>=0 else 0) + A[j]
            result += counts_dct[pre_sum[j]-S]
            counts_dct[pre_sum[j]]+=1

        return result

"""
simplify pre_sum from 1d to 0d as we only use one previous value
"""
import collections
class Solution1:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        counts_dct = collections.defaultdict(int) # number of subarray with sum to S, after check up to index j
        result = 0
        counts_dct[0] = 1
        pre_sum = 0
        for j in range(n):
            pre_sum = pre_sum + A[j]
            result += counts_dct[pre_sum-S]
            counts_dct[pre_sum]+=1

        return result


"""
keep a sliding window with sum <= S
use sliding window to find number of subarrays whose sum is <= S
than the answer is sum_less_than_k(S) - sum_less_than_k(S-1)
to find number of subarrays whose sum is at most S, we use prefix sum

"""


class Solution2:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        def at_most(k):
            nonlocal A
            n = len(A)
            res = 0
            i = 0
            for j in range(n):  # loop right end index
                k -= A[j]
                while i <= j and k < 0:
                    k += A[i]
                    i += 1
                res += j - i + 1
                # print('i=%s j=%s k=%s' % (i, j, k))
            return res

        return at_most(S) - at_most(S - 1)


"""
keep as long as possible sliding window with sum < S
each time when right index j moves right once, if nums[j] + sums  < S, then we got j-i+1 more subarrays whose sum < S

"""

class Solution3:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        def sum_less_than_k(k):
            nonlocal A
            n = len(A)
            res = 0
            sums = 0
            j = 0
            for i in range(n):  # loop left end index
                if j < i:
                    j = i
                    sums = 0
                while j < n and sums + A[j] < k:  # end right index as far right as possible but keep sum S < k
                    sums += A[j]
                    j += 1
                res += j - i  # now sums+A[j] >= k, and sums+A[j-1]<k, so we added j-i, not j-i+1 subarrays
                sums -= A[i]
                # print('i=%s j=%s sums=%s res=%s' % (i, j, sums, res))
            return res

        return sum_less_than_k(S + 1) - sum_less_than_k(S)


"""
Hash Table / prefix sum

to find window of size goal, we can use prefix sum, so that window of size goal = presum[i]-presum[j] == goal

for each presum[i], see how many times we have seen presum[i]-goal, we use hash table to keep track of count of reach presum occurances

"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        counts = collections.defaultdict(int)
        presum = 0
        ans = 0
        for i in range(n):
            presum = presum + nums[i]
            if presum == goal:  # window starting at index 0, or we can init counts[0]=1 to include window starts at index 0
                ans += 1
            ans += counts[presum - goal]  # window starts at presum value presum-goal
            counts[presum] += 1

        return ans



def main():
    sol = Solution()
    assert sol.numSubarraysWithSum([1,0,1,0,1], 2) == 4, 'fails'

if __name__ == '__main__':
   main()