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

        timestamps = [(t[0], 1) for t in self.events]  # start timestamps
        timestamps += [(t[1], -1) for t in self.events]  # start timestamps

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


class MyCalendarThree:

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