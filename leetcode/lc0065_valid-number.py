"""
65. Valid Number
Hard

208

428

Add to List

Share
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.



Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true


Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""
"""
String

different formats

(+/-)num.num eE (+/-)num
(+/-).num eE (+/-)num
(+/-)num. eE (+/-)num
(+/-)num eE (+/-)num
"""
import re


class Solution0:
    def isNumber(self, s: str) -> bool:
        return bool(re.search('^([+-])?(\d+(\.)?(\d+)?|\.\d+)(e([+-])?\d+)?$', s, re.IGNORECASE))


"""
Deterministic Finite Automaton (DFS)

digit 0-9
sign +- # first char or right after exponent
dot . # cannot be after another dot or after exponent
exponent eE # must have seen digit, not seen exponent, we reset seen digit here as we requires digit after exponent
anything else => invalid

at end, we need to have seenDigit = True, it applies whether we have exponent or not

possible states:
seen_digit # must have at least one digit
seen_dot
seen_exponent # after exponent, cannot have dot after

-123.456E+789
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit, seen_dot, seen_exponent = False, False, False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in '+-':  # must be first or right after seen_exponent
                if i > 0 and s[i - 1] not in 'eE':
                    return False
            elif c in 'eE':
                if seen_exponent or not seen_digit:
                    return False
                else:
                    seen_exponent = True
                    seen_digit = False  # reset seen_digit so we can detect integer exponent
            elif c == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit


def main():
    sol = Solution()
    assert sol.isNumber('e') == False, 'fails'

    assert sol.isNumber(s = ".1") == True, 'fails'

if __name__ == '__main__':
   main()