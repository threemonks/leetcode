"""
1347. Minimum Number of Steps to Make Two Strings Anagram
Medium

1544

73

Add to List

Share
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.



Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.


Constraints:

1 <= s.length <= 5 * 10^4
s.length == t.length
s and t consist of lowercase English letters only.
"""
"""
Hash Table

get char count dictionary of both string

assume there's a total of d char counts (adding all char count difference between the char count for s and t) being different, it would take d/2 steps to replace one to match the other

"""
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        scount = Counter(s)
        tcount = Counter(t)

        ans = 0
        for k in 'abcdefghijklmnopqrstuvwxyz':
            if scount[k] != tcount[k]:
                ans += abs(scount[k] - tcount[k])

        return ans // 2

def main():
    sol = Solution()
    assert sol.minSteps(s = "bab", t = "aba") == 1, 'fails'

    assert sol.minSteps(s = "leetcode", t = "practice") == 5, 'fails'

    assert sol.minSteps(s = "anagram", t = "mangaar") == 0, 'fails'

if __name__ == '__main__':
   main()