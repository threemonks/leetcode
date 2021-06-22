"""
301. Remove Invalid Parentheses
Hard

3523

162

Add to List

Share
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.



Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]


Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""
from functools import lru_cache
from typing import List

"""
Backtrack / String

cout left and right parens
if right > left, max(right-left) are invalid right paren counts
if at end, left > right, left-right are invalid left paren counts

Obseration:
1. We don't know which brackets can possibly be removed, so we will try all options using recursion/backtrack
2. since we are asked to remove minimum number of invalid parentheses, so the result should all be same length, i.e., all removing same number of chars
3. we can try to find out the minimum number of invalid parentheses, by counting left paren and right paren, if any time right > left, than right-lefts are invalid right parens, at end, if left > right, left-right are invalid left parens.

time: O(2^N) - backtracking for each char, can use it or not use

mistakes:
1. Need to use memoization, to speed up also to avoid duplicates in result
2. if no result, return [""], not []
3. within recursive call, test i==n and valid path first, add to result if valid
4. if accumulated path is '', don't add to result (would otherwise result in duplicate "")
5. we need to keep all letters, only remove invalid open or close parenthesis
"""


class Solution0:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)

        @lru_cache(None)
        def count_invalid(p, op='(', cp=')'):
            invalid_right = 0  # right parens that need to be removed
            left, right = 0, 0  # left and right paren counts
            for c in p:
                if c == op:
                    left += 1
                elif c == cp:
                    right += 1
                if right > left:
                    invalid_right = max(invalid_right, right - left)

            return invalid_right

        @lru_cache(None)
        def valid(p):
            invalid_right = count_invalid(p, op="(", cp=")")
            invalid_left = count_invalid(p[::-1], op=")", cp="(")

            return invalid_left == 0 and invalid_right == 0

        invalid_right = count_invalid(s, op="(", cp=")")
        invalid_left = count_invalid(s[::-1], op=")", cp="(")
        print('invalid_right=%s invalid_left=%s' % (invalid_right, invalid_left))

        result = []

        @lru_cache(None)
        def helper(i, path):
            # checking index i
            # print('i=%s path=%s' % (i, path))
            if i == n:
                if path and valid(path):
                    result.append(path)
                return

            helper(i + 1, path + s[i])
            if s[i] in '()':  # cannot skip letters
                helper(i + 1, path)

        helper(0, '')
        # print(result)
        return result or [""]


"""
BFS

use valid() to check for valid parenthesis expression, then use BFS to traverse all possible answer, BFS gives result with smallest removal first (level by level)

"""


class Solution1:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)

        @lru_cache(None)
        def valid(p):
            count = 0  # unmatched open paren
            for c in p:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:  # too many closing paren
                    return False

            return count == 0

        q = deque([s])
        seen = set([s])
        result = []
        while q:

            # process level by level, each level we remove more characters
            # so first level with non-empty result are the valid answers (minimum removal to make valid parentheses expression)
            size = len(q)
            for _ in range(size):
                curs = q.popleft()
                if valid(curs):
                    result.append(curs)
                for i in range(len(curs)):
                    nxt = curs[:i] + curs[i + 1:]
                    if nxt not in seen:
                        q.append(nxt)
                        seen.add(nxt)

            if result:  # first set of valid expression should be the set with minimum removals
                return result


from functools import lru_cache
from typing import List

"""
Backtrack / String

1. we are asked to output all possible results with minimum removal to form valid parentheses, so we should be considering backtracking instead of dp (dp usually is good for find min/max counts/number of ways etc)
2. we use backtracking to try to keep or remove each character, and check if the final result string is valid or not.

time: O(2^N) - backtracking for each char, can use it or not use

"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)

        @lru_cache(None)
        def valid(p):
            # if any moment count < 0, or at last count != 0, then it is invalid
            count = 0  # unmatched open paren
            for c in p:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False

            return count == 0

        result = []

        @lru_cache(None)
        def helper(i, path, removed):
            # checking index i
            if i == n:
                if valid(path):
                    result.append(path)
                return

            helper(i + 1, path + s[i], removed)
            if s[i] in '()':  # cannot skip letters
                helper(i + 1, path, removed + 1)

        helper(0, '', removed=0)
        maxlen = max([len(r) for r in result])
        return [r for r in result if len(r) == maxlen]


def main():
    sol = Solution()

    assert sol.removeInvalidParentheses(s = "()())()") == ["(())()","()()()"], 'fails'

    assert sol.removeInvalidParentheses(s = "(a)())()") == ["(a())()","(a)()()"], 'fails'

    assert sol.removeInvalidParentheses(s = ")(") == [""], 'fails'

    assert sol.removeInvalidParentheses(s = ")(f") == ["f"], 'fails'

    assert sol.removeInvalidParentheses(s = "(()y") == ["()y"], 'fails'

if __name__ == '__main__':
   main()