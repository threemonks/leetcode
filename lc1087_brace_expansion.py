"""
1087. Brace Expansion
Medium

A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]


Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.

"""
from functools import lru_cache
from typing import List

"""
for chars outside bracket, append to each result
for chars inside bracket, build a separate list, until end of bracket, then multiple current result sets by appending each char of bracket content into result to get a new result
"""


class Solution:
    def expand(self, S: str) -> List[str]:

        result = [[]]
        in_bracket = False
        bracket_chars = []
        for i in range(len(S)):
            c = S[i]
            if c == ',':
                continue
            elif c == '{':
                in_bracket = True
                bracket_chars = []
            elif c == '}':
                in_bracket = False
                result = [r + [bc] for r in result for bc in sorted(bracket_chars)]
                bracket_chars = []
            else:
                if not in_bracket:
                    result = [r + [c] for r in result]
                else:
                    bracket_chars.append(c)

        return [''.join(r) for r in result]


def main():
    sol = Solution()
    assert sol.expand("{a,b}c{d,e}f") == ["acdf","acef","bcdf","bcef"], 'fails'

    assert sol.expand("abcd") == ["abcd"], 'fails'

if __name__ == '__main__':
   main()