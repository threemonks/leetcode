"""
1871. Jump Game VII
Medium

37

2

Add to List

Share
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.



Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3.
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false


Constraints:

2 <= s.length <= 10^5
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
"""
from collections import deque

"""
区间DP

dp[i] := can we get to point i 
from i to j if s[j] == '0' and 
  i + minJump <= j <= min(i + maxJump, s.length - 1)
  and s[i] == 0

from j to i if s[i] =='0'
  j+minJump <= i <= min(j+maxJump, n-1)
   max(i-maxJump, 0) <= j <= i-minJump

base case
dp[0] = True
all dp[i] = False, where s[i] == '1' 

TLE

time O(N^2)
"""
class Solution0:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if '1' not in set(s):
            return True

        if s[-1] == '1':
            return False

        n = len(s)

        dp = [False] * (n)
        dp[0] = True

        for i in range(1, n):
            if s[i] == '0':
                #max(i-maxJump, 0) <= j <= i-minJump
                # print('%s, %s' % (max(i-maxJump, 0), min(max(i-minJump, 0), n-1)+1))
                dp[i] = any([dp[j] for j in range(max(i-maxJump, 0), min(max(i-minJump, 0), n-1)+1)])

        return dp[n-1]

#         # recursive/ top down TLE
#         @lru_cache(None)
#         def dp(i):
#             # print('i=%s' % i)
#             if s[i] == '1':
#                 return False
#             if i == n-1 and s[i] == '0':
#                 return True
#             for j in range(min(i+maxJump, n-1), i+minJump-1, -1):
#                 # print('j=%s' % j)
#                 if s[j] == '0' and dp(j):
#                     return True

#             return False

#         return dp(0)

"""
DP + PrefixSum
Given DP O(N^2) TLE, we need to find better solution.

Obseration
to get dp[i], we need to find if any of dp[i-maxJump] to dp[i-minJump] is true, or if sum(dp[i-maxJump:i-minJump+1]) > 0
就是要找dp[i-maxJump] 到dp[i-minJump]间有至少一个>0，就是要求区间和sum(dp[i-maxJump:i-minJump+1])>0，区间和可以转换为前缀和之差，就是

sum(dp[i-maxJump:i-minJump+1]) = presum[i-minJump] - presum[i-MaxJump-1]

"""

class Solution1:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0]*(n+1) # index 0 is dummy value
        presum = [0]*(n+1) # index 0 is dummy value

        dp[1] = 1
        presum[1] = 1
        for i in range(1, n+1):
            if s[i-1] == '0' and i-minJump-1 >= 0:
                l, r = max(1, i-maxJump), i-minJump
                if presum[r] - presum[l-1] > 0:
                    dp[i] = 1
            presum[i] = presum[i-1] + dp[i]

        return dp[n]

"""
BFS with early pruning

since regular BFS would be O(N^2), 10^5 would result in TLE. 

We realize that this solution is O(n^2) since maxJump-minJump can be as big as n. But actually, we are close to the solution: notice that we are repeatedly adding in indices that have been visited.

For example, consider s = "0100000", minJumps = 2, maxJumps = 6. After the first iteration, we have already put all the relevant indices into the queue. When we visit index 2, we can start adding the next reachable indices from where the last iteration leftoff. I keep track of where to start with the max_reached variable.

https://leetcode.com/problems/jump-game-vii/discuss/1224681/Python3-Thinking-process-no-DP-needed

without start = max(max_reach, cur+minJump), we are doing O(E)~O(V^2), with start = max(max_reach, cur+minJump), we achieve O(E) ~O(V) because each node is checked and enqueued just once.

time O(|V|+|E|)
"""
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])

        seen = set([0])
        max_reached = 0
        while q:
            cur = q.popleft()
            if cur == n-1:
                return True
            # we can skip any node before max_reached, since we can already reach max_reached from previous steps
            start = max(cur+minJump, max_reached)
            for i in range(start, min(cur+maxJump+1, n)):
                if i not in seen and s[i] == '0':
                    q.append(i)
                    seen.add(i)
            max_reached = cur + maxJump

        return False

def main():
    sol = Solution()
    assert sol.canReach(s = "011010", minJump = 2, maxJump = 3) == True, 'fails'

    assert sol.canReach(s = "01101110", minJump = 2, maxJump = 3) == False, 'fails'


if __name__ == '__main__':
   main()