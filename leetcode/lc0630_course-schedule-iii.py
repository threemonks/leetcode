"""
630. Course Schedule III
Hard

1155

44

Add to List

Share
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.



Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation:
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:

Input: courses = [[1,2]]
Output: 1
Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0


Constraints:

1 <= courses.length <= 10^4
1 <= durationi, lastDayi <= 10^4
"""
import heapq
from functools import lru_cache
from typing import List

"""
Greedy / Sort + Heap

1. Sort courses by the end date, this way, when we're iterating through the courses, we can switch out any previous course with the current one without worrying about end date.

2. Next, we iterate through each course, if we have enough days, we'll add it to our priority queue. If we don't have enough days, then we can either
2.1 ignore this course OR
2.2 We can replace this course with the longest course we added earlier in the priority queue, so we use max heap (negative duration in min heap)

Note:
1. store negative duration in heap since python heap is minheap, and we need to replace course with longest duration if possible
2. Push or pop the heapq only when necessary

"""


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        hq = []
        curtime = 0

        for duration, end in courses:
            # if we can finish this course, add to current queue
            curtime += duration
            heapq.heappush(hq, -duration)  # min heap, but we want to try replace longer course first if necessary

            # if this course won't finish in time, can we swap it with one we finished already
            if curtime > end:
                long_duration = heapq.heappop(hq)
                curtime += long_duration  # This can be some other long course (negative)

        return len(hq)


"""
DP

sort courses by ending time, then for each course, take and not take, return max result of the two options

"""


class Solution1:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        courses = sorted(courses, key=lambda x: x[0])

        @lru_cache(None)
        def helper(k, t):
            nonlocal courses
            # with up to k courses, finish at time t
            # base case
            if k == n:
                return 0

            taken = 0
            if t + courses[k][0] <= courses[k][1]:
                taken = 1 + helper(k + 1, t + courses[k][0])
            not_taken = helper(k + 1, t)

            return max(taken, not_taken)

        return helper(0, 0)

def main():
    sol = Solution()
    assert sol.scheduleCourse(courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]) == 3, 'fails'

    assert sol.scheduleCourse(courses = [[1,2]]) == 1, 'fails'

    assert sol.scheduleCourse(courses = [[3,2],[4,3]]) == 0, 'fails'


if __name__ == '__main__':
   main()