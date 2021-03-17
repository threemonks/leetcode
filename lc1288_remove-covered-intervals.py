"""
1288. Remove Covered Intervals
Medium

"""
from typing import List

"""
Interval Sweep Line

brutal force 
- sort intervals by start time, and length descending (long first), would like longer interval add to result first when start time is the same
- iterate intervals
- for any new interval, is it covered by any interval in result
- if covered, skip this interval, else add it to result

time O(N^2)
space O(N)

mistakes:
1. for same starting time, we would like to add longer ones (larger ending time) to result first, as it is less likely to be covered by other intervals
"""


class Solution0:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))

        result = []

        for iv in intervals:
            if result and any([(r[0] <= iv[0] and r[1] >= iv[1]) for r in result]):
                # covered, drop
                continue
            else:
                result.append(iv)

        return len(result)


"""
Interval Sweep Line

Note: we only need to check if current interval is covered by immediate preceeding interval, because any interval before the proceeding one must ends before this proceeding one, else this proceeding one would be removed, so those interval before this proceeding interval must end ealier, so if this proceeding one does not cover current interval, then any other interval before that will not cover either
"""


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))

        result = []
        prev_end = None

        for start, end in intervals:
            if not prev_end or end > prev_end:
                # not covered by proceeding one, add to result
                result.append([start, end])

                # update prev_end
                prev_end = end

        return len(result)


def main():
    sol = Solution()
    assert sol.removeCoveredIntervals(intervals = [[1,4],[3,6],[2,8]]) == 2, 'fails'

    assert sol.removeCoveredIntervals(intervals = [[1,4],[2,3]]) == 1, 'fails'

    assert sol.removeCoveredIntervals(intervals = [[0,10],[5,12]]) == 2, 'fails'

    assert sol.removeCoveredIntervals(intervals = [[3,10],[4,10],[5,11]]) == 2, 'fails'

    assert sol.removeCoveredIntervals(intervals = [[1,2],[1,4],[3,4]]) == 1, 'fails'

if __name__ == '__main__':
   main()