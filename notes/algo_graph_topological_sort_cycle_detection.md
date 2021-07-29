## Detect Cycle in graph
### undirected graph 无向图找环
使用拓扑排序可以判断一个无向图中是否存在环，具体步骤如下：

求出图中所有结点的度。
将所有度 <= 1 的结点入队。（独立结点的度为 0）
当队列不空时，弹出队首元素，把与队首元素相邻节点的度减一。如果相邻节点的度变为一，则将相邻结点入队。
循环结束时判断已经访问的结点数是否等于 n。等于 n 说明全部结点都被访问过，无环；反之，则有环。

### directed graph 有向图找环

使用拓扑排序判断无向图和有向图中是否存在环的区别在于：

在判断无向图中是否存在环时，是将所有 入度 <= 1 的结点入队；
在判断有向图中是否存在环时，是将所有 入度 = 0 的结点入队。

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

2. PostOrder DFS traverse with path to return topological sort result
从任一个未访问过的节点开始做DFS遍历，如果在某个支路遍历过程中（还没有到出度为0的点），遇到了任何一个在这条支路中已经访问过的节点，那就判断成环。注意不是“遇到任何已经访问过的节点”。
如何区分在这条支路中已经访问过的节点，和任何已经访问过的节点？需要两种不同方法标记已经访问过的节点。在某个支路访问中第一次遇到某个未访问过的节点，标记为2，如果遇到已经标记为2的节点，则表示有环。如果到达支路末端（出度为0的节点），都没有遇到标记为2的节点，则回溯返回，同时标记遇到的节点为1（以后任何其他访问遇到标记为1 的节点可以直接返回，因为标记1 的节点后面是死胡同，没有环）。如果能成功返回到起点，则此支路没有环。
    visited = set()
    res = []
    def postorder_dfs(curr, path)
        nonlocal nums, res, visited
        if len(path) == len(nums):
            res = path
        if curr in visited:
            return True
        else:
            if curr in path:
                return False
            else:
                for next in adj_list[cur]:
                    if postorder_dfs(next, path=[curr]) is False:
                        return False
                visited.add(curr)
                return True

    for curr in nums:
        if postorder_dfs(curr) is False:
        break

    return res

3. BFS (topological sort)
 BFS核心是拓扑排序。就是遍历图中所有节点，寻找入度为0的节点cur，处理其指向节点(dependencies)（减少其入度，加入queue）,然后把节点cur从queue弹出，同时记录当前cur为处理过。当遍历结束，应该是所有节点都处理过（count == len(numCourses），否则即可判断有环。

*BFS topological sort algorithm
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

    BFS sample code

        adj_list = collections.defaultdict(list) # adjacency list
        indegree = collections.defaultdict(int) # indegree

        for s, t in prerequisites:
            if t not in adj_list[s]: # avoid adding this edge twice if there possible duplicates in prerequisites
                adj_list[s].append(t)
                indegree[t] += 1

        sources = collections.defaultdict(int) # all possible sources (indegree == 0)
        for num in nums:
            if indegree[num] == 0:
                sources.append(num)

        nums_sorted = list()
        while sources:
            node = sources.pop()
            nums_sorted.append(node)
            for child in adj_list[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)

        # method 1 to check circle
        if len(nums_sorted) == len(nums):
            return nums_sorted
        else:
            return [] # cycle detected

        # method 2 to check circle
        if sum(indegree) == 0:
            print('no circle')