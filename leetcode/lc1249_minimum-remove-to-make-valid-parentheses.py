"""
1249. Minimum Remove to Make Valid Parentheses
Medium

2199

50

Add to List

Share
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""
"""
Two Pass

key observation:
when scan from left to right, for any invalid ")", we know immediately as opens < 0, so we can scan from left to right to drop any invalid ")"
similarly, after the above operation, we scan from right to left to find any invalid "(", which we can identify immediately and drop it.

from left to right, drop any extra closing parenthesis
for the result string, from right to left, drop any extra opening parenthesis

time O(N)
"""
class Solution0:
    def minRemoveToMakeValid(self, s: str) -> str:
        # from left to right, drop any closing parenthesis
        opens = 0
        s1 = ''
        for c in s:
            if c == ')':
                if opens == 0: # drop extra )
                    pass
                else:
                    opens -= 1
                    s1 += c
            else:
                if c == '(':
                    opens += 1
                s1 += c

        # from right to left, drop any opening parenthesis
        opens = 0
        ans = ''
        for c in s1[::-1]:
            if c == '(':
                if opens == 0: # drop extra )
                    pass
                else:
                    opens -= 1
                    ans += c
            else:
                if c == ')':
                    opens += 1
                ans += c

        return ans[::-1]

"""
Stack

Each time we see "(", we add its index to stack, each time we see ")", we remove index from stack top because ")" will match the closest "(" on top of stack. The length of the stack is equivalent of balance (unmatched "(").

steps:
1. Push char index into the stack when we see '('.
2. Pop from the stack when we see ')'.
    2.1 If the stack is empty, then we have ')' without the pair, and it needs to be removed.
3. In the end, the stack will contain indexes of '(' without the pair, if any. We need to remove all of them too.

time O(N)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        toremove = set()
        stack = []

        for i, c in enumerate(s):
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    toremove.add(i)
            elif c == '(':
                stack.append(i)

        while stack:
            toremove.add(stack.pop())

        ans = ''
        for i, c in enumerate(s):
            if i not in toremove:
                ans += c

        return ans

def main():
    sol = Solution()

    assert sol.minRemoveToMakeValid(s = "lee(t(c)o)de)") in ["lee(t(co)de)" , "lee(t(c)ode)", 'lee(t(c)o)de'], 'fails'

    assert sol.minRemoveToMakeValid(s = "a)b(c)d") in ["ab(c)d"], 'fails'

    assert sol.minRemoveToMakeValid(s = "))((") in [""], 'fails'

    assert sol.minRemoveToMakeValid(s = "(a(b(c)d)") in ["a(b(c)d)"], 'fails'

if __name__ == '__main__':
   main()