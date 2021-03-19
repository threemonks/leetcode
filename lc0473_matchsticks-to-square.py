"""
473. Matchsticks to Square
Medium

"""
from functools import lru_cache
from typing import List

"""
DFS

observation:
if total length % 4 != 0, then false

time O(4^N)
space O(N)

TLE

mistakes:
1. keep sums that records edge length of each side, just as a variable outside of the recursive call, no need to pass as parameter
"""


class Solution0:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or sum(nums) % 4 != 0:
            return False

        n = len(nums)
        maxlen = sum(nums) / 4

        nums.sort(reverse=True)

        edges = [0 for _ in range(4)]

        def dfs(i):
            # use up to i-th stick, how many sides we bult so far
            nonlocal nums, edges
            if any([edge > maxlen for edge in edges]):
                return False

            if i == n and edges[0] == edges[1] == edges[2] == edges[3] == maxlen:
                return True
            # try adding i-th stick to any one side
            for j in range(4):
                if edges[j] + nums[i] <= maxlen:
                    # update this edge
                    edges[j] += nums[i]

                    # explore this case
                    if dfs(i + 1):
                        return True
                    # undo the change / backtrac
                    edges[j] -= nums[i]

            # none worked
            return False

        return dfs(0)


"""
DP bitmask

observation, when some sides are completely formed, then later problem can reuse those completed sides as sub problem
and the complete dp state would need to know which sticks have been used, and which sides have been completed, but we don't need to keep track of which stick is used in which side (as that does not matter)

Given the constrain on number of sticks, 15, we can use bitmask to represent which stick is used, that is 2^15 states

dp[bitmask][sides] := using all sticks marked as 0 bit in bitmask, we are able to complete # of sides.

Also note since we know the total length is k*4, so if we form three sides with expected length, then it is successful.

pseudo code:

edge = sum(nums)/4
def dp(stickused, sides):
    # stick used bitmask, # sides completed
    if sides == 3:
        return True
    for stick in unused stick:
        add stick to stickused
        result = dp(stickused, sides_updated)
        if result:
            return True
        remove stick from stickused

    return False

"""


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or sum(nums) % 4 != 0:
            return False

        n = len(nums)
        edgelen = sum(nums) / 4

        nums.sort(reverse=True)
        fullmask = (1 << n) - 1

        edges = [0 for _ in range(4)]

        @lru_cache(None)
        def dp(bitmask, sides):
            # bitmask of stick used, 0 means used, 1 means still available, sides completed so far
            nonlocal nums
            # calculate how many sides does this state complete
            total = 0
            for i in range(n):
                if (1 << i) & bitmask == 0:
                    total += nums[n - 1 - i]

            if total > 0 and total % edgelen == 0:
                sides += 1

            # print('bitmask=%s sides=%s' % (bin(bitmask), sides))

            # needs to check total==edgelen*3 to avoid we jump from 2 sides complete to 4 sides
            # exampl e[2,2,2,2,2,6]
            if sides == 3 and total == edgelen * 3:
                return True

            # now try add each one of the remaining stick, and see if we can get to 3 sides complete
            ans = False

            # each 1 bit represents a stick not used
            for i in range(n):
                if (1 << i) & bitmask:  # this stick available
                    if dp(bitmask ^ (1 << i), sides):  # turn off i-th bit from right in bitmask
                        ans = True
                        break

            return ans

        return dp(fullmask, 0)


def main():
    sol = Solution()
    assert sol.makesquare([1,1,2,2,2]) == True, 'fails'

    assert sol.makesquare([3,3,3,3,4]) == False, 'fails'

if __name__ == '__main__':
   main()