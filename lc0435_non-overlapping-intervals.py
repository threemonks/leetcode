"""
435. Non-overlapping Intervals
Medium

"""
from typing import List

"""
Intervals / Sweepline / Greedy

To perform least removal and obtain non-overlapping, is same as schedule most number of intervals without overlapping, a greedy approach to schedule most intervals would be to always schedule the ones with ending time first

steps:
1. sort interval by end time
2. iterate through intervals, if a new interval end time is no early than the latest scheduled intervals ending time, then this interval can be scheduled

when done, result would contain maximum number of non-overlapping intervals that can be chosen, we can derive minimum number of interval to remove to keep rest interval non-overlapping
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        result = []
        for iv in intervals:
            if not result or iv[0] >= result[-1][1]:  # if new interval does not overlap with last scheduled
                result.append(iv)

        return len(intervals) - len(result)

def main():
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1, 'fails'

    assert sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2, 'fails'

    assert sol.eraseOverlapIntervals([[1,2],[2,3]]) == 0, 'fails'


if __name__ == '__main__':
   main()