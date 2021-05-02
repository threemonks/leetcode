"""
1847. Closest Room
Hard

68

6

Add to List

Share
There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.

You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:

The room has a size of at least minSizej, and
abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.

Return an array answer of length k where answer[j] contains the answer to the jth query.



Example 1:

Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
Output: [3,-1,3]
Explanation: The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.
Example 2:

Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
Output: [2,1,3]
Explanation: The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.


Constraints:

n == rooms.length
1 <= n <= 10^5
k == queries.length
1 <= k <= 10^4
1 <= roomIdi, preferredj <= 10^7
1 <= sizei, minSizej <= 10^7
"""
import bisect
from typing import List
from sortedcontainers import SortedList

"""
SortedList + Binary Search

Thoughts:
1. sort queries by decreaing minSize
2. sort rooms by decreasing size
3. create a orderedlist containing avail rooms so far, with size >= minSize of current query
4. use two pointers, for each query q in queries
    1. add into avail all room with size > minSize of current query
    2. query floor and ceiling of q[0] (perferred id) (use binary search or bisect.bisect_left) from avail rooms, to pick the id which closest to our preferredid.

mistakes:
1. k = bisect.bisect_left(avail, p) then check if k or k+1
   if we use bisect.bisect_right(avail, p), then check k and k-1
"""

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms = sorted(rooms, key=lambda x: x[1], reverse=True)  # sort by room size
        queries = sorted([(y, x, i) for i, (x, y) in enumerate(queries)], key=lambda q: q[0],
                         reverse=True)  # sort by query minsize, need to keep original index

        # print(rooms)
        # print(queries)

        avail = SortedList()  # available room ids for current queries, ordered

        i = 0  # pointer in queries
        j = 0  # pointer in rooms ordered by size

        ans = [-1] * len(queries)
        while i < len(queries):
            minsize, p, qi = queries[i]  # minsize, preferredroomid, query original index
            while j < len(rooms) and rooms[j][1] >= minsize:
                avail.add(rooms[j][0])
                j += 1

            # print('i=%s qi=%s p=%s minsize=%s j=%s avail=%s' % (i, qi, p, minsize, j, avail))
            # now with avail contains all room ids whose size > minsize
            # we find which room has smallest abs(roomid-perferredid)
            # if there's only one room availabe, we have to use it
            if len(avail) == 1:
                ans[qi] = avail[0]
                i += 1
                continue
            k = bisect.bisect(avail,
                              p)  # k is after p in avail (if p is in avail), so below we need to check k-1 in addition to k
            # print('k=%s' % k)
            # compare k-1 and k and k+1, pick whichever one has smallest abs(avail[?]-p)
            cands = []
            if k - 1 >= 0:
                cands.append(avail[k - 1])
            if k < len(avail):
                cands.append(avail[k])
            if cands:
                ans[qi] = min(cands, key=lambda x: abs(x - p))

            # print('i=%s ans=%s' % (i, ans))
            i += 1

        return ans


def main():
    sol = Solution()

    assert sol.closestRoom(rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]) == [3,-1,3], 'fails'

    assert sol.closestRoom(rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]) == [2,1,3], 'fails'


if __name__ == '__main__':
   main()