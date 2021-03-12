"""
57. Insert Interval
Medium

"""
from typing import List

"""
Interval

mistakes:
1. intervals could be empty
2. newInterval could be a sub-interval of some intervals
"""


class Solution0:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        curr_iv = newInterval
        i = 0
        added = False
        while i < len(intervals):
            # print('i=%s' % i)
            # if overlap
            iv = intervals[i]
            if iv[0] <= curr_iv[0] <= iv[1] or curr_iv[0] <= iv[0] <= curr_iv[1]:
                lo = min(iv[0], curr_iv[0])
                hi = max(iv[1], curr_iv[1])
                curr_iv[0] = lo
                curr_iv[1] = hi
                # print('curr_iv=%s' % curr_iv)
            else:  # no overlap
                if iv[0] > curr_iv[1] and not added:
                    result.append(curr_iv)
                    added = True
                result.append(iv)

            i += 1

        # needed to handle special case when newInterval is a sub-interval of one in intervals
        # or vice versa
        if not added:  # curr_iv not added, because there is no more intervals element for the above non-overlap case
            result.append(curr_iv)
            added = True

        return result


"""
Interval
use method from 56 merge intervals
iterate through starts, add to result, compare start of next to end of previous (end of last one of result), extend end of last in result if necessary
within each iteration step, check if it is time to add newInterval (intervals[i][0] <= newInterval[0] < intervals[i+1][0]), and handle newInterval if it is right order
Note: need to special handling of empty intervals, newInterval starts before all intervals

mistakes1:
1. intervals could be empty
2. newInteval could start before first of intervals

"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        result = []

        # special handling if newInterval[0] < intervals[0][0]
        if newInterval[0] < intervals[0][0]:
            result.append(newInterval)

        i = 0
        for i in range(n):
            iv = intervals[i]
            if result and iv[0] <= result[-1][1]:
                result[-1][1] = max(iv[1], result[-1][1])
            else:
                result.append(iv)

            # check if it is time to add newInterval
            # its time for newInterval if newInterval[0] is between [intervals[i][0], intervals[i+1][0])
            if (intervals[i][0] <= newInterval[0] and (i + 1 > n - 1 or newInterval[0] < intervals[i + 1][0])):
                if result and newInterval[0] <= result[-1][1]:
                    result[-1][1] = max(newInterval[1], result[-1][1])
                else:
                    result.append(newInterval)

        return result


def main():
    sol = Solution()
    assert sol.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]) == [[1,5],[6,9]], 'fails'

    assert sol.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]) == [[1,2],[3,10],[12,16]], 'fails'

    assert sol.insert(intervals = [[1,5]], newInterval = [2,3]) == [[1,5]], 'fails'

    assert sol.insert(intervals = [[1,5]], newInterval = [2,7]) == [[1,7]], 'fails'

if __name__ == '__main__':
   main()