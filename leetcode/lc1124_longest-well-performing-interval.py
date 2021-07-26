"""
1124. Longest Well-Performing Interval
Medium

661

77

Add to List

Share
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.



Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].


Constraints:

1 <= hours.length <= 10000
0 <= hours[i] <= 16
"""
from typing import List

"""
Hash Map

Observation, each hour > 8 adds score +1, each hour <= 8, adds score -1, so the problem is to look for longest subarray with positive sum.

subarray sum can be obtained with diff of prefix sum.

prefix sum diff would be presum[i] - presum[j]

if presum[i] > 0, then longest subarray would be the one started at index 0, gives subarray length i+1

if presum[i] < 0, presum[j]=presum[i]-1 would give subarray of positive sum 1, first presum[j] would give longest subarray, since presum starts at 1 or -1, so any presum[k] < presum[j]<-1 would come later than presum[j], thus will only give shorter subarray of positive sum, and any presum[k] to left of j would give 0 or negative sum = (presum[i] - presum[k]).

So we need to find first occurence of presum[i]-1, which gives longest subarray of positive sum i - seen[presum[i]-1]

"""


class Solution0:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        seen = dict()
        presum = [0 for _ in range(n + 1)]  # presum[0] is sentinel val
        for i in range(1, n + 1):
            if hours[i - 1] > 8:
                presum[i] = presum[i - 1] + 1
            else:
                presum[i] = presum[i - 1] - 1
            if presum[i] not in seen:
                seen[presum[i]] = i  # first occurence of presum[i] # this gives longest subarray to value presum[i]+1

        ans = 0
        for i in range(1, n + 1):
            if presum[i] > 0:  # if presum[i] > 0, longest subarray with positive sum would be starting from beginning
                ans = max(ans, i)
            else:  # else if presum[i] < 0, longest subarray would be the one starts at presum[i]-1 (if exists)
                if presum[i] - 1 in seen:
                    ans = max(ans, i - seen[presum[i] - 1])

        return ans


"""
Stack

Similar to above, hour>8 => score = 1, hour<=8 => score=-1, we are trying to find longest subarray with positive sum on scores

After calculating prefixsum, we use monotonic decreasing stack to keep track of all decreasing prefixsum, for each value at stack top, we want to pair it up with a prefixsum that's larger, but furtherst to the right, this will give us a longest subarray for this value.

To get furtherst (right most) larger prefix sum, we iterate prefix sum from right to left, and pop all smaller value from stack top as those are not optimal (valid, but shorter, while remaining stack top element would give longer and valid subarray), until the stack top value is larger than the current prefixsum being iterating, than we check next value in prefix sum.

"""


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        presum = [0 for _ in range(n + 1)]  # presum[0] is sentinel val
        for i in range(1, n + 1):
            if hours[i - 1] > 8:
                presum[i] = presum[i - 1] + 1
            else:
                presum[i] = presum[i - 1] - 1

        # monotonic decreasing stack of presum elements
        stack = []

        for i in range(0, n + 1):
            if not stack or presum[i] < presum[stack[-1]]:
                stack.append(i)

        ans = 0
        for i in range(n, -1, -1):
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i - stack.pop())

        return ans


def main():
    sol = Solution()
    assert sol.longestWPI(hours = [9,9,6,0,6,6,9]) == 3, 'fails'


if __name__ == '__main__':
   main()