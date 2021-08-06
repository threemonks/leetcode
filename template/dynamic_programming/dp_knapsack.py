"""
https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485064&idx=1&sn=550705eb67f5e71487c8b218382919d6&chksm=9bd7f880aca071962a5a17d0f85d979d6f0c5a5ce32c84b8fee88e36d451f9ccb3bb47b88f78&scene=21#wechat_redirect

DP 普通模板

for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 择优(选择1，选择2...)
"""
from typing import List

"""
DP 0/1背包

dp[i][w]的定义如下：对于前i个物品，当前背包的容量为w，这种情况下可以装的最大价值是dp[i][w]

最终答案就是dp[N][W]。
base case 就是dp[0][..] = dp[..][0] = 0，因为没有物品或者背包没有空间的时候，能装的最大价值就是 0。

细化上面的框架：
int dp[N+1][W+1]
dp[0][..] = 0
dp[..][0] = 0

for i in [1..N]:
    for w in [1..W]:
        dp[i][w] = max(
            把物品 i 装进背包,
            不把物品 i 装进背包
        )
return dp[N][W]

for i in [1..N]:
    for w in [1..W]:
        dp[i][w] = max(
            dp[i-1][w], # 没有把这第i个物品装入背包
            dp[i-1][w - wt[i-1]] + val[i-1] # 把这第i个物品装入了背包
        )
return dp[N][W]

"""

class Solution:
    def knapsack(self, W: int, N: int, wt: List[int], val:List[int]):
        # init condition / base case set
        # dp[0][j] = 0 # no item allowed
        # dp[i][0] = 0 # no knapsack space allowed
        dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

        for i in range(1, N+1):
            for w in range(1, W+1):
                if w-wt[i-1] < 0:
                    # knapsack capacity not enough for this item 背包容量不足，不能装入第 i 个物品
                    dp[i][w] = dp[i-1][w]
                else:
                    # use this item or not, pick max 第i个物品装入或不装入背包
                    dp[i][w] = max(dp[i-1][w-wt[i-1]] + val[i-1], # use this item, wt and val is 0-indexed array
                                   dp[i-1][w] # do not use
                                   )

        return dp[N][W]

"""
DP 背包子集

416. Partition Equal Subset Sum
416. 分割等和子集 

给一个可装载重量为sum/2的背包和N个物品，每个物品的重量为nums[i]。现在让你装物品，是否存在一种装法，能够恰好将背包装满？

https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485103&idx=1&sn=8a9752e18ed528e5c18d973dcd134260&chksm=9bd7f8a7aca071b14c736a30ef7b23b80914c676414b01f8269808ef28da48eb13e90a432fff&scene=21#wechat_redirect

dp[i][j] = x表示，对于前i个物品，当前背包的容量为j时，若x为true，则说明可以恰好将背包装满，若x为false，则说明不能恰好将背包装满。

最终答案就是dp[N][sum/2]，base case 就是dp[..][0] = true和dp[0][..] = false，因为背包没有空间的时候，就相当于装满了，而当没有物品可选择的时候，肯定没办法装满背包。

}
"""
class Solution:
    def canPartition(self, nums):
        sums = sum(nums)
        if sums % 2 != 0: # odd sum cannot be equally divided
            return False
        n = len(nums)
        sums //= 2
        dp = [[0 for _ in range(n+1)] for _ in range(sums+1)]

        # base case
        for i in range(n+1):
            dp[i][0] = True # sums to zero, can be achieved by choosing no item

        for i in range(1, n+1):
            for j in range(1, sums+1):
                if j-nums[i-1] < 0:
                    # not enough knapsack capacity to add i-th item 背包容量不足，不能装入第 i 个物品
                    dp[i][j] = dp[i-1][j]
                else:
                    # use or not use i-th item 第i个物品装或不装入背包
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]

        return dp[n][sums]

"""
背包子集问题 状态压缩
2-D dp array -> 1-D dp array

bool canPartition(vector<int>& nums) {
    int sum = 0, n = nums.size();
    for (int num : nums) sum += num;
    if (sum % 2 != 0) return false;
    sum = sum / 2;
    vector<bool> dp(sum + 1, false);
    // base case
    dp[0] = true;

    for (int i = 0; i < n; i++) 
        for (int j = sum; j >= 0; j--) 
            if (j - nums[i] >= 0) 
                dp[j] = dp[j] || dp[j - nums[i]];

    return dp[sum];
}

这就是状态压缩，其实这段代码和之前的解法思路完全相同，只在一行dp数组上操作，i每进行一轮迭代，dp[j]其实就相当于dp[i-1][j]，所以只需要一维数组就够用了。

唯一需要注意的是j应该从后往前反向遍历，因为每个物品（或者说数字）只能用一次，以免之前的结果影响其他的结果。

"""

class Solution:
    def canPartition(self, nums):
        sums = sum(nums)
        if sums % 2 != 0: # odd sum cannot be equally divided
            return False
        n = len(nums)
        sums //= 2
        dp = [0 for _ in range(sums+1)]

        # base case
        dp[0][0] = True # sums to zero, can be achieved by choosing no item

        for i in range(1, n+1):
            for j in range(sums+1, -1, -1): # j loop backwards, to ensure dp[i][j] for smaller j not being impacted by those of dp[i][j] for larger j from previous i-1 th run
                if j-nums[i-1] > 0:
                    # use or not use i-th item 第i个物品装或不装入背包
                    dp[j] = dp[j] | dp[j-nums[i-1]]

        return dp[n][sums]

"""
完全背包问题

有一个背包，最大容量为amount，有一系列物品coins，每个物品的重量为coins[i]，每个物品的数量无限。请问有多少种方法，能够把背包恰好装满？

leetcode 518 coin change 2

dp[i][j]的定义如下：
若只使用前i个物品，当背包容量为j时，有dp[i][j]种方法可以装满背包。

若只使用coins中的前i个硬币的面值，若想凑出金额j，有dp[i][j]种凑法。

base case 为dp[0][..] = 0， dp[..][0] = 1

答案就是dp[N][amount]，其中N为coins数组的大小。

int dp[N+1][amount+1]
dp[0][..] = 0
dp[..][0] = 1

for i in [1..N]:
    for j in [1..amount]:
        把物品 i 装进背包,
        不把物品 i 装进背包
return dp[N][amount]

for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= amount; j++) {
        if (j - coins[i-1] >= 0)
            dp[i][j] = dp[i - 1][j]  # 不把这第i个物品装入背包，不使用coins[i-1]这个面值的硬币，
                     + dp[i][j-coins[i-1]] # 把这第i个物品装入了背包，使用coins[i-1]这个面值的硬币 (i-th)
return dp[N][amount]

int change(int amount, int[] coins) {
    int n = coins.length;
    int[][] dp = amount int[n + 1][amount + 1];
    // base case
    for (int i = 0; i <= n; i++) 
        dp[i][0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= amount; j++)
            if (j - coins[i-1] >= 0)
                dp[i][j] = dp[i - 1][j] 
                         + dp[i][j - coins[i-1]];
            else 
                dp[i][j] = dp[i - 1][j];
    }
    return dp[n][amount];
}
"""

class Solution:
    def change(self, amount: int, coins: List[int]):
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]

        # base case
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(n+1):
            for j in range(1, amount+1):
                if j-coins[i-1] >= 0: # coins[i-1] is for i-th run since coins is 0-indexed
                    dp[i][j] = dp[i-1][j] \
                                + dp[i][j-coins[i-1]]
                else: # cannot use this coin not enough remaining amount
                    dp[i][j] = dp[i - 1][j]

        return dp[n][amount]