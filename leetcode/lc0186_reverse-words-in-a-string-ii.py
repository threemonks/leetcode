"""
186. Reverse Words in a String II
Medium

683

122

Add to List

Share
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.



Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]


Constraints:

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
"""
from typing import List

"""
Two Pointers

Use two pointers, to keep track of beginning and end of each word (possibly with leading space), move and insert it to beginning of entire string
repeat until finish entire string
"""


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left, right = 0, 0
        head = 0
        while right < n:
            while right < n and s[right].isalnum():
                right += 1
            # now left ... right-1 is a valid word
            # insert it to begin of word
            tmp = s[left:right]  # take the whitespace with this word
            l = len(tmp)
            for i in range(left - 1, -1, -1):
                s[i + l] = s[i]

            if tmp[0] == ' ':  # if tmp has leading whitespace, switch it to end of tmp
                tmp = tmp[1:] + tmp[:1]

            # insert tmp at begining of s
            for i in range(l):
                s[i] = tmp[i]
            # now move to next whitespace ready to do next move
            left = right
            right = left + 1

