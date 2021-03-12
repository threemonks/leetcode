"""
732. My Calendar III
Hard

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.


Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3


Constraints:

0 <= start < end <= 109
At most 400 calls will be made to book.

"""
import math

"""
Sweep Line
brutal force
store all events so far, solve meetings-ii

time O(N^2)
space O(N)
"""

class MyCalendarThree0:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        self.events.append((start, end))

        timestamps = [(t[0], 1) for t in self.events] # start timestamps
        timestamps += [(t[1], -1) for t in self.events] # start timestamps

        timestamps = sorted(timestamps)
        max_count = 0
        count = 0
        for ts in timestamps:
            count += ts[1]
            # print('ts=%s count=%s' % (ts, count))
            max_count = max(max_count, count)
            if ts == start:
                break

        return max_count

from sortedcontainers import SortedList
"""
Sweep Line
try to use SortedList to store all timestamps
time O(N^2)
space O(N)
"""

class MyCalendarThree1:

    def __init__(self):
        self.timestamps = SortedList()

    def book(self, start: int, end: int) -> int:
        self.timestamps.add((start, +1))
        self.timestamps.add((end, -1))
        max_count = 0
        count = 0
        for ts in self.timestamps:
            count += ts[1]
            max_count = max(max_count, count)
        return max_count

"""
Segment Tree

"""

class Node:
    # Segment Tree for range max query
    # half-open inteval [lo, hi)
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.val = val # range max
        self.left = None
        self.right = None

class MyCalendarThree:
    # boundary of calendars

    def __init__(self):
        self.root = Node(0, 10**9+1, 0)

    def book(self, start: int, end: int) -> int:
        self.update(self.root, start, end-1)
        return self.root.val # maximum k-booking between all previous events
        #return self.query(self.root, start, end-1) # maximum booking between start and end

    def query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.val
        mid = node.start + (node.end - node.start)//2
        res = -math.inf
        if not node.left:
            node.left = Node(node.start, mid, node.val)
        if not node.right:
            node.right = Node(mid+1, node.end, node.val)

        if start <= mid:
            res = max(res, self.query(node.left, start, end))
        if end > mid:
            res = max(res, self.query(node.right, start, end))

        return res

    def update(self, node, start, end):
        # for each events [start, end), bookings+1
        # we should update all related nodes to maintain max bookings for [start, end)
        # time O(N*log(N))
        # spance O(N)
        if start <= node.start and node.end <= end:
            node.val += 1
            if node.left:
                self.update(node.left, start, end)
            if node.right:
                self.update(node.right, start, end)
            return

        # update left and right recursively
        mid = node.start + (node.end - node.start) // 2
        if not node.left:
            node.left = Node(node.start, mid, node.val)
        if not node.right:
            node.right = Node(mid+1, node.end, node.val)
        if start <= mid:
            self.update(node.left, start, end)
        if end > mid:
            self.update(node.right, start, end)

        node.val = max(node.left.val, node.right.val)

def main():

    myCalendarThree = MyCalendarThree()
    myCalendarThree.book(10, 20)
    myCalendarThree.book(50, 60)
    myCalendarThree.book(10, 40)
    myCalendarThree.book(5, 15)
    myCalendarThree.book(5, 10)
    myCalendarThree.book(25, 55)

if __name__ == '__main__':
   main()