# Greedy
## Greedy problems in general

Greedy problems usually look like "Find minimum number of something to do something" or "Find maximum number of something to fit in some conditions", and typically propose an unsorted input.

The idea of greedy algorithm is to pick the locally optimal move at each step, that will lead to the globally optimal solution.

## 适用条件
最优子结构、无后效性和贪心选择性
“贪心选择性”的意思是，通过局部最优的选择，能产生全局的最优选择。

##  Popular greedy algorithms

* Dijkstra’s Shortest Path
* Kruskal’s Minimum Spanning Tree (MST)
* Prim's Minimum Spanning tree
* Huffman Coding

## Greedy vs DP
都需要满足无后效性、最优子结构性质。
区别：
- greedy - local optimization
- dp - global optimization

|         | Common      | 贪心法              | DP                             |
|:--------|:------------|:--------------------|:-------------------------------|
| 适用条件 |             | 最优子结构、无后效性和贪心选择性 | 最优子结构、无后效性和重复子问题 |
| 最优     |             | 局部最优            | 全局最优                       |

## 贪心、分治、回溯和动态规划
四种算法思想比较分析
下面我们分析下已经学过的四种算法思想——贪心、分治、回溯和动态规划，看它们之间有什么区别和联系。

若将这四种算法思想分一下类，那么贪心、回溯、动态规划可以归为一类，而分治单独可以作为一类。因为前三个算法解决问题的模型，都可以抽象成本节的多阶段决策最优解模型，而分治算法解决的问题尽管大部分也是最优解问题，但是，大部分都不能抽象成多阶段决策模型。

回溯算法是个“万金油”。基本上能用的动态规划、贪心解决的问题，都可以用回溯算法解决。回溯算法相当于穷举搜索。穷举所有的情况，然后对比得到最优解。不过，回溯算法的时间复杂度非常高，是指数级别的，只能用来解决小规模数据的问题。对于大规模数据的问题，用回溯算法解决的执行效率就很低了。

尽管动态规划比回溯算法高效，但是，并不是所有问题，都可以用动态规划来解决。能用动态规划解决的问题，需要满足三个特征，最优子结构、无后效性和重复子问题。在重复子问题这一点上，动态规划和分治算法的区分非常明显。分治算法要求分割成的子问题，不能有重复子问题，而动态规划正好相反，动态规划之所以高效，就是因为回溯算法实现中存在大量的重复子问题。

贪心算法实际上是动态规划算法的一种特殊情况。它解决问题起来更加高效，代码实现也更加简洁。不过，它可以解决的问题也更加有限。它能解决的问题需要满足三个条件，最优子结构、无后效性和贪心选择性（这里我们不怎么强调重复子问题）。其中，最优子结构、无后效性跟动态规划中的无异。“贪心选择性”的意思是，通过局部最优的选择，能产生全局的最优选择。每一个阶段，我们都选择当前看起来最优的决策，所有阶段的决策完成之后，最终由这些局部最优解构成全局最优解。