"""
253. Meeting Rooms II
Medium

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
import collections
from typing import List

"""
Intrevals / Sweep line

1. sort intervals by start time
2. use a sweep line start from min start time to max end time
3. , for each end time, decrease room counter by 1, for each starttime, increase room counter by 1 # decrease for end time first if one end and another start is the same
4. keep track of global max of room counter

time O(M) - M is total time from start of first meeting to end of last meeting

Note: this is not efficient, as we don't need to go to each timestamp, as we don't need all the timestamps that no even happens

mistakes:
1. two meeting starts at same time, so we need to counter number of starts and ends at each timestep

"""


class Solution0:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = collections.Counter([iv[0] for iv in intervals])
        ends = collections.Counter([iv[1] for iv in intervals])

        global_start = min(starts)
        global_end = max(ends)

        ans = 0
        count = 0
        for i in range(global_start, global_end + 1):
            if i in ends:
                count -= ends[i]
            if i in starts:
                count += starts[i]
            ans = max(ans, count)

        return ans


"""
Intrevals / Sweep line

1. Save all time points and the change on current meeting rooms.
2. Sort all the changes on the key of time points.
3. Track the current number of using rooms cur and update result res.

"""


class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timestamp = []
        for iv in intervals:
            timestamp.append((iv[0], 1))  # starting time, room # increase by 1
            timestamp.append((iv[1], -1))  # ending time, room # decrease by 1

        ans = 0
        room = 0
        # now sort all timestamps, and iterate through in order
        # find max room number of all time
        # this sort guarantees room decrease before increasing if one meeting starts at same time as previous ending
        for ts_count in sorted(timestamp):
            ts, count = ts_count
            room += count
            ans = max(ans, room)

        return ans


import heapq

"""
Sort + Heap

Sort meetings by starting time, iterate through the meetings
for each new meeting, if its start time is later than or equal to the earliest meeting end time in heap, replace that meeting end time with this new ending time, means it reuse the same room as this previous meeting
if this meeting start time is before the earliest meeting ending time in heap, that means this meeting needs a new room, so we push this new meeting's ending time into heap.

The size of heap at end is total room numbers needed

time O(N*log(N)) - sorting
space O(N) - heap

"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        hq = []
        heapq.heapify(hq)
        for start, end in sorted(intervals, key=lambda x: x[0]):
            if hq and start >= hq[0]:
                heapq.heapreplace(hq, end)  # reuse this room
            else:
                heapq.heappush(hq, end)  # need a new room

        return len(hq)


def main():
    sol = Solution()
    assert sol.minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]) == 2, 'fails'

    assert sol.minMeetingRooms(intervals = [[7,10],[2,4]]) == 1, 'fails'

if __name__ == '__main__':
   main()