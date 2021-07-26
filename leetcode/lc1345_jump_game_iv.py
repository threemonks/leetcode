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

from index i can jump to
1. i+1
2. i-1
3. arr[i] == arr[j] where i != j => all index with same value would be adjacent to each other

in BFS, once a peer group of nodes are added into queue, we clear the set since later it might be added again and again, and we want to avoid this.

time O(N)

mistakes:
1. have to clear each peer set once all its nodes have been added to BFS queue, as they will be re-added later on, thus causing each of its node being added m-1 times (for a set of size m members)
"""
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:  # single element, no need to jump
            return 0
        if len(set(arr)) == 1 or arr[0] == arr[n - 1]:  # all values being same, just one step
            return 1
        peers = defaultdict(set)

        for i, a in enumerate(arr):
            peers[a].add(i)

        q = deque([(0, 0)])
        visited = set([0])

        while q:
            cur, step = q.popleft()
            if cur == n - 1:
                return step
            neighbors = [v for v in set([cur - 1, cur + 1] + list(peers[arr[cur]])) if v != cur and 0 < v < n]
            peers[arr[cur]] = {}  # clear this peer set since all its member nodes are now already visited
            for nxt in sorted(neighbors)[::-1]:  # sort neighbors and try largest index first
                if nxt < 0 or nxt >= n:
                    continue
                if nxt not in visited:
                    q.append((nxt, step + 1))
                    visited.add(nxt)

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