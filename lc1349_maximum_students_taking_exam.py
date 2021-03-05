"""
1349. Maximum Students Taking Exam
Hard

Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.



Example 1:


Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.
Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats.

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.


Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8

"""
import math
from functools import lru_cache
from typing import List

"""
DP bitmask

bitmask cheatsheets
1. (x >> i) & 1 to get i-th bit in state x
   x & (1 << i)
2. (x & y) == x to check if x is a subset of y, i.e., every bit in x can be 1 only if the corresponding bit in y is 1
3. (x & (x >> 1)) == 0 to check if there are no adjacent valid states in x (1 is valid, 0 is invalid state)
4. iterate through all subsets of something target
    while state:
        # do something with state
        state = (state-1)&total_states
observation:
第一型 dp 时间序列 + bitmask 状态压缩 

seats[i][j] : 1 - good seat, 0 - bad seats

dp[i][bitset] := for given sitting state bitset after checking i-th row, maximum number of students
final result would be max(dp[m-1][1:(1<<n)])

m - seats.length number of rows
n - seats[0].length number of columns per row

bitmask
00000000
00000000
00000000
00000000
00000000
00000000
00000000
00000000

init
dp[bitmask][i] = [[0 for _ in range((1<<n))] for _ in range(n)]

for bitmask in range((1<<n)):
    for i in range(m):
        if conflict with seats, or adjacent seats are set:
            continue
        for prev_bitmask in range(1<<n):
            if bitmask and prev_bitmask not conflict (not left upper or right upper)
            dp[i][bitmask] = max(dp[i][bitmask], dp[i-1][bitmask]+ count_bit(bitset)
            
time O(N^2*2^N)
space O(2^N*m) - can be reduced to 1-d (2^N) since for each row, we only use information from immediate previous row

"""

class Solution0:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])

        # convert seats to bitmask int array
        seatbits = []
        for row in seats:
            rowbit = 0
            for idx, c in enumerate(row[::-1]):
                if c == '.':
                    rowbit |= (1 << idx)
            #print(bin(rowbit))
            seatbits.append(rowbit)
        # print([bin(bs) for bs in seatbits])

        dp = [[0 for _ in range((1<<n))] for _ in range(m)]
        for bitset in range(0, (1 << n)):
            # no adjacent seats used, and only valid seats used
            if ((bitset & (bitset >> 1)) == 0) and ((bitset & seatbits[0]) == bitset):
                dp[0][bitset] = bin(bitset).count("1")

        for i in range(1, m):
            for bitset in range(0, (1<<n)):
                if (bitset & (bitset >> 1)) > 0:
                    continue
                # for each bitset in row i-1, what bitset in i will work?
                if not ((bitset & seatbits[i]) == bitset):
                    continue
                # check all bitset in i-1 th row?
                dp[i][bitset] = 0
                for prev_bitset in range(1<<n):
                    # no adjacent valid states, nor left upper or right upper adjacent valid states
                    if (bitset & (prev_bitset >> 1) == 0) and (bitset & (prev_bitset << 1) == 0):
                        dp[i][bitset] = max(dp[i][bitset], dp[i-1][prev_bitset] + bin(bitset).count("1"))
            # print('i=%s' % i)
            # print(bin(seatbits[i]))
            # print([bin(idx) for idx, v in enumerate(dp[i])])
            # print(dp[i])

        # print([dp[m-1][k] for k in range((1 << n))])
        return max([dp[m-1][k] for k in range((1 << n))])


"""
use 1-d dp state matrix
"""
class Solution1:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])

        # convert seats to bitmask int array
        seatbits = []
        for row in seats:
            rowbit = 0
            for idx, c in enumerate(row[::-1]):
                if c == '.':
                    rowbit |= (1 << idx)
            #print(bin(rowbit))
            seatbits.append(rowbit)
        # print([bin(bs) for bs in seatbits])

        dp = [0 for _ in range((1<<n))]
        for bitset in range(0, (1 << n)):
            # no adjacent seats used, and only valid seats used
            if ((bitset & (bitset >> 1)) == 0) and ((bitset & seatbits[0]) == bitset):
                dp[bitset] = bin(bitset).count("1")

        for i in range(1, m):
            prev_dp = dp[:]
            for bitset in range(0, (1<<n)):
                if (bitset & (bitset >> 1)) > 0:
                    continue
                # for each bitset in row i-1, what bitset in i will work?
                if not ((bitset & seatbits[i]) == bitset):
                    continue
                # check all bitset in i-1 th row?
                dp[bitset] = 0
                for prev_bitset in range(1<<n):
                    # no adjacent valid states, nor left upper or right upper adjacent valid states
                    if (bitset & (prev_bitset >> 1) == 0) and (bitset & (prev_bitset << 1) == 0):
                        dp[bitset] = max(dp[bitset], prev_dp[prev_bitset] + bin(bitset).count("1"))
            # print('i=%s' % i)
            # print(bin(seatbits[i]))
            # print([bin(idx) for idx, v in enumerate(dp[i])])
            # print(dp[i])

        # print([dp[m-1][k] for k in range((1 << n))])
        return max([dp[k] for k in range((1 << n))])


"""
DP recursion with bitmask

two possible ways to handle transition
1. just iterate all possible masks (1<<n) in current row # this works for n<=8, but might not work for n=32
2. iterate submask (subsets) of the mask for current row

"""

class Solution2:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])

        valid_seats = [0] * m  # n bits
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    valid_seats[i] |= (1 << j)

        def bit_count(n):
            cnt = 0
            while n:
                n &= n - 1  # get most significant bit
                cnt += 1

            return cnt

        @lru_cache(None)
        def dp(i, prev_mask):
            if i == m:
                return 0
            ans = 0

            for mask in range(1 << n): # iterate all possible masks, only use valid ones
                if mask & valid_seats[i] == mask:
                    if mask & (mask >> 1) == 0 and mask & (mask << 1) == 0 and prev_mask & (
                            mask >> 1) == 0 and prev_mask & (mask << 1) == 0:
                        ans = max(ans, bit_count(mask) + dp(i + 1, mask))

            return ans

        return dp(0, 0)

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])

        valid_seats = [0] * m  # n bits
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    valid_seats[i] |= (1 << j)

        @lru_cache(None)
        def dp(i, prev_mask):
            if i == m:
                return 0
            ans = 0
            mask = valid_seats[i]
            while mask >= 0:  # loop through all possible subsets of 1 bits combinations in mask, must include 0 (empty set), as some rows might have no students
                if mask & valid_seats[i] == mask and mask & (mask << 1) == 0 and prev_mask & (
                        mask << 1) == 0 and prev_mask & (mask >> 1) == 0:
                    ans = max(ans, bin(mask).count('1') + dp(i+1, mask))
                if mask == 0: # avoid infinite loop, as empty is always subset of empty
                    break
                mask = (mask - 1) & valid_seats[i]

            return ans

        return dp(0, 0)


def main():
    sol = Solution()
    assert sol.maxStudents([["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]) == 4, 'fails'

    assert sol.maxStudents([[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]) == 3, 'fails'

    assert sol.maxStudents([["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]) == 10, 'fails'


if __name__ == '__main__':
   main()