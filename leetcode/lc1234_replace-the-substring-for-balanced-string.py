"""
1234. Replace the Substring for Balanced String

Medium

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.



Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".
Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".


Constraints:

1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.
"""
import collections

"""
Sliding Window / Two Pointers

Use a sliding window, we want to make sure all chars outside this window have its char count less than or equal to n/4, n=len(s)
At each step, move right pointer to right, make window bigger, to make the condition True, then we can keep move left pointer to right to minimize the answer (replaced window size), while keep the condition True, until the condition is broken, then we move left pointer to right to hopefully make the condition True again

Why inner loop i < n instead of i<j?
For sliding window, we don't need i<j, because usually when i<j, there's nothing in the sliding window. Instead, we only need to prevent index out of bound, for which we can use i<n.

For this problem specifically, when i>j, i.e., we have already have a balanced string, so we should return 0, instead of continue updating ans=min(ans, j-i+1)

condition all counts of all chars outside the i,...,j window have occurance counts less than n/4

all([v<=m for v in count.values()])

time O(N^2)
space O(1)
"""


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        m = n // 4

        count = collections.Counter(s)
        ans = n
        i = 0
        for j in range(n):  # j is right boundary of window
            count[s[j]] -= 1  # include s[j] into window, so count of outside chars --
            while i < n and all([v <= m for v in count.values()]):  # i is left boundary of window
                if i > j:  # the string is already balanced
                    return 0
                ans = min(ans, j - i + 1)
                count[s[i]] += 1
                i += 1

        return ans

def main():
    sol = Solution()
    assert sol.balancedString(s = "QWER") == 0, 'fails'

    assert sol.balancedString(s="QQWE") == 1, 'fails'

    assert sol.balancedString(s="QQQW") == 2, 'fails'

    assert sol.balancedString(s="QQQQ") == 3, 'fails'

if __name__ == '__main__':
   main()