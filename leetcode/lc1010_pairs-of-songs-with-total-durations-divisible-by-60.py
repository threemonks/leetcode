"""
1010. Pairs of Songs With Total Durations Divisible by 60
Medium

1549

89

Add to List

Share
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
"""
from typing import List

"""
Hash Table

Observation:
1. we only need to consider song length % 60
2. for each song length l%60=r, if 60-r exists in known maps, then it adds # of pairs: maps[60-r]
   special handling of 0, which adds maps[0] count of pairs
3. then update remainder counts:
    maps[r] += 1

time O(N)
"""
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        maps = defaultdict(int)
        ans = 0

        for t in time:
            r = t % 60
            if r == 0:
                ans += maps[0]
            elif 60 - r in maps:
                ans += maps[60 - r]
            # update remainder count
            maps[r] += 1

        return ans

def main():
    sol = Solution()
    assert sol.numPairsDivisibleBy60(time = [30,20,150,100,40]) == 3, 'fails'

    assert sol.numPairsDivisibleBy60(time = [60,60,60]) == 3, 'fails'

if __name__ == '__main__':
   main()