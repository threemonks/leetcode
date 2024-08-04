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

    # we could use visited/seen instead of discovered, for which we only add into visited after the node comes out of the queue, which is when it is processed

### DFS for tree vs graph (possible with circle)
When using DFS for a tree, which is a graph without circle, we can just keep track of the previous node the current visiting is coming from, instead of keep track of a visited set