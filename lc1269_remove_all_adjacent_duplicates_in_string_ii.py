"""
1209. Remove All Adjacent Duplicates in String II
Medium

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.



Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.

"""
import math
from functools import lru_cache
from typing import List

"""
use stack to keep track last checked letter and its count
if new character matches stack top, and its count adds 1 becomes k, then delete this char, i.e., pop stack
if new character matches stack top, but its count adds 1 is less than k, then increase the count by 1
if new character does not match stack top, push it into stack

time O(N)
space O(N)
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for idx, c in enumerate(s):
            if stack and c == stack[-1][0]:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([c, 1])

        # print(stack)
        return ''.join([v[0] * v[1] for v in stack])

def main():
    sol = Solution()
    assert sol.removeDuplicates("abcd", 2) == "abcd", 'fails'

    assert sol.removeDuplicates("deeedbbcccbdaa", 3) == "aa", 'fails'

    assert sol.removeDuplicates("pbbcggttciiippooaais", 2) == "ps", 'fails'


if __name__ == '__main__':
   main()