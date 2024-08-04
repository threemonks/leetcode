# When/Where to use each technique / algorithm
## Knapsack problem
## Heap
* if we need to sort input, but we only need to use min or max, not the entire sorted list
* if we need to find or use min/max

## Binary search
* sorted data, or no idea just random guess
* if predicate function is monotonic: if x < k, f(x) is False, and for all x>=k, f(x) is True, or vice versa
* searching for some min/max value satisfying some condition/predicate, within some search space, if the predicate is mononotic, i.e., if x<k, then f(x) is False, and for all x>=k, f(x) = True

## Graph problem BFS or DFS?
* backtracking -> dfs
* shortest path -> bfs
* tree level ordering -> bfs
* finding any component -> dfs
* cycle detection can be either DFS or BFS
** non-direction use BFS

## Greedy
    * choose locally optimal leads to global solution
    * usually has the following two properties:
    **Greedy Choice Property
    ** Optimal Substructure

## Dynamic Programming    recursive solution that has repeated calls for the same inputs,
    * subproblem are overlapping
    * subproblems are dependent on earlier subproblems
    * but one previous subprolbems are solved, later ones do not affect previous ones
    * store solution of subproblem
    * bottom up and top down

## Divide and Conquer    solve problem by dividing problems into subproblems
    * subproblems are NOT dependent on each other
    * do not store solution of subproblem
    * top down

## 算法设计策略中
* 和扫描法有关的，常常包括
    * 前缀和与差分
    * 前缀最大值，最小值维护

* 和单调性有关的，常常包括
    * 单调队列与单调栈
    * 滑动窗口，双指针
    * 二分