## Strongly Connected Components
- connected components
- strongly connected: A directed graph is called strongly connected if there is a path in each direction between each pair of vertices of the graph. That is, a path exists from the first vertex in the pair to the second, and another path exists from the second vertex to the first.
### number of connected components in undirected graph
#### DFS
- dfs from each unvisited nodes, traverse to all nodes it can visit but not visited yet. For each such start, we find one connected component.
### Articulation Points / Bridges
- bridge - an edge, whose removal will increase number of connected components
- articulation - an vertex, whose removal will increase number of connected components
- Tarjan's algorithm

### Tarjan's 算法找桥或割点
遍历一个点，指定唯一时间戳DFN[i]；指定改点向前追溯可追溯到最老时间戳LOW[i]；
枚举当前点的所有边，若DFN[j]=0表明未被搜索过（这儿0、-1等都是可以的，只要是自我约定好的，正常不使用的就可以，如下面算法中使用的NO_VISIT），递归搜索；
当DFN[i]不为0，则j被搜索过，这时判断是否在我们存储新建的栈中，且j的时间戳DFN[j]小于当前时间戳DFN[i]，可判定成环，将LOW[i]设定为DFN[j]；
若这个点LOW[i]和DFN[i]相等，则这个点是目前强连通分量的元素中在栈中的最早的节点；
出栈，将这个强连通分量全部弹出，保存。

bridge condition: id(e.from) < lowlink(e.to)
O(V(V+E)) => (one pass updating lowlink value) O(V+E)

pseudo code
g # graph adjlist
visited = set()
lowest = dict() # lowest timestamp cur node can reach
bridges = []

def dfs(cur, parent, curtime)
    visited.add(cur)
    lowest[cur] = curtime
    for n in g[cur]:
        if n == parent: continue # dont' go back to parent
        if nei not in visited:
            dfs(nei, cur, curtime+1)
        lowest[cur] = min(lowest[cur], lowest[nei]) # update lowest timestamp reachable from child if lower timestamp found
        if curtime < lowest[nei]: # if curtime smaller than lowest timestamp nei can reach, we found a bridge
            bridges.append((cur, nei))

dfs(0, -1, 0)

Condition for Articulation Points:
case 1: non-root node, curtime < lowest[nei]
or
case 2: root node with >= 2 children

Condition for bridge:
  curtime < lowest[nei]

- Kosaraju’s algorithm