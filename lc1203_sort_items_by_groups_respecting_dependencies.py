"""
1203. Sort Items by Groups Respecting Dependencies
Hard

There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.


Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.

"""
import collections
import math
from functools import lru_cache, partial
from typing import List

"""
build two graphs one for item, one for group
topological sort the item within each group, then topological sort each group
Note:
    1. need to get all items for each group, order them within each group
    2. when build graph for group, there could be duplicated edges (adj_list)
"""


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # assign a separate group id for each node with group id -1 (they does not belong to any group
        # and we need to treat them as with their own group)
        # setup group_items (items within each group)
        group_items = collections.defaultdict(list)
        next_group_id = m  # total number of groups m, so next possible group id to avoid conflict is m
        for i in range(n):
            if group[i] == -1:
                group[i] = next_group_id
                next_group_id += 1
            group_items[group[i]].append(i)
            # print('group_items=%s' % group_items)

        # topological sort items
        def topology_sort(nodes, adj_list, indegree):
            sources = collections.deque()
            for node in nodes:
                if indegree[node] == 0:
                    sources.append(node)

            output = []
            while sources:
                node = sources.popleft()
                output.append(node)
                for child in adj_list[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        sources.append(child)

            if len(output) == len(nodes):
                return output
            else:
                return []

        #  build graph adj_list and indegree for items
        adj_list = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for i, bi in enumerate(beforeItems):
            for j in bi:
                if group[j] != group[i]:  # per group item adj_list and indegree should only include information for items within a group
                    continue
                adj_list[j].append(i)
                indegree[i] += 1

        # print('adj_list=%s' % adj_list)
        # print('indegree=%s' % indegree)

        # sort items within each group
        group_items_ordered = dict()
        for g in group_items:
            items = group_items[g]
            group_items_ordered[g] = topology_sort(items, adj_list, indegree)
            if len(group_items_ordered[g]) != len(items):
                return []
        # print('group_items_ordered=%s' % group_items_ordered)

        # build graph for group
        adj_list = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for i, bi in enumerate(beforeItems):
            for j in bi:
                if group[i] == group[j]:  # both item in same group, this give no information about group graph
                    continue
                if group[i] not in adj_list[group[j]]:
                    adj_list[group[j]].append(group[i])
                    indegree[group[i]] += 1

        # print('adj_list=%s' % adj_list)
        # print('indegree=%s' % indegree)

        # sort groups
        groups = list(set([group[i] for i in range(n)]))
        # print('groups=%s' % groups)
        groups_ordered = topology_sort(groups, adj_list, indegree)
        # print('groups_ordered=%s' % groups_ordered)

        # output group_items_ordered for each group
        output = []
        for group in groups_ordered:
            for item in group_items_ordered[group]:
                output.append(item)

        return output


def main():
    sol = Solution()
    assert sol.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]) == [6, 3, 4, 5, 2, 0, 7, 1], 'fails'

    assert sol.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]) == [], 'fails'

if __name__ == '__main__':
   main()