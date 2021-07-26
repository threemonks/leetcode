"""
797. All Paths From Source to Target
Medium

2227

99

Add to List

Share
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).



Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]


Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
"""
"""
BFS modidified

"""


class Solution0:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        adj_list = defaultdict(list)

        for i, g in enumerate(graph):
            adj_list[i].extend(g)

        # print(adj_list)
        queue = deque()

        # start
        queue.append((0, [0]))  # node, and path from orig to this node

        ans = []
        while queue:
            cur, path = queue.popleft()
            # print('cur=%s path=%s queue=%s' % (cur, path, queue))
            if cur == n - 1:
                ans.append(path)

            for nei in adj_list[cur]:
                # if nei not in path: # can revisit if not on the path, DAG, no cycle, no need to check next node in parent or not.
                queue.append((nei, path + [nei]))

        return ans


"""
Backtrack

Note:
1. use meaningful function name
2. use parameter instead of scope variable
3. use path.append() and path.pop() instead of path+[nxt] to explicitly show the idea of backtracking
4. results.append(path[:]) # must make copy of path to append into results
"""


def explore(graph, cur, target, path, results):
    if cur == target:
        # print('cur=%s target=%s adding result %s' % (cur, target, path))
        results.append(path[:])
        # print('results=%s' % results)
        return
    for nxt in graph[cur]:
        path.append(nxt)
        explore(graph, nxt, target, path, results)
        path.pop()


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        start, target = 0, n - 1

        results = []
        path = [start]
        explore(graph, start, target, path, results)

        return results

def main():
    sol = Solution()
    assert sol.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]], 'fails'

    assert sol.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]], 'fails'

    assert sol.allPathsSourceTarget(graph = [[1],[]]) == [[0,1]], 'fails'

    assert sol.allPathsSourceTarget(graph = [[1,2,3],[2],[3],[]]) == [[0,1,2,3],[0,2,3],[0,3]], 'fails'

    assert sol.allPathsSourceTarget(graph = [[1,3],[2],[3],[]]) == [[0,1,2,3],[0,3]], 'fails'

if __name__ == '__main__':
   main()