"""
1004. Max Consecutive Ones III
Medium

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1

"""

from typing import List

"""
use two pointers, when left pointer fixes, move right pointer to right and keep track of number of zeros (j-(i-1) - (presum[j]-presum[i-1])) <= K

time O(N*K)
TLE
"""


class Solution0:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        presum = [0] * n
        for i in range(n):
            presum[i] = presum[i - 1] + A[i]
        # print(presum)
        res = 0
        for i in range(n):
            j = i
            # print('i=%s' % i)
            while j < n and j - (i - 1) - (presum[j] - (presum[i - 1] if i - 1 >= 0 else 0)) <= K:
                res = max(res, j - i + 1)
                # print('i=%s j=%s j-(i-1) - (presum[j]-(presum[i-1] if i-1>=0 else 0))=%s res=%s' % (i, j, j-(i-1) - (presum[j]-(presum[i-1] if i-1>=0 else 0)), res))
                j += 1
        return res


"""
dp[i][k] maximum length of array at i-th element and done k'th flip 0 to 1

if A[i] == 1, then no need to flip 0 to 1, dp[i][k] = dp[i-1][k]+1
if A[i] == 0, then we need to flip 0 to 1 for i-th, dp[i][k] = dp[i-1][k-1]+1


time O(N*K)
TLE
"""


class Solution1:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [[0] * K for _ in range(n)]

        # initial
        for i in range(n):
            if A[i] == 1:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = 0

        for k in range(K):
            if A[0] == 1:
                dp[0][k] = 1
            else:
                dp[0][k] = 0

        for i in range(n):
            for k in range(K):
                if A[i]:
                    dp[i][k] = dp[i - 1][k] + 1
                else:
                    dp[i][k] = dp[i - 1][k - 1] + 1

        return max([dp[i][K - 1] for i in range(n)])


"""

subarray问题，通常用双指针，固定(遍历)左边界，探索右边界。假设固定左边界是i，要右边界j最远，但保证区间[i,j]内最多有K个0(K次反转)。右边界j应该停在0上，因为1不需要翻转，subarray总可以包括右边的1而不影响使用的翻转次数。

此时考虑左边界遍历到i+1,如果A[i+1]是1，那此时[i+1,j]内需要翻转的次数还是K，没有变化，所以右边界j不能往右边增加。我们只能不断右移左边界i，直到A[i]==0的时候，这样A[i]不需要翻转，[i+1,j]区间内翻转次数减少一次，count-=1。这样右边界j又可以继续向右移动，直到下一个A[j]==0（此时count = K）。

time O(N)

"""


class Solution2:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)

        res = 0
        count = 0
        j = 0
        for i in range(n):
            while j < n and (count < K or (A[j] == 1 and count <= K)):
                if A[j] == 0:
                    count += 1
                # print('i=%s j=%s count=%s j-i+1=%s' % (i, j, count, j-i+1))
                j += 1
            # now count == K and A[j] == 0
            # assert (count<=K and (j >= n or A[j]==0)), 'logic incorrect'
            res = max(res, j - i)
            if A[i] == 0:
                count -= 1
                # print('i=%s j=%s count=%s j-i+1=%s' % (i, j, count, j-i+1))

        return res


"""
双指针，固定(遍历)右边界，探索左边界
X X [i X X X X j]
X X [i X X X X X 0] count += 1
 while count > K: # 探索左边界
     if A[i] == 0:
        count -=1
     i+=1
 """

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)

        res = 0
        count = 0
        i = 0
        for j in range(n):
            if A[j] == 0:
                count += 1
            while i <= j and count > K:
                if A[i] == 0:
                    count -= 1
                i += 1
            # now i > j or count <=K
            assert (i > j or count <= K), 'logic incorrect'
            # print('i=%s j=%s count=%s j-i+1=%s' % (i, j, count, j-i+1))
            res = max(res, j - i + 1)

        return res


"""
双指针，固定(遍历)右边界，探索左边界
左边界探索优化（因为寻找最大窗口，不需要缩小窗口，所以在右边界是遍历（每次移动1）的情况下，左边界其实只在需要的时候（K<0）往右移动1

因为求最大的窗口，所以窗口变小是没有意义的
1）窗口增大： left不变，right右移，即right++
什么时候增大？窗口内的0数量没有达到上限K
2）窗口不变：left跟着right右移，即left++, right++
什么时候不变？窗口内的0数量达到了上限K
"""


class Solution4:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        i = 0
        for j in range(n):
            if A[j] == 0:
                K -= 1
            if K < 0:
                if A[i] == 0:
                    K += 1
                i += 1

        return j - i + 1

def main():
    sol = Solution()
    assert sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6, 'fails'

    assert sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10, 'fails'

if __name__ == '__main__':
   main()