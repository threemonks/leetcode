"""
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

1743. Restore the Array From Adjacent Pairs
Medium

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.



Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]


Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 105
-105 <= nums[i], ui, vi <= 105
There exists some nums that has adjacentPairs as its pairs.

"""
import collections
from typing import List

"""
1. build an undirected graph (adj_list) with the pair of values
2. calculate indegree of the nodes while adding them to the graph
3. start BFS (or DFS) traverse from a node with indegree==1, the complete traverse path will be the result

"""
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)

        for ap in adjacentPairs:
            adj_list[ap[0]].append(ap[1])
            indegrees[ap[1]] += 1
            adj_list[ap[1]].append(ap[0])
            indegrees[ap[0]] += 1

        # there should be two nodes with indegree==1, we start from sources[0], search for sources[1]
        sources = [num for num in indegrees if indegrees[num] == 1]

        q = collections.deque([sources[0]])
        visited = set()

        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nxt in adj_list[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(cur)

        return res


def main():
    sol = Solution()
    assert sol.restoreArray([[2,1],[3,4],[3,2]]) == [1, 2, 3, 4], 'fails'

    assert sol.restoreArray([[4,-2],[1,4],[-3,1]]) == [-2, 4, 1, -3], 'fails'

    assert sol.restoreArray([[100000, -100000]]) == [-100000, 100000], 'fails'


if __name__ == '__main__':
   main()