"""
394. Decode String
Medium

5473

252

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
"""
Stack

steps:
1. if ], pop from stack until we see [, concatenate popped into s1
  if stack top is digit, multiply s1*int(stack[-1]), and push result back into stack
2. if not ], push into stack
3. when done iterating s, pop from stack and push into output one by one
4. reverse output as ans

mistakes:
1. repeat number could be multiple digits
"""


class Solution0:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        ans = ''
        i = 0
        while i < n:
            c = s[i]
            if c == ']':
                s1 = ''
                while stack and stack[-1] != '[':  # do we check digit here?
                    if stack[-1].isdigit():
                        raise Exception('invalid stack=%s' % stack)
                    s1 += stack.pop()
                if stack:
                    stack.pop()  # remove the corresponding '['
                    if stack[-1].isdigit():
                        m = stack.pop()
                        stack.append(s1 * int(m))
                    else:
                        stack.append(s1)
                else:
                    raise Exception('Matching [ not found')
            elif c.isdigit():
                # get the entire number and push to stack as one
                num_s = c
                while i + 1 < n and s[i + 1].isdigit():
                    num_s += s[i + 1]
                    i += 1
                # now we have entire number, push to stack
                stack.append(num_s)
            else:
                stack.append(c)

            i += 1

        while stack:
            ans += stack.pop()

        return ans[::-1]


"""
Stack
push multiple digits into stack separately
"""


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        ans = ''
        for c in s:
            if c == ']':
                s1 = ''
                while stack and stack[-1] != '[':  # do we check digit here?
                    if stack[-1].isdigit():
                        raise Exception('invalid stack=%s' % stack)
                    s1 += stack.pop()
                if stack:
                    stack.pop()  # remove the corresponding '['
                    num_s = ''
                    while stack and stack[-1].isdigit():
                        num_s += stack.pop()
                    if num_s:
                        num_s = num_s[::-1]  # to get original order of digits
                        stack.append(s1 * int(num_s))
                    else:
                        stack.append(s1)
                else:
                    raise Exception('Matching [ not found')
            else:
                stack.append(c)

        while stack:
            ans += stack.pop()

        return ans[::-1]


def main():
    sol = Solution()
    assert sol.decodeString(s = "3[a]2[bc]") == "aaabcbc", 'fails'

    assert sol.decodeString(s = "3[a2[c]]") == "accaccacc", 'fails'

    assert sol.decodeString(s = "2[abc]3[cd]ef") == "abcabccdcdcdef", 'fails'

    assert sol.decodeString(s = "abc3[cd]xyz") == "abccdcdcdxyz", 'fails'

if __name__ == '__main__':
   main()