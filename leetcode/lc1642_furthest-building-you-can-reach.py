"""
1642. Furthest Building You Can Reach
Medium

4010

85

Add to List

Share
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.



Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3


Constraints:

1 <= heights.length <= 10^5
1 <= heights[i] <= 10^6
0 <= bricks <= 10^9
0 <= ladders <= heights.length
"""
from typing import List

"""
Heap

use minheap to allow ladder always consume large jumps and bricks cover rest small jumps, and see how far we can go

iterate through all jumps, if it is jump up, and total up jump r < ladders, we can keep go to next building
if total jump r > ladders, then we need to check if the new jump is larger than the min in heap (all jumps covered by ladder), use remaining bricks to cover the smaller jump

1. allocate a ladder if one is available
2. otherwise, look at smallest ladder allocation in heap. If the heap is empty or the current climb is shorter than the smallest in the heap, we subtract bricks for this climb. Otherwise, we reclaim a ladder from the smallest ladder allocation in the heapd, and subtract bricks to replace the ladder, until we run out of both ladder and bricks.

time: O(N*log(N))

"""
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        climbs = []
        for i in range(1, n):
            climbs.append((heights[i] - heights[i - 1], i))

        ans = 0

        q = []  # hold climbs that we used ladder for
        heapq.heapify(q)
        for climb, idx in climbs:
            # print(f"{idx = } {climb = } {q = }")
            if climb < 0:  # jump down should not require any bricks or ladders
                ans = max(ans, idx)
            elif len(q) < ladders:
                heapq.heappush(q, climb)
                ans = max(ans, idx)
            else:  # all ladders used
                if q and climb > q[0]:
                    if bricks >= q[0]:
                        minclimb = heapq.heappop(q)
                        heapq.heappush(q, climb)
                        bricks -= minclimb
                        ans = max(ans, idx)
                    else:
                        break
                else:
                    if bricks >= climb:
                        bricks -= climb
                        ans = max(ans, idx)
                    else:
                        break

        return ans


"""
Heap
use max-heap to hold all bricks usage, and replace largest brick usage if there's ladder left
"""

"""
Binary Search to find reachable building, and verify for each building if we can reach it
"""


def main():
    sol = Solution()
    assert sol.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1) == 4, 'fails'

    assert sol.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2) == 7, 'fails'

    assert sol.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0) == 3, 'fails'

if __name__ == '__main__':
   main()