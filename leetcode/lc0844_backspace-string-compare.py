"""
844. Backspace String Compare
Easy

2788

126

Add to List

Share
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
"""
"""
Stack

time O(M+N)
space O(M+N)
"""


class Solution0:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def eval_backspace(s):
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)

            return ''.join(stack[::-1])

        s1 = eval_backspace(s)

        t1 = eval_backspace(t)

        return s1 == t1


"""
Two Pointers

use two pointers, to iterate from right to left, since we don't know if a character belongs to final result until we scan all the # after it

note:
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def eval_backspace(s):
            ans = ''
            skip = 0
            for c in reversed(s):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    ans += c

            return ans

        return eval_backspace(s) == eval_backspace(t)

def main():
    sol = Solution()
    assert sol.backspaceCompare(s = "ab#c", t = "ad#c") == True, 'fails'

if __name__ == '__main__':
   main()