"""
1395. Count Number of Teams
Medium

1218

133

Add to List

Share
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
All the integers in rating are unique.

"""
from typing import List

"""
Array

for each element, count # of higher to left high_left, and # of lower to right low_right, multiple these two numbers gives the number of teams (decreasing) centered at this element
similarly, count # of lower to left low_left, and # of higher to right high_right, multiple these two numbers gives the number of teams (ascending) centered at this element

"""


class Solution0:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        ans = 0
        for i in range(1, n - 1):
            v = rating[i]
            left_high, right_low = 0, 0
            left_low, right_high = 0, 0
            for j in range(0, i):
                u = rating[j]
                if u > v:
                    left_high += 1
                elif u < v:
                    left_low += 1
            for j in range(i + 1, n):
                u = rating[j]
                if v < u:
                    right_high += 1
                elif v > u:
                    right_low += 1

            ans += left_high * right_low + left_low * right_high

        return ans


"""
BIT

Idea: For every middle solider, count how many soliders smaller than it on the left (cL), how many soliders larger than it on the right (cR). For this solider as middle one, cL * cR is the result of ascending order. Also, do same thing for the descending order.

Code: Iterate all soliders as it is the middle solider. And then, count number of solider smaller than it, and bigger than it from both left and right halves by Fenwick Tree

"""


class BIT:
    def __init__(self, n):
        self._sums = [0] * (n + 1)  # note index i is 1-based

    def prefix_sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & (-i)

        return s

    def suffix_sum(self, i):
        return self.prefix_sum(100000) - self.prefix_sum(i - 1)

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def update(self, i, delta):  # i is 1-based
        # add delta at index i
        i += 1
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & (-i)


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        left_tree = BIT(100001)
        right_tree = BIT(100001)

        for r in rating:
            right_tree.update(r, 1)

        res = 0

        for r in rating:
            right_tree.update(r, -1)
            res += left_tree.prefix_sum(r - 1) * right_tree.suffix_sum(r + 1)
            res += left_tree.suffix_sum(r + 1) * right_tree.prefix_sum(r - 1)
            left_tree.update(r, 1)

        return res


def main():
    sol = Solution()
    assert sol.numTeams(rating = [2,5,3,4,1]) == 3, 'fails'

    assert sol.numTeams(rating = [2,1,3]) == 0, 'fails'

    assert sol.numTeams(rating = [1,2,3,4]) == 4, 'fails'

if __name__ == '__main__':
   main()