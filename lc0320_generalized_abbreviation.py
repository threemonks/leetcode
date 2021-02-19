"""
320. Generalized Abbreviation
Medium

https://leetcode.com/problems/generalized-abbreviation/
"""
from typing import List

"""
backtrack with loop to abbreviate 0 to len(s) chars in current solution
"""


class Solution0:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        result = []

        def dfs(s, curr):
            """
            curr is current result so far, and s is remaining string to be processed
            """
            if not s:
                result.append(curr)
                return
            for i in range(len(s) + 1):
                if i == 0:
                    dfs(s[i + 1:], curr + s[i])  # don't insert number 0
                else:
                    dfs(s[i + 1:], curr + str(i) + s[i:i + 1])  # insert abbreviation and next char

        dfs(word, '')
        return result


"""
backtrack without loop, but keep track a count of how many chars we are abbreviating
"""


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        result = []

        def dfs(s, curr, count):
            """
            curr is current result so far, and s is remaining string to be processed
            """
            if not s:
                if count > 0:
                    curr = curr + str(count)
                result.append(curr)
                return

            # abbreviate current char (increase count)
            dfs(s[1:], curr, count + 1)
            # don't abbreviate current char, add previous counts as string if necessary, and reset count
            dfs(s[1:], curr + (str(count) if count > 0 else '') + s[0], 0)

        dfs(word, '', 0)
        return result


def main():
    sol = Solution()
    assert sorted(sol.generateAbbreviations(word = "word")) == sorted(["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]), 'fails'

    assert sorted(sol.generateAbbreviations(word = "a")) == sorted(["1","a"]), 'fails'

if __name__ == '__main__':
   main()