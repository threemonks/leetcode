## 动态规划
要求适用 ： 最优子结构、无后效性和重复子问题
https://www.zdaiot.com/DataStructureAlgorithm/40%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%90%86%E8%AE%BA%EF%BC%9A%E4%B8%80%E7%AF%87%E6%96%87%E7%AB%A0%E5%B8%A6%E4%BD%A0%E5%BD%BB%E5%BA%95%E6%90%9E%E6%87%82%E6%9C%80%E4%BC%98%E5%AD%90%E7%BB%93%E6%9E%84%E3%80%81%E6%97%A0%E5%90%8E%E6%95%88%E6%80%A7%E5%92%8C%E9%87%8D%E5%A4%8D%E5%AD%90%E9%97%AE%E9%A2%98/

### 一个模型三个特征 - 理论讲解
什么样的问题适合用动态规划来做，其实这有一套成熟的理论，叫作”一个模型三个特征“理论。
一个模型理论指的是动态规划适合解决的问题的模型。这个模型可以定义为”多阶段决策最优解模型“。我们一般是用动态规划来解决最优问题。而解决问题的过程，需要经历多个决策阶段，每个决策阶段都对应着一组状态。然后需要寻找一组决策序列，经过这组决策序列，能够产生最终期望求解的最优值。

”三个特征“分别为最优子结构、无后效性和重复子问题。下面对这三个概念详细解释一下。
#### 最优子结构
最优子结构指的是，问题的最优解包含子问题的最优解。反过来说就是，可以通过子问题的最优解，推导出问题的最优解

#### 无后效性
无后效性有两层含义，第一层含义是，在推导后面阶段的状态的时候，只关心前面阶段的状态值，不关心这个状态是怎么一步一步推导出来的。第二层含义是，某阶段状态一旦确定，就不受之后阶段的决策影响。

#### 重复子问题
不同的决策序列，到达某个相同的阶段时，可能会产生重复的状态。

## DP分类
https://zhuanlan.zhihu.com/p/126546914
1. 线性DP
- 最经典单串：
  - 300\. 最长上升子序列 (LIS)
- 最经典双串：
  - 1143\. 最长公共子序列 (LCS)
- 经典问题：
  - 120\. 三角形最小路径和
  - 53\. 最大子序和
  - 152\. 乘积最大子数组
  - 887\. 鸡蛋掉落 (DP+二分)
  - 354\. 俄罗斯套娃信封问题 (隐晦的LIS)
- 打家劫舍系列: (打家劫舍3 是树形DP)
  - 198\. 打家劫舍
  - 213\. 打家劫舍 II
- 股票系列:
  - 121\. 买卖股票的最佳时机
  - 122\. 买卖股票的最佳时机 II
  - 123\. 买卖股票的最佳时机 III
  - 188\. 买卖股票的最佳时机 IV
  - 309\. 最佳买卖股票时机含冷冻期
  - 714\. 买卖股票的最佳时机含手续费
- 字符串匹配系列
  - 72\. 编辑距离
  - 44\. 通配符匹配
  - 10\. 正则表达式匹配
2. 区间DP
- 516\. 最长回文子序列
- 730\. 统计不同回文子字符串
- 1039\. 多边形三角剖分的最低得分
- 664\. 奇怪的打印机
- 312\. 戳气球
3. 背包DP
- 416\. 分割等和子集 (01背包-要求恰好取到背包容量)
- 494\. 目标和 (01背包-求方案数)
- 322\. 零钱兑换 (完全背包)
- 518\. 零钱兑换 II (完全背包-求方案数)
- 474\. 一和零 (二维费用背包)
4. 树形DP
- 124\. 二叉树中的最大路径和
- 1245\. 树的直径 (邻接表上的树形DP)
- 543\. 二叉树的直径
- 333\. 最大 BST 子树
- 337\. 打家劫舍 III
5. 状态压缩DP
- 464\. 我能赢吗
- 526\. 优美的排列
- 935\. 骑士拨号器
- 1349\. 参加考试的最大学生数
6. 数位DP
- 233\. 数字 1 的个数
- 902\. 最大为 N 的数字组合
- 1015\. 可被 K 整除的最小整数
7. 计数型DP
   计数型DP都可以以组合数学的方法写出组合数，然后dp求组合数
