class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

from sortedcontainers import SortedDict

"""
Line Sweep

collect all event timestamp, sort them, with score, for start, +1, for end, -1, aggregate score for each timestamp - stored in SortedDict, when count == 0, means all employees free, so we basically count when count change from >0 to 0, and when it again change from 0 to >0

"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = SortedDict()
        
        for sched in schedule:
            for x in sched:
                if x.start in events:
                    events[x.start] += 1
                else:
                    events[x.start] = 1
                if x.end in events:
                    events[x.end] -= 1
                else:
                    events[x.end] = -1
        
        ans = []
        count = 0 # event start +=1, event end -=1
        start = -1 # indicate invalid start of free interval
        for e, c in events.items():
            count += c
            if count == 0 and start == -1: # entering free interval
                start = e
            elif start != -1 and count > 0: # ending free interval, add to result
                ans.append(Interval(start, e))
                start = -1
            
        return ans

"""
Line Sweep / Merge Interval

flat intervals from different employee, sort all intervals by start time,
1. if new interval start is before current interval ending, extend current interval ending (take max of existinb busy interval end and new interval end)
2. if new interval start is after current interval ending, there's a gap, add to result
"""

    class Solution:
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