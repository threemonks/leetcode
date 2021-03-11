"""
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List

"""
Intervals

sort intervals by start time
for any new interval, if start is before previous ending, then merge (extend previous ending if new interval ends after previous interval)
else (start after previous ending), add this new interval into result

time O(N)
space O(N)

mistakes:
1. new interval could be covered completely by last of previous interval
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        result = []

        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result


def main():
    sol = Solution()
    assert sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]], 'fails'

    assert sol.merge(intervals = [[1,4],[4,5]]) == [[1,5]], 'fails'



if __name__ == '__main__':
   main()