- 62\. 不同路径
- 63\. 不同路径 II
- 96\. 不同的二叉搜索树 (卡特兰数)
- 1259\. 不相交的握手 (卢卡斯定理求大组合数模质数)
8. 递推型DP
   所有线性递推关系都可以用矩阵快速幂做，可以O(logN)，最典型是斐波那契数列
- 70\. 爬楼梯
- 509\. 斐波那契数
- 935\. 骑士拨号器
- 957\. N 天后的牢房
- 1137\. 第 N 个泰波那契数
9. 概率型DP
   求概率，求数学期望
- 808\. 分汤
- 837\. 新21点
10. 博弈型DP
-  strategy is the best, luck is the worst
-  策梅洛定理，SG定理，minimax
- 翻转游戏
  - 293\. 翻转游戏
  - 294\. 翻转游戏 II
- Nim游戏
  - 292\. Nim 游戏
- 石子游戏
  - 877\. 石子游戏
  - 1140\. 石子游戏 II
- 井字游戏
  - 348\. 判定井字棋胜负
  - 794\. 有效的井字游戏
  - 1275\. 找出井字棋的获胜者
11. 记忆化搜索
    本质是 dfs + 记忆化，用在状态的转移方向不确定的情况
- 329\. 矩阵中的最长递增路径
- 576\. 出界的路径数

youtube seminar from wisdompeak
https://www.youtube.com/watch?v=FLbqgyJ-70I&list=PL4eek-kYmeR1H9vbuzxtf9lJb3TVW-obm&index=5

slides from this google doc:
https://docs.google.com/presentation/d/1F_Qp3kzw7jZkPpb7ll7J6-02285bCA3Z9nmU1e7a2rk/edit#slide=id.g8285dd8f3f_1_512

## DP适用问题： 能将大问题拆成几个小问题，且满足无后效性、最优子结构性质。

## DP wisdompeak 分类

1. DP坐标型：

1. 第I类基本型DP（“时间序列”型）/线性DP
    - dp[i][j]：表示第i-th轮的第j种状态 (j=1,2,...,K)
2. 第II类基本型（“时间序列”加强版）
    - dp[i]：表示第i-th轮的状态，一般这个状态要求和元素i直接有关。dp[i]与之前的状态dp[i’]产生关系(i=1,2,...,i-1) (比如sum, max, min)
3. 双序列型
    - dp[i][j]：表示针对s[1:i]和t[1:j]的子问题的求解。dp[i][j]往之前的状态去转移：dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
4. 区间型
4.1. 第I类区间型
    - dp[i][k]表示针对s[1:i]分成k个区间，此时能够得到的最优解。搜寻最后一个区间的起始位置j，将dp[i][k]分割成dp[j-1][k-1]和s[j:i]两部分。
4.2. 第II类区间型DP
    - dp[i][j]：表示针对s[i:j]的子问题的求解。dp[i][j]往小区间的dp[i’][j’]转移
5. 背包入门 Knapsack Problem
    - dp[i][c]：表示考虑只从前i件物品的子集里选择、代价为c的最大收益。c = 1,2,...,C。将dp[i][c]往dp[i-1][c’]转移：即考虑如何使用物品i，对代价/收益的影响
6. 状态压缩 （01背包）Knapsack Problem bit masking
    - 设计“状态”代表一个01向量（不超过32位），我们可以用一个整形的bit位来表示

***********
** DP套路(I): 第I类基本型（“时间序列”型）

给出一个序列（数组/字符串），其中每一个元素可以认为“一天”，并且“今天”的状态只取决于“昨天”的状态。
House Robber
Best Time to Buy and Sell Stocks
longest increasing subsequence (LIS ) => DP 序列型
...
套路：
定义dp[i][j]：表示第i-th轮的第j种状态 (j=1,2,...,K)
千方百计将dp[i][j]与前一轮的状态dp[i-1][j]产生关系(j=1,2,...,K)
最终的结果是dp[last][j]中的某种aggregation (sum, max, min …)

