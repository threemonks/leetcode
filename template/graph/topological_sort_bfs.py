import collections


class Solution:
    # start at i, j, shortest path to get to target m, n
    def topological_sort_bfs(self, nums, prerequisites):
        # BFS time O(V+E), space O(V^2)

        # Step 1: build graph and init indegree
        adj_list = collections.defaultdict(list) # adjacency list
        indegree = collections.defaultdict(int) # indegree

        for s, t in prerequisites:
            if t not in adj_list[s]: # avoid adding this edge twice if there possible duplicates in prerequisites
                adj_list[s].append(t)
                indegree[t] += 1

        # Step 2: bfs
        # 2.1 init sources with all nodes with indegree = 0
        sources = collections.defaultdict(int) # all possible sources (indegree == 0)
        for num in nums:
            if indegree[num] == 0:
                sources.append(num)

        # 2.2 pop out nodes from sources queue to process it, reduce all its neighbors (destination of directed edges) indegree by 1
        # and add any neighbors now with indegree = 0 into queue for processing
        nums_sorted = list()
        while sources:
            node = sources.pop()
            nums_sorted.append(node)
            for child in adj_list[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)

        # method 1 checking cirlce
        if len(nums_sorted) == len(nums):
            return nums_sorted
        else:
            return [] # cycle detected

        # method 2 to check circle
        if sum(indegree) == 0:
            print('no circle')