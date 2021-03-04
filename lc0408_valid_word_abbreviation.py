"""
408. Valid Word Abbreviation
Easy
https://leetcode.com/problems/valid-word-abbreviation/

"""
from functools import lru_cache

"""
Backtracking with memoization
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        @lru_cache(None)
        def match(word, abbr):
            # print('word=%s abbr=%s' % (word, abbr))
            if not word and not abbr:
                return True
            if (word and not abbr) or (not word and abbr):
                return False

            if word[0] == abbr[0]:
                return match(word[1:], abbr[1:])
            else:  # word[0] != abbr[0]
                i, num = 0, ''
                while i < len(abbr) and abbr[i].isdigit():
                    if num == '' and abbr[i] == '0':  # invalid abbreviation '01'
                        return False
                    num += abbr[i]
                    i += 1

                if num:
                    num = int(num)
                    if num > len(word):
                        return False
                    else:
                        return match(word[num:], abbr[i:])
                else:
                    return False

        return match(word, abbr)


def main():
    sol = Solution()
    assert sol.validWordAbbreviation(s = "internationalization", abbr = "i12iz4n") is True, 'fails'

    assert sol.validWordAbbreviation(s = "apple", abbr = "a2e") is False, 'fails'

if __name__ == '__main__':
   main()