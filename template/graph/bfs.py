from collections import deque

"""
Generic BFS traverse template
"""
def bfs(graph, start, target):
    q = deque([start])
    seen = set([start])

    while q:
        u = q.popleft()
        # do something with each node
        # print(u)
        if u == target:
            return
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)


"""
shortest path by BFS level order
"""

def bfs(graph, start, target):
    queue = deque([start])
    seen = set([start])
    depth = 0

    while queue:
        for _ in range(len(queue)):
            u = queue.popleft()
            if u == target:
                return depth
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        depth += 1

"""
generic BFS shortest path (slower than level order BFS)
"""

def bfs(graph, start, target):
    q = deque([(start, 0)]) # start node, and steps from start node
    seen = set([start])

    while q:
        u, step = q.popleft()
        # do something with each node
        # print(cur)
        if u == target:
            return step
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                q.append((v, step+1))

