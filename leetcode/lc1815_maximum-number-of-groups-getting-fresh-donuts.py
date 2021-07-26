"""
1815. Maximum Number of Groups Getting Fresh Donuts
Hard

There is a donuts shop that bakes donuts in batches of batchSize. They have a rule where they must serve all of the donuts of a batch before serving any donuts of the next batch. You are given an integer batchSize and an integer array groups, where groups[i] denotes that there is a group of groups[i] customers that will visit the shop. Each customer will get exactly one donut.

When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.

You can freely rearrange the ordering of the groups. Return the maximum possible number of happy groups after rearranging the groups.



Example 1:

Input: batchSize = 3, groups = [1,2,3,4,5,6]
Output: 4
Explanation: You can arrange the groups as [6,2,4,5,1,3]. Then the 1st, 2nd, 4th, and 6th groups will be happy.
Example 2:

Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
Output: 4


Constraints:

1 <= batchSize <= 9
1 <= groups.length <= 30
1 <= groups[i] <= 10^9
"""

from typing import List
from functools import lru_cache

"""
DP / Greedy

Note the problem is to find way to group numbers into group g, so that as many as possible group sums are divisble by batchSize B.

steps:
1. for all numbers that are divisble by B, add 1 to answer, because it gives one group that can have fresh donuts.
2. we need to keep the remaining, num%B, for num > B, as they need to be in next group (causing next nums in this group get no fresh donuts)
3. greedily count all complimentary sizes (two group size adds up to B), each such pair would gives one group fresh donuts res+=1 (this step improves performance, but is not necessary)
4. for all remaining group sizes (all < B), brutal force (dfs) find

"""


class Solution:
    def maxHappyGroups(self, B: int, groups: List[int]) -> int:
        n = len(groups)

        # first calculate all groups that require donut count % B == 0, they add one group who get fresh donut
        ans = sum([g % B == 0 for g in groups])

        # filter out any group that whose donut count are multiple of B, and replace groups' remaining groups donut requirements with g%B (remainder after served some batches)
        groups = [g for g in groups if g % B]

        # how many group needs 1, 2, ..., B-1 donuts
        pos = [0 for _ in range(B)]
        for g in groups:
            pos[g % B] += 1

        # this is not necessary to pass
        # pair up compplimentary sizes
        # either pair up two different complimentary size, or pair up same size
        i, j = 1, B - 1
        while i <= j:  # i+j==B
            t = min(pos[i], pos[j]) if i != j else pos[i] // 2
            ans += t
            pos[i] -= t
            pos[j] -= t
            i, j = i + 1, j - 1

        # now in pos, we should have at least half elements being zero
        if sum(pos) == 0:
            return ans

        @lru_cache(None)
        def dfs(state, prev):
            # given state (state[1] = 2 means 2 group needs 1 donut)
            # prev how many donuts in this batch left from prevoius group consumption
            if sum(state) == 0:  # no more group requires donut
                return 0
            res = 0
            for i, s in enumerate(state):
                # consider this group i with remaining donut count s
                if state[i] <= 0:
                    continue
                tmp_state = list(state)
                tmp_state[i] -= 1

                rem = (prev + i) % B
                # explore further after considering group i with remaining required donut count s
                # we visit next iteration with (prev+s)%B, i.e., counts that cannot be fulfilled by current donut batch
                # prev==0 means starting next group afresh
                res = max(res, dfs(tuple(tmp_state), rem) + (prev == 0))

                # backtrack # not necessary
                tmp_state[i] += 1

            return res

        ans += dfs(tuple(pos), 0)

        return ans


def main():
    sol = Solution()
    assert sol.maxHappyGroups(3, groups = [1,2,3,4,5,6]) == 4, 'fails'

    assert sol.maxHappyGroups(3, groups = [1,3,2,5,2,2,1,6]) == 4, 'fails'


if __name__ == '__main__':
   main()