* To Do or Not To Do
很多不是那么套路的DP题，DP状态可能比较难设计。不过还是有套路可循。
某些题目给你一次“行使某种策略的权力”。联想到买卖股票系列的题，我们常会设计的两个状态就是“行使了权力”和“没有行使权力”分别对应的价值。

** DP套路(II): 第II类基本型（“时间序列”加强版）
给出一个序列（数组/字符串），其中每一个元素可以认为“一天”：但“今天”的状态 和之前的“某一天”有关，需要挑选。
longest common subsequence (LCS) => DP 双序列型
套路：
定义dp[i]：表示第i-th轮的状态，一般这个状态要求和元素i直接有关。
千方百计将dp[i]与之前的状态dp[i’]产生关系(i=1,2,...,i-1) (比如sum, max, min)
dp[i]肯定不能与大于i的轮次有任何关系，否则违反了DP的无后效性。
最终的结果是dp[i]中的某一个

** DP套路(III): 双序列型
给出两个序列s和t（数组/字符串），让你对它们搞事情。
Longest Common Subsequences
Shortest Common Supersequence
Edit distances
...
套路：
定义dp[i][j]：表示针对s[1:i]和t[1:j]的子问题的求解。
千方百计将dp[i][j]往之前的状态去转移：dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
最终的结果是dp[m][n]

* LCS/SCS的变种：换汤不换药
LC 583. Delete Operation for Two Strings
问：从字符串s和t中总共最少删除多少个字符能使得它们相等。
LC 712. Minimum ASCII Delete Sum for Two Strings
问：从字符串s和t中总共最少删除多少ASCII码值的字符能使得它们相等。
LC 1035. Uncrossed Lines
两个数组s和t之间相等的数字可以连线。连线不能交叉。问最多可以有几条连线。
LC 1216. Valid Palindrome III
问一个字符串s最少删除多少个字符能变成回文串。
LC 1312. Minimum Insertion Steps to Make a String Palindrome
问一个字符串s最少需要添加多少个字符能变成回文串。

T = S[:-1]
S

** DP套路(IV): 第I类区间型DP
给出一个序列，明确要求分割成K个连续区间，要你计算这些区间的某个最优性质。
套路：
状态定义：dp[i][k]表示针对s[1:i]分成k个区间，此时能够得到的最优解
搜寻最后一个区间的起始位置j，将dp[i][k]分割成dp[j-1][k-1]和s[j:i]两部分。
最终的结果是dp[N][K]

** DP套路(V): 第II类区间型DP
只给出一个序列S（数组/字符串），求一个针对这个序列的最优解。
适用条件：这个最优解对于序列的index而言，没有“无后效性”。即无法设计dp[i]使得dp[i]仅依赖于dp[j] (j<i). 但是大区间的最优解，可以依赖小区间的最优解。
套路：
定义dp[i][j]：表示针对s[i:j]的子问题的求解。
千方百计将大区间的dp[i][j]往小区间的dp[i’][j’]转移。
第一层循环是区间大小；第二层循环是起始点。
最终的结果是dp[1][N]

* 结合第I类和第II类区间型DP算法的Boss题：
LC 1000. Minimum Cost to Merge Stones
给一个数组代表N堆石头的重量。每步操作将K堆相邻的石头合并，代价是这K堆的重量和。问最少的代价将所有的石头堆合并到一起。
我们考虑将任意区间[i:j]归并到一起的最优解，取决于如何先最小代价地将[i:j]归并成K堆（即先分成K个subarray），然后再加sum[i:j]即可。于是提示我们需要结合两类区间型DP的套路：
dp[i][j][k]表示将区间[i:j]归并成k堆的最小代价。

