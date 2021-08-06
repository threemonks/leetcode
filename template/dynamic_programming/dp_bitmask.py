from functools import lru_cache

class Solution:
    def myfunc(nums, cost):
        nums = [1,2,3,4]
        n = len(nums)
        full_mask = (1<<n)-1

        ans = 0
        @lru_cache(None)
        def dp(i, mask):
            if mask == full_mask:
                return 1
            for j in [1,2,3]: # loop all possible j's
                if mask & (1<<j): # skip some neighbors if necessary
                    continue
                ans = max(ans, cost[i][j]+dp(i+1, mask | (1<<j))) # combine current answer with answer from next recursive dp call result, parameter for next level call is i+1 (skip current node), and mask|(1<<j), which is the new state to use after this node operation

            return ans

        return dp(0, 0)