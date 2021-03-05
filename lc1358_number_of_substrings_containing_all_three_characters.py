"""
1358. Number of Substrings Containing All Three Characters
Medium

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1


Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

"""

from typing import List

"""
Two Pointers
loop (fixed) right index j, increase left index i to as right as possible so that substring s[i:j] dost not contain all 'abc' while s[i-1:j] does contain all 'abc',
then we got valid subarray that ranges s[i-1:j], and every character before s[i-1] can also be prepended to make a new qualified subarray. so we have
    res += (i-1) - 0 + 1 = i (number of different subarray starting at 0, 1, ..., i-1)

time O(N^2)
"""


class Solution0:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ccounts = [0] * 3  # 0->'a', 1->'b', 2->'c'

        res = 0
        i = 0
        for j in range(n):
            ccounts[ord(s[j]) - ord('a')] += 1
            while i < n and all(ccounts):
                ccounts[ord(s[i]) - ord('a')] -= 1
                i += 1
            # i was the last char that makes all(ccounts) true s[i:j] qualified substring, and s[i+1:j] is not qualified substring
            res += i

        return res


"""
two pointers
loop (fix) left index i, explore right index j to as far as possible to just cover at least one of each of 'a', 'b', 'c'
then res += n-1-j+1 (all letters after j adds one valid subarray start at i, and ending at that new char after j)

time O(N^2)
"""


class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ccounts = [0] * 3  # 0->'a', 1->'b', 2->'c'

        res = 0
        j = 0
        ccounts[ord(s[0]) - ord('a')] += 1
        for i in range(n):
            # print('i=%s' % i)
            while j + 1 < n and not all(ccounts):
                j += 1
                ccounts[ord(s[j]) - ord('a')] += 1
                # print('j=%s ccounts=%s res=%s' % (j, str(ccounts), res))
            if all(ccounts):
                res += n - 1 - j + 1  # now all letters after j will add a new qualified
            # print('i=%s j=%s ccounts=%s res=%s' % (i, j, str(ccounts), res))
            # reduce count for s[i] as we will increase i in next round
            ccounts[ord(s[i]) - ord('a')] -= 1

        return res


"""
lastpos={'a', 'b', 'c'} # store last seen 'abc' before i-th element
for each element s[i]
if s[i] == 'a':
    res  += min(lastpos['b'], lastpos['c'])+1
    # number of result increase by number of valid substring ending at i, which is the smallest last seen position of 'b and 'c'

time O(N)
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        lastpos = [-1, -1, -1]
        for i in range(n):
            if s[i] == 'a':
                res += min(lastpos[1], lastpos[
                    2]) + 1  # number of result increase by number of valid substring ending at i, which is the smallest last seen position of 'b and 'c'
            elif s[i] == 'b':
                res += min(lastpos[0], lastpos[2]) + 1
            else:  # s[i] == 'c':
                res += min(lastpos[0], lastpos[1]) + 1
            lastpos[ord(s[i]) - ord('a')] = i

        return res

def main():
    sol = Solution()
    assert sol.numberOfSubstrings("abcabc") == 10, 'fails'

    assert sol.numberOfSubstrings("aaacb") == 3, 'fails'

    assert sol.numberOfSubstrings("abc") == 1, 'fails'

if __name__ == '__main__':
   main()