"""
DFS generic recursive template
"""
def dfs(graph, cur, target, visited):
    # do something
    if cur == target:
        return True
    for v in graph[cur]:
        if v not in visited:
            visited.add(v)
            if dfs(graph, v):
                return True

    # not found
    return False

graph = [[1, 2], [0, 2], [0, 1]] # adjacency list
dfs(graph, 0)

"""
DFS iterative template
"""
def dfs(adj_list, start, target):
    visited = set()
    stack = [start]
    while stack:
        cur = stack.pop()
        # do something
        # print(cur)
        # if cur == target:
        #     return True
        for neighbor in adj_list[cur]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)