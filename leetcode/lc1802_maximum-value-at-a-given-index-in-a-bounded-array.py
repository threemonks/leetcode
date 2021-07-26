"""
1802. Maximum Value at a Given Index in a Bounded Array
Medium

274

44

Add to List

Share
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.



Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3


Constraints:

1 <= n <= maxSum <= 10^9
0 <= index < n
"""
"""
Binary Search

Obseration:
To maximize nums[index], it should be the max value in the array, and each element to its left and right will be nums[index]-1, etc, from nums[index] to nums[0] is arithmetic  sequence with diff -1, from nums[index] to nums[n-1] is also arithmetic  sequence with diff -1, with both end must be at least 1 (nums[i] positive)

We can use binary search to try and find maximum nums[index] between 1 and maxSum

if we subtract n from maxSum, i.e., replace maxSum with maxSum-n, then we simplified to a sum of array with non-negative element, with elements abs diff <=1, and try to maximize value at index index, with total sum <= maxSum-n. This will make the calculation of sum of the array under given condition easier.

time O(log(N))
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        target = maxSum - n

        def sums(x):
            # sum x, x-1, ..., 1, 0
            return x * (x + 1) // 2  # 等差数列求和。此处必须用//

        def check(m):
            # nums[i] = m
            # left end is max(0, m-i)
            # right end is  max(0, m-((n-1)-i))
            total = m  # count value at index m only once
            if m - index >= 0:
                total += sums(m - 1) - sums(m - index - 1)  # 求和从m-index 到 m-1
            else:
                total += sums(m - 1)
            if index + m >= n:
                total += sums(m - 1) - sums(m - (n - 1 - index) - 1)  # 求和从m-(n-1-index) 到 m-1
            else:
                total += sums(m - 1)

            return total <= target

        lo, hi = 0, target
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo + 1


"""
solution from comment

https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1119666/Python-or-Binary-Search
"""


class Solution1:
    def partial(self, x):
        return x * (x + 1) // 2

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(num):
            r = n - index - 1  # number of elements on the right
            l = index  # number of elements on the left
            count = num
            if num <= l + 1:
                count += self.partial(num - 1) + l - num + 1
            else:
                count += self.partial(num - 1) - self.partial(num - l - 1)

            if num <= r + 1:
                count += self.partial(num - 1) + r - num + 1
            else:
                count += self.partial(num - 1) - self.partial(num - r - 1)

            return count <= maxSum

        left, right = 1, maxSum
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        if check(left):
            return left

        return left - 1


"""
lee215 solution
"""


class Solution2:
    def maxValue(self, n, index, maxSum):
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1

def main():
    sol = Solution()
    assert sol.maxValue(n = 4, index = 2,  maxSum = 6) == 2, 'fails'

    assert sol.maxValue(n = 6, index = 1,  maxSum = 10) == 3, 'fails'


if __name__ == '__main__':
   main()