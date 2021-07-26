"""
1851. Minimum Interval to Include Each Query
Hard

90

0

Add to List

Share
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.



Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.


Constraints:

1 <= intervals.length <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 2
1 <= lefti <= righti <= 10^7
1 <= queries[j] <= 10^7
"""
import heapq
from typing import List

"""
Line Sweep

sort queries
then sort intervals, and add intervals that are currently meet this query (open interval) to the heap, with (intervalsize, interval end point), so only valid intervals (for this query) are in the heapq, and it will pop out the smallest one first
also remove intervals who's end point has passed this query (closed interval) - this is removed when the node comes to top of priority queue

also needs to store original index in queries to reconstruct the answer
"""


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals = sorted(intervals)  # sort by start time
        hq = []  # store interval (size, end time) that's currently open for current query, and has not closed yet (end time has not passed)
        queries = sorted([[q, i] for i, q in enumerate(queries)])
        j = 0
        ans = [-1] * len(queries)

        for q, i in queries:
            while j < len(intervals) and intervals[j][0] <= q:
                heapq.heappush(hq, [intervals[j][1] - intervals[j][0] + 1,
                                    intervals[j][1]])  # store interval size, end time
                j += 1

            while hq and hq[0][1] < q:
                heapq.heappop(hq)

            if hq:
                ans[i] = hq[0][0]

        return ans

def main():
    sol = Solution()

    assert sol.minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]) == [3,3,1,4], 'fails'

    assert sol.getMinSwaps(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]) == [2,-1,4,6], 'fails'


if __name__ == '__main__':
   main()