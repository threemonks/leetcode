"""
2266. Count Number of Texts
Medium

243

5

Add to List

Share
Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.


In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

For example, when Alice sent the message "bob", Bob received the string "2266622".
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.
Example 2:

Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.


Constraints:

1 <= pressedKeys.length <= 10^5
pressedKeys only consists of digits from '2' - '9'.
"""
"""
DP

dp[n] # of ways up till character 0...n-1

for digit 2,3,4,5,6,8, there are three cases

      *
      |
4 4 4 4

case 1: [4 4 4] 4 consider only one 4
                -
case 2: [4 4] 4 4 consider two 4's
              - -
case 3: [4] 4 4 4 consider three 4's
            - - -

for 7, 9 and we need to consider four 7's and four 9's case

if s[i] == s[i-1]:
  dp[i] += dp[i-1] % MOD
  if s[i] == s[i-2]:
    dp[i] += dp[i-2] % MOD
    if s[i] == s[i-3]:
      dp[i] += dp[i-3] % MOD
      if s[i] == s[i-4] and s[i] in '79':
        dp[i] += dp[i-4] % MOD

"""


class Solution:
    def countTexts(self, s: str) -> int:
        n = len(s)
        MOD = 1000000007
        dp = [0] * (n + 1)  # padding empty at left

        dp[0] = 1  # one way for left of beginning

        for i in range(1, n + 1):
            # index for s in i-1
            dp[i] = (dp[i] + dp[i - 1]) % MOD
            if (i - 2 >= 0 and s[i - 1] == s[i - 2]):
                dp[i] = (dp[i] + dp[i - 2]) % MOD
                if (i - 3 >= 0 and s[i - 1] == s[i - 3]):
                    dp[i] = (dp[i] + dp[i - 3]) % MOD
                    if (i - 4 >= 0 and s[i - 1] in '79' and s[i - 1] == s[i - 4]):
                        dp[i] = (dp[i] + dp[i - 4]) % MOD

        return dp[-1]


def main():
    sol = Solution()
    assert sol.countTexts(s = "22233") == 8, 'fails'

    assert sol.countTexts(s = "222222222222222222222222222222222222") == 82876089, 'fails'

if __name__ == '__main__':
   main()