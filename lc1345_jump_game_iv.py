"""
1345. Jump Game IV
Hard

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3


Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108

"""
import collections
import heapq
from typing import List

"""
BFS

start from starting element, explore all directly accessible elements (-1, +1, j for arr[j]==arr[i]), put all valid next element into minheap queue, with number of steps to get to this element as weight, mark and process nodes with smaller weight/cost first, recursively process all nodes in the queue until queue is empty or end elements is reached.

Note: to speed up search, we eliminate a value from peers dict once used as all other edges come to this group would try to re-add these same sets of nodes into queue, and skipping this can improve performance.

time O(N)
"""


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr: return 0

        n = len(arr)
        peers = collections.defaultdict(list)

        if len(peers.keys()) == 1:  # one unique number only
            return 1

        for i, a in enumerate(arr):
            peers[a].append(i)

        q = [(0,
              0)]  # store all active index to consider its next step (-1, +1, and all same value peers), with steps to get to this node
        heapq.heapify(q)
        visited = set()
        visited.add(0)

        while q:
            steps, idx = heapq.heappop(q)
            # print('idx=%s steps=%s' % (idx, steps))
            if idx == n - 1:
                return steps
            neighbors = [i for i in peers[arr[idx]] if i != idx]

            # clear the list to prevent redudant search on this same value
            peers[arr[idx]].clear()

            neighbors = neighbors[::-1]  # reverse so that index towards end is checked first
            if idx - 1 not in neighbors:
                neighbors.append(idx - 1)
            if idx + 1 not in neighbors:
                neighbors.append(idx + 1)
            # print('neighbors=%s' % neighbors)
            for nei in neighbors:
                if nei < 0 or nei >= n or nei in visited:
                    continue
                heapq.heappush(q, (steps + 1, nei))
                visited.add(nei)

        return -1


def main():
    sol = Solution()
    assert sol.minJumps([100,-23,-23,404,100,23,23,23,3,404]) == 3, 'fails'

    assert sol.minJumps([7]) == 0, 'fails'

    assert sol.minJumps([7,6,9,6,9,6,9,7]) == 1, 'fails'

    assert sol.minJumps([6,1,9]) == 2, 'fails'

    assert sol.minJumps([11,22,7,7,7,7,7,7,7,22,13]) == 3, 'fails'

if __name__ == '__main__':
   main()