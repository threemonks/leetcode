"""
282. Expression Add Operators
Hard

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []


Constraints:

0 <= num.length <= 10
num only contain digits.

"""

from typing import List
from functools import lru_cache

"""
divide and conquer with memoization

Note: maximum number of combinations 4^10 ('+-*'), this is within range that can be done by divide and conquer / brutal force

time O(N*4^N) eval take O(N), combinations total 10 chars, in between each char pair, 4 possible operators (3 + NOOP)
space O(N)

mistakes:
1. iterate through all possible position to insert operator - for i in range(1, len(s))
2. all numeric only string are valid substrings that can be part of the answer, except if it starts with 0
   i.e., a number can contain multiple digits

"""

class Solution0:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)

        @lru_cache(None)
        def helper(s):
            # print('s=%s' % s)
            if len(s) == 1:
                return [s]
            result = set()
            if s.isdigit() and not s.startswith('0'):
                result.add(s)
            for i in range(1, len(s)):
                for op in '+-*':
                    for l in helper(s[:i]):
                        for r in helper(s[i:]):
                            result.add(l + op + r)

            # print('s=%s result=%s' % (s, result))
            return result

        result = helper(num)
        # print(result)

        return [r for r in result if eval(r) == target]


"""
Observation:
eval entire expression at last is expensive and slow, we want to try to parse the string token as we go from left to right, and eval each valid token when it is encountered

steps:
1. at index idx of string num, for i = idx+1,..., len(num), extract a number of length i from beginning of remaining string num[idx:]
   note if leading 0, only extract 1 digit, as '01' is invalid number according to example
2. apply each one of the three operators (+-*) between cur (numeric eval result from processing chars before num[idx:])
   and int(num[idx:i]), then add result into current running numeric result of processing, also add string num[idx:i] into running string result path, cur+int(num[idx:i])
3. and recursive call dfs with index i
base case: if idx == len(num):
                if cur == target: result.append(path)
            return

Note: to handle precedence of * is higher than + and -, we pass current token value int(num[idx:i]) into next recursive call as last, so for operator *, the added value calculation is cur-last+last*int(num[idx:i])

but there are a few edge cases need handled to parse tokens from the string and calculate intermediate result
1. cannot have leading zero in multi-digit integer
2. multiplication has higher precedence than +/-, so we need to keep track of previous operand to deal with multiplication

mistakes:
1. for subtraction case, pass -x as last into recursive call, not just
2. for multiplication case, pass last*x as last into recursive call, not just x

"""


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        result = set()

        def dfs(idx, path, cur, last):
            # print('idx=%s path=%s cur=%s last=%s' % (idx, path, cur, last))
            if idx == n:
                if cur == target:
                    result.add(''.join(path))
                return
            for i in range(idx + 1, n + 1):
                if i > idx + 1 and num[idx] == '0':  # skip numeric number with leading '0'
                    continue
                s, x = num[idx:i], int(num[idx:i])
                # print('i=%s s=%s x=%s' % (i, s, x))
                if path == '':  # first expression
                    dfs(i, s, x, x)
                else:
                    dfs(i, path + '+' + s, cur + x, x)
                    dfs(i, path + '-' + s, cur - x, -x)
                    dfs(i, path + '*' + s, cur - last + last * x, last * x)

        dfs(0, '', 0, 0)

        return list(result)


def main():
    sol = Solution()
    assert sol.addOperators(num = "123", target = 6) == ["1+2+3", "1*2*3"], 'fails'

    assert sol.addOperators(num = "232", target = 8) == ["2*3+2", "2+3*2"], 'fails'

    assert sol.addOperators(num = "105", target = 5) == ["1*0+5","10-5"], 'fails'

    assert sol.addOperators(num = "00", target = 0) == ["0+0", "0-0", "0*0"], 'fails'

    assert sol.addOperators(num = "3456237490", target = 9191) == [], 'fails'

if __name__ == '__main__':
   main()