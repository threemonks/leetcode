"""
759. Employee Free Time
Hard

838

58

Add to List

Share
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.



Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]


Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
"""

# Definition for an Interval.
from collections import defaultdict


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self):
        return '(%s, %s)' % (self.start, self.end)


"""
Line Sweep

collect all event timestamp, with score, for start, +1, for end, -1, aggregate score for each timestamp, sort by keys, when count == 0, means all employees free, so we basically count when count change from >0 to 0, and when it again change from 0 to >0

time O(Nlog(K)) - N is number of intervals per employee, K is number of employees

mistakes:
1. sort event by (time, count-+), note decrease first, increase after
2. combine score change on same timestamp, using defaultdict(int), SortedDict, may simplify logic
3. check only free interval start (start=-1 and count==0) and end (start!=-1 and count!=0)
"""


class Solution0:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = defaultdict(int)

        for sched in schedule:
            for x in sched:
                events[x.start] += 1
                events[x.end] -= 1

        ans = []
        count = 0  # event start +=1, event end -=1
        start = -1  # indicate invalid start of free interval
        for ts in sorted(events.keys()):
            c = events[ts]
            count += c
            if count == 0 and start == -1:  # entering free interval
                start = ts
            elif start != -1 and count > 0:  # ending free interval, add to result
                ans.append(Interval(start, ts))
                start = -1

        return ans


"""
Line Sweep / Merge Interval

flat intervals from different employee, sort all intervals by start time,
1. if new interval start is before current interval ending, extend current interval ending (take max of existinb busy interval end and new interval end)
2. if new interval start is after current interval ending, there's a gap, add to result

mistakes:
1. new end could be even smaller than prev_end, so we need to take max of prev_end and new interval end, as extended end of current busy interval
"""


class Solution1:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []

        for sched in schedule:
            for x in sched:
                events.append(x)

        events = sorted(events, key=lambda x: (x.start,
                                               x.end))  # for same timestamp, shorter one goes first, but it actually does not matter which one goes first

        ans = []
        prev_end = events[0].end
        for x in events[1:]:
            if x.start > prev_end:
                ans.append(Interval(prev_end, x.start))
            prev_end = max(prev_end, x.end)

        return ans


"""
PriorityQueue

Using the information that each employee's intervals are already sorted, we can do k-merge style sort usng priority queue
store into pq the start time, along with which employee (employee_id), so that when we remove one node from pq, we will add one more event from that employee if there's any event start time has not passed.

Steps:
1. get one interval from each employee, store (start, end) into priorityqueue, along with employee id
2. while priorityqueue is not empty, pop one out with smallest start time
2.1 if this new interval start > end of previous busy interval, add this free interval (prev_end, this start) to result
2.2 update previous busy interval end to max of (prev busy end, this interval end)
3. if there's any more intervals for this employee left, pick next one from him and insert into prorityqueue.

Time complexity O(N log K)

mistakes:
1. need to update previous end to max of previous end, and current interval end. - new interval could end earlier than previous one
"""
import heapq


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        n = len(schedule)
        q = []
        index = [0] * n  # index pointer for each employee (not using LinkedList)
        for emp_idx, emp in enumerate(schedule):
            interval = emp[index[emp_idx]]
            heapq.heappush(q, (interval.start, interval.end, emp_idx))

        res = []
        prev_end = None
        while q:
            cur_start, cur_end, emp_idx = heapq.heappop(q)
            if prev_end is None:
                prev_end = cur_end
            # 1. if there's free period from end of last busy interval to start of next busy interval, add to result
            if prev_end < cur_start:  # free period
                res.append(Interval(prev_end, cur_start))
            # 2. replace with new busy interval or extended by it
            prev_end = max(prev_end, cur_end)

            # add next interval from this employee into queue if there's one
            index[emp_idx] += 1
            if index[emp_idx] < len(schedule[emp_idx]):
                interval = schedule[emp_idx][index[emp_idx]]
                heapq.heappush(q, (interval.start, interval.end, emp_idx))

        return res