** DP套路(VI): 背包入门
题型抽象：给出N件物品，每个物品可用可不用（或者有若干个不同的用法）。要求以某个有上限C的代价来实现最大收益。（有时候反过来，要求以某个有下限的收益来实现最小代价。）
套路：
定义dp[i][c]：表示考虑只从前i件物品的子集里选择、代价为c的最大收益。c = 1,2,...,C
千方百计将dp[i][c]往dp[i-1][c’]转移：即考虑如何使用物品i，对代价/收益的影响
第一层循环是物品编号i；
第二层循环是遍历“代价”的所有可能值。
最终的结果是 max {dp[N][c]}, for c=1,2,...,C

题型抽象：给出N件物品，每个物品可用可不用（或者有若干个不同的用法）。要求以某个有上限C的代价来实现最大收益。（有时候反过来，要求以某个有下限的收益来实现最小代价。）
背包问题的解法特点：
利用了物品次序的“无后效性”：我在前4件物品中做选择的最大收益，与第5件物品是啥没有关系。
“过去不依赖将来，将来不影响过去”
将原本题意的解空间（代表各种物品是否使用的高维向量），替换成了代价的解空间（是一个有上限C的标量）。压缩了复杂度。
[0,2,0,3,1,0,0,4]  => {10}

** 状态压缩
对于比较复杂的“状态”，DP经常会用到“状态压缩”的技巧。
比如：有些情况下如果想设计“状态”代表一个01向量（不超过32位），我们可以用一个整形的bit位来表示。
[1,0,1,1,0,0,1] => b1011001 => 89

***********
DP template
***********

** dp recusrive bitmask template

from functools import lru_cache
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m, n = len(req_skills), len(people)
        mapping = {v: i for i, v in enumerate(req_skills)} # skill to its index

        people_skill_masks = [0] * n # people id to its skill bit masks
        for i, p in enumerate(people):
            for skill in p:
                if skill in mapping:
                    people_skill_masks[i] |= (1<<mapping[skill]) # 0000 0010 | 0000 0001 => 0000 0011

        full_mask = (1<<m)-1

        @lru_cache(None)
        def dp(masks):
            if masks == full_mask: # base case
                return []

            ans = [0] * (n+1) # default is list of people, and want max, so use [0] * (n+1), similar to math.inf if ans is to look for number of people
            for i, psm in enumerate(people_skill_masks):
                nxt_mask = masks | psm
                if nxt_mask != masks:
                    ans = min(ans, [i] + dp(nxt_mask), key=len) # if we need number of people, 1+dp(nxt_mask), and would be just min, without define key func, but we are returning actual people list, so we are comparing number of people in the list to return least number of people

            return ans

        return dp(0) # would start from dp(full_mask) if we need to use subsets, then start with full_mask will make it easier to get and use subsets mask

** dp recursive and bitmask iterate through all substates
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])

        valid_seats = [0] * m  # n bits
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    valid_seats[i] |= (1 << j)

        @lru_cache(None)
        def dp(i, prev_mask):
            if i == m:
                return 0
            ans = 0
            mask = valid_seats[i]
            while mask >= 0:  # loop through all possible subsets of 1 bits combinations in mask, must include 0 (empty set), as some rows might have no students
                if mask & valid_seats[i] == mask and mask & (mask << 1) == 0 and prev_mask & (
                        mask << 1) == 0 and prev_mask & (mask >> 1) == 0:
                    ans = max(ans, bin(mask).count('1') + dp(i+1, mask))
                if mask == 0: # avoid infinite loop, as empty is always subset of empty
                    break
                mask = (mask - 1) & valid_seats[i]

            return ans

** dp recursive and bitmask iterate through all possible states

            for mask in range(1 << n): # iterate all possible masks, only use valid ones
                if mask & valid_seats[i] == mask:
                    if mask & (mask >> 1) == 0 and mask & (mask << 1) == 0 and prev_mask & (
                            mask >> 1) == 0 and prev_mask & (mask << 1) == 0:
                        ans = max(ans, bit_count(mask) + dp(i + 1, mask))

区间型DP (chen mei ling)

1. 自顶向下 dfs + memo
2. 先计算小区间

3. 换个方向
for i = n downto 1 do
 for j = i to n do
  f[i][j] = ...
 end for
end for