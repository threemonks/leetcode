"""
252. Meeting Rooms
Easy

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
"""
from typing import List

"""
Intervals

observation:
sort intervals by starting time, and see if any new start is smaller than previous ending, if so return False
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prev_end = 0
        for iv in sorted(intervals, key=lambda x: x[0]):
            start, end = iv
            if start < prev_end:
                return False
            prev_end = end

        # no conflict
        return True


def main():
    sol = Solution()
    assert sol.canAttendMeetings(intervals = [[0,30],[5,10],[15,20]]) is False, 'fails'

    assert sol.canAttendMeetings(intervals = [[7,10],[2,4]]) is True, 'fails'

if __name__ == '__main__':
   main()