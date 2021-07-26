"""
1857. Largest Color Value in a Directed Graph
Hard

125

6

Add to List

Share
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.



Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.


Constraints:

n == colors.length
m == edges.length
1 <= n <= 10^5
0 <= m <= 10^5
colors consists of lowercase English letters.
0 <= aj, bj < n
"""
"""
BFS + DP

dp[u][c] := maximum count of color c from any ancester nodes to vertex u

steps
1. detect cycle using BFS, start with nodes indegs==0, for all its neighbor nodes, reduce indeg by 1, if indeg =0 after reduce, add it to queue, repeat until queue is empty. Check if len(visited) == len(nodes), if so no cycle, else there is cycle
2. BFS traverse, after visiting each node, update its dp value color count dp[cur][colors[cur]-'a']+=1, also add it to visited set
3. explore cur's neighbor nodes u, if u not visited, 
   update all dp[u][0...25] using dp[cur][0...25]
       for c in range(26):
          dp[u][c] = max(dp[u][c], dp[cur][c]) # for each cur->u edge
4. traverse finishes when queue is empty
5. if len(visited) == len(vertices), no cycle, return max value from dp
   else cycle detected

time O(V+E)
space O(V+E)
"""
import copy


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, m = len(colors), len(edges)
        adj_list = defaultdict(list)
        indeg = defaultdict(int)
        for e in edges:
            adj_list[e[0]].append(e[1])
            indeg[e[1]] += 1

        # dp[u][c] := maximum count of color c from any ancester nodes to vertex u
        dp = [[0 for _ in range(26)] for _ in range(n)]  # 26 characters total

        # find indeg = 0 nodes
        q = deque()  # node, and color counts along parent path to here
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        visited = set()
        while q:
            cur = q.popleft()
            dp[cur][ord(colors[cur]) - ord('a')] += 1  # increase color count for this node once it has been visited
            visited.add(cur)
            for nxt in adj_list[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
                # update all dp[nxt][c], but only increase 1 for this color colors[nxt]
                for c in range(26):
                    # update neighbor node color count using current node's new color count (if it is bigger)
                    dp[nxt][c] = max(dp[nxt][c], dp[cur][c])

        if len(visited) != len(colors):  # cycle detected
            return -1
        else:
            return max([max(x) for x in dp])


def main():
    sol = Solution()

    assert sol.largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]) == 3, 'fails'

    assert sol.largestPathValue(colors = "a", edges = [[0,0]]) == -1, 'fails'


if __name__ == '__main__':
   main()