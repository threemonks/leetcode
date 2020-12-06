"""
321. Create Maximum Number
Hard

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]

"""
from functools import lru_cache
from typing import List

"""
intuition
to get maximum number from nums1 and nums2, we would need to get maximum number from nums1, and nums2 separately, then merge them
to remove k digits in total, we would be removing k1 digits from nums1, and k2 from nums2, with k1+k2 = k
so steps are:
    1 loop k1 from 0 to k, and k2 = k-k1, get maximum number from nums1 by removing k1 digits, and also get maximum number from nums2 by removing k2 digits
    2. merge these two maximum number to get a max number
    3. get max number from result of looping k1

"""


class Solution1:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        def get_single_max_number(nums, k):
            """
            get a single max number by keeping k digits from nums

            """
            stack = []
            pop_count = 0
            for i in range(len(nums)):
                while stack and nums[i] > stack[-1] and pop_count < len(nums) - k:
                    stack.pop()
                    pop_count += 1
                stack.append(nums[i])

            return stack[:k]

        def merge_nums(nums1, nums2):
            """
            merge nums1 and nums2 to get maximum number
            """
            m = len(nums1)
            n = len(nums2)
            i = 0
            j = 0
            res = []
            while i < m or j < n:
                if i < m and j < n:
                    if nums1[i:] > nums2[j:]:
                        res.append(nums1[i])
                        # print(res)
                        i += 1
                    else:
                        res.append(nums2[j])
                        # print(res)
                        j += 1
                elif i < m and j >= n:
                    res.append(nums1[i])
                    # print(res)
                    i += 1
                elif i >= m and j < n:
                    res.append(nums2[j])
                    # print(res)
                    j += 1

            return res

        # for k1 from 0 to k-1
        # remove k1 digits from nums1 to get largest number1,
        # remove k-k1 digits from nums2 to get largest number2
        # then merge number1 and number2 to get max number
        max_num = []
        for k1 in range(k + 1):
            k2 = k - k1
            number1 = get_single_max_number(nums1, k1)
            number2 = get_single_max_number(nums2, k2)
            # print('k1=%s k2=%s number1=%s number2=%s' % (k1, k2, number1, number2))
            number = merge_nums(number1, number2)
            if len(number) < k:
                continue
            max_num = max(max_num, number)

        return max_num


"""
dp 双序列

nums1 XXXXXX i
nums2 YYYYYYYYY j

dp[i][j][k]: (string)
  => dp[i-1][j][k-1] + nums1[i]
     dp[i][j-1][k-1] + nums2[j]
     dp[i-1][j-1][k] don't use either nums1[i] or nums2[j]

"""

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], K: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        nums1 = [0] + nums1
        nums2 = [0] + nums2
        dp = [[['' for _ in range(K+1)] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = ''
        for i in range(1, m + 1):
            for k in range(1, min(i+1, K+1)):
                dp[i][0][k] = max(dp[i - 1][0][k-1] + str(nums1[i]),
                                  dp[i - 1][0][k])

        for j in range(1, n + 1):
            for k in range(1, min(j+1, K+1)):
                dp[0][j][k] = max(dp[0][j - 1][k-1] + str(nums2[j]),
                                  dp[0][j - 1][k])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, min(i + j + 1, K+1)):
                    dp[i][j][k] = max(dp[i - 1][j][k - 1] + str(nums1[i]),
                                      dp[i][j - 1][k - 1] + str(nums2[j]),
                                      dp[i - 1][j - 1][k])

        return [int(s) for s in dp[m][n][K]]

def main():
    sol = Solution()
    assert sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5) == [9, 8, 6, 5, 3], 'fails'

    assert sol.maxNumber([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4], 'fails'

    assert sol.maxNumber([3, 9], [8, 9], 3) == [9, 8, 9], 'fails'

if __name__ == '__main__':
   main()