"""
1353. Maximum Number of Events That Can Be Attended
Medium

"""
import heapq
from typing import List

"""
Greedy PriorityQueue

For each day, there are some attendable events

which one do we attend first?
- intuitively, we attend the one that would ends soonest
how do we find the one ends soonest among all attendable events
- use minheap, that sort events by ending date
what are the attendable events?
- at time t, attendable events are such event e[0] <= t <= e[1]

steps:
1 sort all events by starting time
2. use priorityqueue (minheap) to keep track of all open events
3. iterate all possible days 1 ... 10**5+1
    for d in range(1...10^5+1)
4. remove from pq any closed event (e[1] < d)
5. for any event whose start time is current day (e[0] == d), add it to pq
6. we then try to greedily attend events that would ends soonest
    heapq.heappop(pq)
7. if we can attend event, increase result by 1
so we iterate all possible days (min([e[0] for e in events]) to max([e[1] for e in events])), and check all events ordered by start
add it to heap if e[0]<=t, and remove from heap if e[1] > t, increase count if we can attend it

mistakes:
1. greedily attend event that would end soonest:
    heapq.heappop(pq)
2. to avoid having to track which event has been added to queue (open events) because we also need to iterate through the events list for each time step, we sort events first, and use a global index i point at current event to be added (i+=1 once a event has been added to pq)
"""


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)

        events = sorted(events, key=lambda x: x[0])
        pq = []

        i = 0  # index for events, so we know which events we have added into pq

        ans = 0
        mind = min([e[0] for e in events])
        maxd = max([e[1] for e in events])
        for d in range(mind, maxd + 1):
            # print('d=%s' % d)
            # remove closed events
            while pq and pq[0] < d:
                # print('remove closed event %s' % pq[0])
                heapq.heappop(pq)

            # add open events
            while i < n and events[i][0] == d:
                # print('add open event i=%s' % i)
                heapq.heappush(pq, events[i][1])
                i += 1

            # greedily attend event
            if pq:
                # print('attending event %s' % pq[0])
                heapq.heappop(pq)
                ans += 1

        return ans

def main():
    sol = Solution()
    assert sol.maxEvents(events = [[1,2],[2,3],[3,4]]) == 3, 'fails'

    assert sol.maxEvents(events= [[1,2],[2,3],[3,4],[1,2]]) == 4, 'fails'

    assert sol.maxEvents(events = [[1,4],[4,4],[2,2],[3,4],[1,1]]) == 4, 'fails'

    assert sol.maxEvents(events = [[1,100000]]) == 1, 'fails'

    assert sol.maxEvents(events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]) == 7, 'fails'

if __name__ == '__main__':
   main()