## DP
1. 状态定义，主要是看两点，如何表示剩余物品，状态的含义是true/false还是价值
2. 初始化，因为这里我们都使用递归解决，所以初始化都在递归里了，这里不用考虑
3. 状态转移方程，参考strategy is the best, luck is the worst
4. return 结果

## Game
### 策梅洛定理
策梅洛定理（Zermelo's theorem）。定理表示在任何有限二人交替参与的没有运气成分的完美信息（perfect information）博弈中，要么有一方有必胜策略，要么双方有必不败策略（平局）

- strategy is the best, luck is the worst

## Knapsack problem: find the best solution
Basic idea:
* keep track of the weight and keep track of the best total value ("score")
* loop over all items, adding value to the knapsack, and substracting the weight of items from the total weight allowed
* if the weight goes below zero, we have too many items, stop exploring this path

