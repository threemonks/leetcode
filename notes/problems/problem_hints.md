## Array - Sliding Window
    1. 处理连续的，subarray，而不是subsequence
    2. 题目要求的跟window长度直接相关 => 用sliding window 而不是DP
        1. window state用什么记录
        2. shrink的条件是什么
        3. window需要满足的条件是什么
    3. Ask for Minimum, Maximum, Longest, Shortest, K-sized   

## Array - Intervals
    1 Overlap 和 Merge
    2 Overlapping Interval List
        time as x-axis
        1. 首先sort所有的interval，维护一个window变量代表当前所求的时间窗口，然后每个interval的开始和结束，要么close当前的window新建一个新window，要么是延伸当前的window或推迟将来的window。
        2. 首先sort所有的interval，将每个interval拆解成两个event，这些event会影响整个program的某些状态，比如 overlap_count，然后按照时间序遍历所有event，根据event来open和close window，然后判断window和状态变量是否满足所需的条件。

## 题目要求的暗示 problem hints：
1. 求解的个数number of ways/arrangements/choices => DP
2. 返回所有的解 print all possible ways / arrangements / choices => backtrack / DFS
3. 滑动窗口最大值 单调栈
4. 任意区间最大值 线段树
5. 前缀子数组最大值， 用辅助数组记录可以简化求最大值时间复杂度O(1) <= 最长公共上升子序列

## 由数据范围反推算法复杂度以及算法内容
  https://www.acwing.com/blog/content/32/
一般ACM或者笔试题的时间限制是1秒或2秒。
在这种情况下，C++代码中的操作次数控制在 107∼108107∼108 为最佳。

下面给出在不同数据范围下，代码的时间复杂度和算法该如何选择：

- n≤30, 指数级别, dfs+剪枝，状态压缩dp
- n≤100 => O(n3)，floyd，dp，高斯消元
- n≤10^3 => O(n2)，O(n2logn)O(n2logn)，dp，二分，朴素版Dijkstra、朴素版Prim、Bellman-Ford
- n≤10^4 => O(n∗n)，块状链表、分块、莫队
- n≤10^5 => O(nlogn) => 各种sort，线段树、树状数组、set/map、heap、拓扑排序、dijkstra+heap、prim+heap、spfa、求凸包、求半平面交、二分、CDQ分治、整体二分
- n≤10^6 => O(n), 以及常数较小的 O(nlogn)O(nlogn) 算法 => 单调队列、 hash、双指针扫描、并查集，kmp、AC自动机，常数比较小的 O(nlogn)O(nlogn) 的做法：sort、树状数组、heap、dijkstra、spfa
- n≤10^7 => O(n)，双指针扫描、kmp、AC自动机、线性筛素数
- n≤10^9 => O(n)，判断质数
- n≤10^18 => O(logn)，最大公约数，快速幂
- n≤10^1000 => O((logn)2)，高精度加减乘除
- n≤10^100000 => O(logk×loglogk)，k表示位数，高精度加减、FFT/NTT

## 位异或 XOR
- if only interested in even position or odd position, maybe use xor, since x^x^x = x