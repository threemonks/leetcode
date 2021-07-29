## DFS

### recursive DFS
  def recursive_dfs(cur, discovered):  
    discovered.add(cur)
    for all connected neighbors g of cur:
        if g not in discovered:
            recursive_dfs(g, discovered)

### iterative DFS
  def iterative_dfs(G, v):
      # graph, starting vertex
      stack = [v]
      discovered = set(v)

      while stack:
            cur = stack.pop()
            for all neighbors g of cur:
                if g not in discovered:
                    stack.append(g)
                    discovered.add(g)                                            
