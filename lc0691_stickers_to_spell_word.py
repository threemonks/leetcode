"""
691. Stickers to Spell Word
Hard

438

40

Add to List

Share
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
idea
use bitmask to represent weather a given letter of target has been included or not
dp[i] := minimum number of stickers required to get to state i of target

for each state i, and for each word st, can this word get the state to a new state j, and what's the dp of this new state
dp[j] = min(dp[j], dp[i]+1)


"""


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        n = len(target)
        N = (1 << n)  # number of states
        dp = [math.inf for _ in range(N)]
        dp[0] = 0

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

        for i in range(N):
            if dp[i] == math.inf:
                continue
            for st in stickers:
                j = get_new_state(target, i, st)
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[N - 1] if dp[N - 1] != math.inf else -1


def main():
    sol = Solution()
    assert sol.minStickers(["with", "example", "science"], "thehat") == 3, 'fails'

    assert sol.minStickers(["notice", "possible"], "basicbasic") == -1, 'fails'

if __name__ == '__main__':
   main()