"""
91. Decode Ways
Medium

4183

3414

Add to List

Share
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.
Example 4:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

"""
from functools import lru_cache

"""
DP

dp[i] := how many ways to decode up to s[:i]

base case:
dp[-1] = 1 # empty
if s[0] == '0':
    dp[1] = 0 # cannot have leading '0'
else:
    dp[1] = 1

# check if we can do single digit decoding
if 0 < s[i-1] <= 9:
    dp[i] += dp[i-1]
# check if we can do double digit decoding
if 10 <= s[i-2:i] <= 26: 
    dp[i] += dp[i-2]

time O(N)
space O(N) - can use O(1) space since dp[i] only relies on dp[i-1] and dp[i-2]
"""


class Solution0:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(
            n + 1)]  # dp[i+1] corresponding to s[i], adding extra dp[0] to make working with index i-1, i-2 easier
        dp[0] = 1  # empty string

        if s[0] == '0':  # cannot have leading zero
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, n + 1):
            # check two digits value and one digit value
            onedigit = int(s[i - 1:i])
            twodigit = int(s[i - 2:i])
            # check if successful single digit decode is possible
            if onedigit > 0:
                dp[i] += dp[i - 1]

            if 10 <= twodigit <= 26:
                dp[i] += dp[i - 2]
            # print('i=%s dp=%s' % (i, dp))

        return dp[n]


"""
DP recursive

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def helper(idx):
            nonlocal s
            # decoded entire string, return 1
            if idx == n:
                return 1

            # cannot decode string with leading zero
            if s[idx] == '0':
                return 0

            # decode using single digit
            ans = helper(idx + 1)

            # decode two digits together (if valid)
            if idx + 2 <= n and int(s[idx:idx + 2]) <= 26:
                ans += helper(idx + 2)

            return ans

        return helper(0)


def main():
    sol = Solution()
    assert sol.numDecodings(s = "12") == 2, 'fails'

    assert sol.numDecodings(s = "226") == 3, 'fails'

    assert sol.numDecodings(s = "0") == 0, 'fails'

    assert sol.numDecodings(s = "06") == 0, 'fails'

if __name__ == '__main__':
   main()