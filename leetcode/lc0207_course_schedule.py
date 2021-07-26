"""
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""
import collections
from functools import lru_cache
from typing import List

"""
observation
判断有向图是否有环
course a prerequisites b means a -> b in graph
the problem is to detect if there's a cycle in the graph
1. DFS
从任一个未访问过的节点开始做DFS遍历，如果在某个支路遍历过程中（还没有到出度为0的点），遇到了任何一个在这条支路中已经访问过的节点，那就判断成环。注意不是“遇到任何已经访问过的节点”。
如何区分在这条支路中已经访问过的节点，和任何已经访问过的节点？需要两种不同方法标记已经访问过的节点。在某个支路访问中第一次遇到某个未访问过的节点，标记为2，如果遇到已经标记为2的节点，则表示有环。如果到达支路末端（出度为0的节点），都没有遇到标记为2的节点，则回溯返回，同时标记遇到的节点为1（以后任何其他访问遇到标记为1 的节点可以直接返回，因为标记1 的节点后面是死胡同，没有环）。如果能成功返回到起点，则此支路没有环。
  def dfs(curr)
    if visited[curr] == 1:
        return True
    visited[cur] = 2
    for dep in cur.dependencies:
        if visited[dep] == 1: continue # this branch is ok
        if visited[dep] == 2: return False
        else visited[dep] == 0:
            if dfs(dep) is False:
                return False
    visited[cur] = 1
    return True
"""

class Solution0:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build depenceny list
        deplist = collections.defaultdict(list)

        for pair in prerequisites:
            src, dest = pair
            deplist[src].append(dest)

        # print(deplist)

        # traverse all coureses via toplogical sort
        visited = collections.defaultdict(int)

        @lru_cache(None)
        def dfs(cur):
            nonlocal visited, deplist
            if visited[cur] == 1:
                return True
            elif visited[cur] == 2:
                return False  # cycle detected down this node
            else:
                visited[cur] = 2
                for dep in deplist[cur]:
                    # for dep, we can skip the visited test, just call dfs(dep) directly, and return False if False, otherwise do nothing else (continue)
                    if visited[dep] == 1:
                        continue
                    elif visited[dep] == 2:
                        return False  # cycle detected down this node
                    else:  # not visited yet
                        if dfs(dep) is False:
                            return False
                        else: # this branch can be dropped
                            continue

                visited[cur] = 1

                return True

        for cur in range(numCourses):
            if dfs(cur) is False:
                return False

        return True

"""
2. BFS (topological sort) 
 BFS核心是拓扑排序。就是遍历图中所有节点，寻找入度为0的节点cur，处理其指向节点(dependencies)（减少其入度，加入queue）,然后把节点cur从queue弹出，同时记录当前cur为处理过。当遍历结束，应该是所有节点都处理过（count == len(numCourses），否则即可判断有环。
"""

class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build dependency list
        deplist = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for pair in prerequisites:
            src, dest = pair
            deplist[src].append(dest)
            indegree[dest] += 1

        # loop through all vertices and add those with 0 indegree into queue
        count = 0  # how many nodes of 0 indegree have we got?
        q = []
        for cur in range(numCourses):
            if indegree[cur] == 0:
                q.append(cur)
                count += 1

        while q:
            cur = q.pop()
            for dep in deplist[cur]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)
                    count += 1

        return count == numCourses


"""
using postorder dfs to traverse the tree
for each node
    if it is already in our path:
        then there is a cycle
    else:
        postorder traverse all its children (adjacent list),
        after that, we mark this node as visisted (postorder)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert prerequisites to adjacency matrics (edges)

        adj = dict()
        for p in prerequisites:
            c, dep = p
            if dep in adj:
                adj[dep].append(c)
            else:
                adj[dep] = [c]

        visited = set()
        def postorder_dfs(cur, path):
            """
            return False if there's cycle when we start at course i
            """
            nonlocal visited
            # print('cur=%s visited=%s' % (cur, visited))
            if cur in visited:
                return True
            else:
                if cur in path:
                    return False # cycle detected
                else:
                    if cur in adj:
                        for j in adj[cur]:
                            if postorder_dfs(j, path+[cur]) is False:
                                return False
                    visited.add(cur)
                    return True

        for cur in range(numCourses):
            if postorder_dfs(cur, []) is False:
                return False

        return True


"""
toplogical sort implemented via BFS

L = empty list that will contain sorted elements
S = set of all nodes with no incoming edge

while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do:
        insert m into S

if graph has edges then
    return error (graph has at least one cycle)
else:
    retur L (a topologically sorted order)

1. start from nodes without prerequisites (indegree=0), add it to global ordered list, following the dependenceis (edges)
2. once we follow an edge, we then remove the edge from the graph
3. with removal of edges, there would then be more nodes appearing without any prerequisit dependency (indegree=0), in addition to the initial list in the first step
4. the algorithm would terminate when we can no longer remove any edges from the graph. There are two possible outcomes:
    1) if there are still some edges left in the graph, then these edges must have formed certain cycles, which is similar to the deadlock situation. It is due to thse cyclic dependencies that we can not remove them during the above process.
    2) Otherwise, we have removed all the edges from the graph, and we got a topological order of the graph.
"""
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert prerequisites to dependencylist
        # also construct indegree list

        deplist = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for p in prerequisites:
            prereq, c = p
            deplist[prereq].append(c)
            indegrees[c] += 1

        # print('deplist=%s' % deplist)
        # print('indegrees=%s' % indegrees)

        L = []  # sorted list
        q = []  # all course/nodes with indegree=0

        for c in range(numCourses):
            if indegrees[c] == 0:
                q.append(c)

        # print('q=%s' % q)

        visited = set()

        while q:
            c = q.pop()
            # print('c=%s' % c)
            visited.add(c)
            L.append(c)
            if c in deplist:
                for dc in deplist[c]:
                    indegrees[dc] -= 1
                    if indegrees[dc] == 0:
                        q.append(dc)

        # print('L=%s' % L)
        # print('visited=%s' % visited)
        return len(visited) == numCourses


def main():
    sol = Solution()
    assert sol.canFinish(2, [[1,0]]) is True, 'fails'

    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False, 'fails'

if __name__ == '__main__':
   main()