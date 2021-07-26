"""
664. Strange Printer
Hard

There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.

"""
from functools import lru_cache
from typing import List

"""
DP

idea:
1. first we can remove all consecutively repeating chars except for the first one, as they don't require extra turn to print

dp[i][j] := minimum turns needed to cover s[i:j] (inclusive)

for each letter s[k] between i and j, if s[k] == s[i], then s[k] can be printed in one turn when we print s[i], so we can reduce range dp[i][j] to dp[i][k-1] + dp[k+1][j] (divide into two sub ranges, and skip s[k] while dividing)

base case 
    if i == j
        dp = 1

time O(N^3)
space O(N^2)

"""

class Solution:
    def strangePrinter(self, S: str) -> int:
        if not S:
            return 0

        s = S[0]
        for c in S[1:]:
            if c != s[-1]:
                s += c

        @lru_cache(None)
        def dp(i, j):
            nonlocal s
            if i > j: return 0
            min_turn = j-i+1 # maximum possible turns (print each character at 1 turn)
            # check each char s[k] between i and j, if s[k] is same as s[i], then s[k] would be printed when printing s[i],
            # so we can reduce the range [i,j] to [i,k-1] and [k+1,j]
            for k in range(i, j):
                if (s[k] == s[j]):
                    min_turn = min(min_turn, dp(i,k)+dp(k+1,j)-1)
                else:
                    min_turn = min(min_turn, dp(i, k) + dp(k + 1, j))
            return min_turn

        return dp(0, len(s) - 1)

class Solution1:
    def strangePrinter(self, S: str) -> int:
        if not S:
            return 0

        s = S[0]
        for c in S[1:]:
            if c != s[-1]:
                s += c

        @lru_cache(None)
        def dp(i, j):
            nonlocal s
            if i > j: return 0
            min_turn = dp(i, j - 1) + 1
            # check each char s[k] between i and j, if s[k] is same as s[i], then s[k] would be printed when printing s[i],
            # so we can reduce the range [i,j] to [i,k-1] and [k+1,j]
            for k in range(i, j):
                if (s[k] == s[j]):
                    min_turn = min(min_turn, dp(i, k) + dp(k + 1, j - 1))
                else:
                    min_turn = min(min_turn, dp(i, k) + dp(k + 1, j))
            return min_turn

        return dp(0, len(s) - 1)

def main():
    sol = Solution1()
    assert sol.strangePrinter("aaabbb") == 2, 'fails'
    assert sol.strangePrinter("aba") == 2, 'fails'
    assert sol.strangePrinter("tbgtgb") == 4, 'fails'

if __name__ == '__main__':
   main()