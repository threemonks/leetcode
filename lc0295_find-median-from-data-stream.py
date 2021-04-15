"""
295. Find Median from Data Stream
Hard

4016

76

Add to List

Share
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""

"""
Follow question:
1. we know value within range [0, 100], we can use bucket sort, or store all values in array num[0...100], with value being the count of that index
2. if 99% value are within range [0, 100]? 99 buckets, and plus the count of numbers > 100
"""

"""
SortedList

"""
from sortedcontainers import SortedList


class MedianFinder0:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2


"""
Sort / Binary

keep the self.nums sorted using insertion sort / binary sort

time O(N+log(N)) - Olog(N) for binary search, O(N) for insertion
space O(N)
"""


class MedianFinder1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        lo, hi = 0, len(self.nums)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if self.nums[mi] == num:
                self.nums.insert(mi, num)
                return
            elif self.nums[mi] > num:
                hi = mi
            else:
                lo = mi + 1

        # insert at lo
        self.nums.insert(lo, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2


"""
Heap

Have two heaps, one min heap, one max heap, the min heap hold the larger half of nums, and the max heap hold the smaller half of nums, if we keep these two heaps balanced, i.e., both size would be at most len(nums)//2 for len(nums) even, or (len(nums)+1)//2 for len(nums) odd, then the median would be either the top of minheap, or the top of maxheap, depending on total size being even or odd.

time O(log(N)) resize heap
space O(N)
"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # if minheap[0] < -maxheap[0], we need swap them
        while self.minheap and self.maxheap and self.minheap[0] < -self.maxheap[0]:
            n1 = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -n1)
            n2 = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -n2)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
