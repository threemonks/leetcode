"""
739. Daily Temperatures
Medium

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

"""
from typing import List

"""
Stack
observation 
use stack to hold temperatures that have not have a later warmer day yet, and store result of days til a warmer day whenever we found a new temperature higher than the top of the stack temperature

time O(n) length of T
space O(W) unique values in T

"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        n = len(T)
        res = [0] * n
        stack = [(0, T[0])]

        for i in range(1, n):
            while stack and T[i] > stack[-1][1]:
                tmp = stack.pop(-1)
                res[tmp[0]] = i - tmp[0]
            stack.append((i, T[i]))

        return res

def main():
    sol = Solution()
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0], 'fails'

if __name__ == '__main__':
   main()