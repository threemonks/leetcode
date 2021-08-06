"""
所有结点分为两部分：已确定最短路的结点集合P、未知最短路的结点集合Q。最开始，P中只有源点这一个结点。（可用一个book数组来维护是否在P中）
在Q中选取一个离源点最近的结点u（dis[u]最小）加入集合P。然后考察u的所有出边，做松弛操作。
重复第二步，直到集合Q为空。最终dis数组的值就是源点到所有顶点的最短路。

dijkstra大概就是两种写法：1. queue + dict, 2. heap
遇到符合条件的解立即返回的话，用heap就行了
需要求出某点到所有其它点的最优解，就得用queue + dict，这个dict会保存起点到其它所有点的最优解

"""
import collections
import heapq
import math
from typing import List

class Solution:
    # Simple Dijkstra algo without PriorityQueue
    def dijkstra(self, graph, n):
        adj_list = graph # construct adj_list from graph
        dist = [float("inf") for i in range(n + 1)]  # 存储每个点到节点0的最短距离
        q = [[0, 0]]

        while q:
            cur, cost = q.popleft()

            for nbr, nbr_cost in adj_list[cur]:
                if nbr not in dist or cost + nbr < dist[nbr]: # better cost found
                    dist[nbr] = cost + nbr_cost
                    q.append([nbr, dist[nbr]])

        if dist[n-1] >= math.inf/2:
            return -1
        else:
            return dist[n-1]

    # Dijkstra with PriorityQueue
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        q = [(0, k)]  # min cost from start node to this node, node
        heapq.heapify(q)

        mincost = dict()
        while q:
            d, cur = heapq.heappop(q)
            if cur in mincost: continue
            mincost[cur] = d
            for nxt, dc in adj_list[cur]:
                    heapq.heappush(q, (d + dc, nxt))

        # print('dist=%s' % dist)
        return max(mincost.values()) if len(mincost) == n else -1