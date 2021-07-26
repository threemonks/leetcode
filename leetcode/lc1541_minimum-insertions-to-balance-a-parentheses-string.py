"""
1541. Minimum Insertions to Balance a Parentheses String
Medium

343

76

Add to List

Share
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as openning parenthesis and '))' as closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.



Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
Example 4:

Input: s = "(((((("
Output: 12
Explanation: Add 12 ')' to balance the string.
Example 5:

Input: s = ")))))))"
Output: 5
Explanation: Add 4 '(' at the beginning of the string and one ')' at the end. The string becomes "(((())))))))".


Constraints:

1 <= s.length <= 10^5
s consists of '(' and ')' only.
"""
import math
from typing import List

"""
Hash Table + Prefix sum

For remaining arry after removing subarray to be divisible by p, then the remainder of total sum divided by p should be same as remainder of sum of removed subarray divided by p.

let total_remainder = sum(nums) % p, we want to remove min length subarray whose sum(subarray) %p == total_remainder
if we calculate prefix sum of nums, then calculate remainder of the presum % p, then we are looking for two element in remainder of presum that has difference of total_remainder, i.e., 

iterate through remainder of presum % p, for current index i, with remainder of presum % p as cur_remainder, we look for last found cur_remainder - total_remainder, elements within this subarray can be removed for remaining array to have sum divisible by p.

"""
"""
Stack

1. for each two closing paren, 
    if stack is empty, we need to insert one open paren
    else, just pop one open paren from stack
    if we have just one closing paren, we need to insert another closing paren
2. for open paren, just push into stack
3. if at end, there are open paren left at stack, append double closing paren for each such open paren

"""


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        stack = []

        ans = 0
        i = 0
        while i < n:
            if s[i] == "(":
                stack.append(i)
            else:  # s[i] == ')'
                if i + 1 >= n or s[i + 1] != ')':
                    ans += 1
                else:  # use another )
                    i += 1
                if stack:
                    stack.pop()  # removing corresponding open paren
                else:  # need to insert one open paren
                    ans += 1
            i += 1

        # for each remaining open paren, we need to insert two closing paren
        ans += 2 * len(stack)

        return ans

def main():
    sol = Solution()

    assert sol.minInsertions(s = "(()))") == 1, 'fails'

    assert sol.minInsertions(s = "())") == 0, 'fails'

    assert sol.minInsertions(s = "))())(") == 3, 'fails'

    assert sol.minInsertions(s = "((((((") == 12, 'fails'

    assert sol.minInsertions(s = ")))))))") == 5, 'fails'

if __name__ == '__main__':
   main()