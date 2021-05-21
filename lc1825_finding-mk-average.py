"""
1825. Finding MK Average
Hard

45

36

Add to List

Share
You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
Remove the smallest k elements and the largest k elements from the container.
Calculate the average value for the rest of the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.


Example 1:

Input
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
Output
[null, null, null, -1, null, 3, null, null, null, 5]

Explanation
MKAverage obj = new MKAverage(3, 1);
obj.addElement(3);        // current elements are [3]
obj.addElement(1);        // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
obj.addElement(10);       // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
                          // After removing smallest and largest 1 element the container will be [3].
                          // The average of [3] equals 3/1 = 3, return 3
obj.addElement(5);        // current elements are [3,1,10,5]
obj.addElement(5);        // current elements are [3,1,10,5,5]
obj.addElement(5);        // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
                          // After removing smallest and largest 1 element the container will be [5].
                          // The average of [5] equals 5/1 = 5, return 5


Constraints:

3 <= m <= 10^5
1 <= k*2 < m
1 <= num <= 10^5
At most 105 calls will be made to addElement and calculateMKAverage.

"""
from collections import deque
from sortedcontainers import SortedList
from collections import deque
from sortedcontainers import SortedList

"""
Deque

use deque, and maintain its length m, with each new element adding, remove one from left
when asked to calc MKAverage, sort the list, calculate average for m-2*k (k smallest, k largest)

time: addElement O(1)
      calculateMKAverage ON(log(N))
space: O(N)

TLE
"""


class MKAverage0:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = deque()

    def addElement(self, num: int) -> None:
        if len(self.nums) == self.m:
            self.nums.popleft()
        self.nums.append(num)

    def calculateMKAverage(self) -> int:
        # calculate sum of last m
        # then substract k smallest num sum, and k largest num sum
        if len(self.nums) < self.m:
            return -1
        nums_sorted = sorted(self.nums)

        return int(sum(nums_sorted[self.k:self.m - self.k]) / (self.m - 2 * self.k))


"""
Deque and sorted list with sliding window

use deque, and maintain its length m, with each new element adding, remove one from left, at same time, maintain a sorted list of past m elements, and total of all m elements

and keep the sum of smallest k elements, and largest k elements, as we add new element, we update deque, sorted list, and sum of all m elements, sum of smallest k elements, and sum of largest k elements, also do these update if we need to remove element from left of deque (because size exceeding m)

time: addElement O(log(N))
      calculateMKAverage O(1)
space: O(N)
"""


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = deque()
        self.sl = SortedList()
        self.total = 0
        self.smallest_ksum = 0
        self.largest_ksum = 0

    def addElement(self, num: int) -> None:
        # add new element into dq, sl, and update sums
        self.total += num
        self.nums.append(num)
        # is num within smallest k, or largest k, if so update that part
        index = self.sl.bisect_left(num)
        if index < self.k:
            self.smallest_ksum += num
            if len(
                    self.sl) >= self.k:  # we also need to remove the largest value from smallest_ksum since this is smallest k elements sum, we need to remove 1 element after adding 1 to keep it as k elements sum
                self.smallest_ksum -= self.sl[self.k - 1]
        if index >= len(self.sl) + 1 - self.k:
            self.largest_ksum += num
            if len(self.sl) >= self.k:  # remove the smallest value in self.largest_ksum
                self.largest_ksum -= self.sl[-self.k]
        self.sl.add(num)  # now add num to SortedList

        # after we addd new number num, we need to remove one from self.nums and self.sl if necessary
        if len(self.nums) > self.m:
            num = self.nums.popleft()
            # now remove num from sl, and update all sums
            self.total -= num
            index = self.sl.index(num)
            if index < self.k:
                self.smallest_ksum -= num
                self.smallest_ksum += self.sl[self.k]
            elif index >= len(self.sl) - self.k:
                self.largest_ksum -= num
                # remove smallest value in self.largest_ksum
                self.largest_ksum += self.sl[-self.k - 1]
            # now we can remove num from sl
            self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        # calculate sum of last m
        # then substract k smallest num sum, and k largest num sum
        if len(self.nums) < self.m:
            return -1

        return (self.total - self.smallest_ksum - self.largest_ksum) // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


def main():
    obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    obj.calculateMKAverage()
    obj.addElement(10)
    obj.calculateMKAverage()
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    obj.calculateMKAverage()

if __name__ == '__main__':
   main()