from collections import deque

"""
Generic BFS template
"""
def bfs(graph, start, target):
    q = deque([start])
    discovered = set([start])

    while q:
        cur = q.popleft()
        # do something with each node
        # print(cur)
        # if cur == target:
        #     return True
        for u in graph[cur]:
            if u not in discovered:
                discovered.add(u)
                q.append(u)


"""
BFS level order
"""

def bfs(graph, start, target):
    q = deque([start])
    discovered = set([start])

    while q:
        l = len(q)
        newq = [] # all new nodes gathered after exploring this level
        while l:
            cur = q.popleft()
            # do something with each node
            # print(cur)
            # if cur == target:
            #     return True
            for u in graph[cur]:
                if u not in discovered:
                    discovered.add(u)
                    newq.append(u)
            l -= 1
        # now append all of newq into q
        for i in newq:
            q.append(i)

"""
BFS shortest path
"""

def bfs(graph, start, target):
    q = deque([(start, 0)]) # start node, and steps from start node
    discovered = set([start])

    while q:
        cur, step = q.popleft()
        # do something with each node
        # print(cur)
        # if cur == target:
        #     return step
        for u in graph[cur]:
            if u not in discovered:
                discovered.add(u)
                q.append((u, step+1))

