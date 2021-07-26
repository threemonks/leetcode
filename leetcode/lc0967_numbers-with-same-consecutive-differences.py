"""
967. Numbers With Same Consecutive Differences
Medium

639

121

Add to List

Share
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.



Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
Example 3:

Input: n = 2, k = 0
Output: [11,22,33,44,55,66,77,88,99]
Example 4:

Input: n = 2, k = 2
Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]


Constraints:

2 <= n <= 9
0 <= k <= 9
"""
from typing import List

"""
DFS

dfs tree depth n, each node has children that could be x+j*k, or x-j*k, as long as 0<=x+j*k<=9 (0<=x-j*k<=9)

n=3, k = 2
   1         9
   3         7
 5   1    5     9

"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        nums = list(range(1, 10)) # cannot have leading zero

        res = []
        for num in nums:
            q = [num]

            # print('q=%s' % q)
            while q:
                cur = q.pop()
                # print('cur=%s q=%s res=%s' % (cur, q, res))
                if len(str(cur)) == n:
                    res.append(cur)
                    continue # this path is done, don't explore further

                # explore all children, i.e., appending last digit +/- k as new last digit
                x = cur%10
                if k:
                    if x+k < 10:
                        y = cur*10+x+k
                        q.append(y)
                    if x-k >= 0:
                        y = cur*10+x-k
                        q.append(y)
                else:
                    y = cur*10+x
                    q.append(y)

        return res

"""
DFS recursive

"""
class Solution1:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def dfs(n, num):
            # n: remaining digits to add
            # num: current num
            # print('n=%s num=%s' % (n, num))
            if not n:
                result.append(num)
                return

            # get last digit of num, find its neighbor with difference k
            # explore further
            x = num % 10 # last digit

            # all valid digits that are k steps away from x
            if k:
                if x+k < 10:
                    dfs(n-1, num*10+x+k)

                if x-k >= 0:
                    dfs(n-1, num*10+x-k)
            else:
                dfs(n-1, num*10+x)

        for i in range(1, 10):
            dfs(n-1, i)

        return result

def main():
    sol = Solution()
    assert sol.numsSameConsecDiff(n = 3, k = 7) == [181,292,707,818,929], 'fails'

    assert sol.numsSameConsecDiff(n = 2, k = 1) == [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98], 'fails'

    assert sol.numsSameConsecDiff(n = 2, k = 0) == [11,22,33,44,55,66,77,88,99], 'fails'

    assert sol.numsSameConsecDiff(n = 2, k = 2) == [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97], 'fails'

if __name__ == '__main__':
   main()