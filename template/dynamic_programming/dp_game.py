"""
你和你的朋友面前有一排石头堆，用一个数组 piles 表示，piles[i] 表示第 i 堆石子有多少个。你们轮流拿石头，一次拿一堆，但是只能拿走最左边或者最右边的石头堆。所有石头被拿完后，谁拥有的石头多，谁获胜。

状态有三个：开始的索引 i，结束的索引 j，当前轮到的人。

dp[i][j][0] := max score for player 0 from piles[i...j] <= 先手
dp[i][j][1] := max score for player 1 from piles[i...j] <= 后手

穷举

n = piles.length
for 0<= i < n:
    for j <= i < n:
        for who in [0, 1]:
            dp[i][j][who] = max(left, right)

状态转移方程：

dp[i][j][0] = max (选择左边石头堆， 选择右边石头堆)
            = max(left, right)
where left = piles[i] + dp[i+1][j][1] # player 0 max score from piles[i...j] when picks left
      right = piles[j] + dp[i][j-1][1] # player 0 max score from piles[i...j] when picks right
如果player0选择左边，那player1就变成先手facing piles[i+1...j] => dp[i][j][1] = dp[i+1][j][0]
如果player0选择右边，那player1就变成先手 facing piles[i,...,j-1] => dp[i][j][1] = dp[i][j-1][0]

base case
如果只有一堆石头，那player0 get piles[i]，player1 get 0
dp[i][i][0] = piles[i]
dp[i][i][1] = 0

"""
