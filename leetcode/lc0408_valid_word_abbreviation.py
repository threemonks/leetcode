"""
408. Valid Word Abbreviation
Easy

202

825

Add to List

Share
A string can be abbreviated by replacing any number of non-adjacent substrings with their lengths. For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
Note that "s55n" ("s ubsti tutio n") is not a valid abbreviation of "substitution" because the replaced substrings are adjacent.

Given a string s and an abbreviation abbr, return whether the string matches with the given abbreviation.



Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false


Constraints:

1 <= word.length, abbr.length <= 20
word consists of only lowercase English letters.
abbr consists of lowercase English letters and digits.
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