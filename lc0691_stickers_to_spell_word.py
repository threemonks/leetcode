"""
691. Stickers to Spell Word
Hard

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.

"""
import collections
import math
from functools import lru_cache
from typing import List

"""
1. BitMask主要用于表示组合(的状态)
0表示该位置(idx)没有被取
1表示该位置(idx)已经被取

2. 在Java里面 Integer只有32位
所以数据量超过32位的都不太好用BitMask做
(Java里可以使用BitSet应付超过32位的情况 但不是很方便)


3. 基本操作
bitMask & (1 << idxBit) == 0 用于检测`idxBit`位置是否被取
bitMask | (1 << idxBit) 用于取`idxBit`位置
"""

"""
DP 背包 状态压缩 bitmask
"""
"""
observation that can speed up:

1. for all stickers, we can ignore any letters that are not in target word
2. if a sticker dominates another, we shouldn't include the dominated sticker in our sticker collection. A dominates B if A.count(letter) >= B.count(letter) for all letters

idea

use bitmask to represent weather a given letter of target has been included or not
dp[i] := minimum number of stickers required to get to state i of target

for each state i, and for each word st, can this word get the state to a new state j, and what's the dp of this new state
dp[j] = min(dp[j], dp[i]+1)

Time Complexity: O(2^T * S * T) - S be the total number of letters in all stickers, and TT be the number of letters in the target word
Space Complexity: O(2^T)

"""

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        t_count = collections.Counter(target)
        # remove letters from sticker that do not appear in target
        # also count letters in sticker
        A = [collections.Counter(sticker) & t_count for sticker in stickers]
        # print('A=%s' % str(A))

        # remove dominated sticker(s)
        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        # print('A=%s' % str(A))

        stickers = ["".join(s_count.elements()) for s_count in A]
        print('stickers=%s' % str(stickers))

        def get_new_state(target, i, st):
            """
            new state we can achieve, given curernt state i, and new word st
            idea:
            for each char in st, for each ch in target, is it set in state i, if not, does this char from st set that bit in i? if so, set it
            """
            n = len(target)
            for ch in st:
                for k in range(n):
                    if ((i & (1 << k)) == 0) and ch == target[k]:
                        i += (1 << k)
                        break
            return i

        n = len(target)
        N = (1 << n)  # number of states
        dp = [math.inf for _ in range(N)]
        dp[0] = 0

        for i in range(N):
            if dp[i] == math.inf:
                continue
            for st in stickers:
                # get new state
                #j = get_new_state(target, i, st)
                j = i
                for ch in st:
                    for k in range(n):
                        if ((j & (1 << k)) == 0) and ch == target[k]:
                            j |= (1 << k)
                            break
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[N - 1] if dp[N - 1] != math.inf else -1


"""
leetcode solutions
Time Complexity: O(2^T * S * T) where SS be the total number of letters in all stickers, and TT be the number of letters in the target word. We can examine each loop carefully to arrive at this conclusion.
Space Complexity: O(2^T), the space used by dp.

"""
class Solution1(object):
    def minStickers(self, stickers, target):
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]


def main():
    sol = Solution()
    assert sol.minStickers(["with", "example", "science"], "thehat") == 3, 'fails'

    assert sol.minStickers(["notice", "possible"], "basicbasic") == -1, 'fails'

if __name__ == '__main__':
   main()