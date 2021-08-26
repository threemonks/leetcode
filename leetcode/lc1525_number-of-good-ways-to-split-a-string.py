"""
1525. Number of Good Ways to Split a String
Medium

761

22

Add to List

Share
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.



Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
Example 3:

Input: s = "aaaaa"
Output: 4
Explanation: All possible splits are good.
Example 4:

Input: s = "acbadbaada"
Output: 2


Constraints:

s contains only lowercase English letters.
1 <= s.length <= 10^5
"""
"""
HashMap

use two hashmap to store count of each character
if a valid split is found (uniq count left == uniq count right), increase good split count

"""
from collections import defaultdict

class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)

        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        for i in range(n):
            counter2[s[i]] += 1

        ans = 0

        for i in range(n):
            counter1[s[i]] += 1
            counter2[s[i]] -= 1
            if counter2[s[i]] == 0:
                del counter2[s[i]]
            if len(counter1) == len(counter2):
                ans += 1

        return ans

def main():
    sol = Solution()
    assert sol.numSplits(s = "aacaba") == 2, 'fails'

    assert sol.numSplits(s = "abcd") == 1, 'fails'

    assert sol.numSplits(s = "aaaaa") == 4, 'fails'

    assert sol.numSplits(s = "acbadbaada") == 2, 'fails'

if __name__ == '__main__':
   main()