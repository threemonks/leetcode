
from functools import lru_cache
"""
区间DP
"""

class Solution:
    def func(self):
        @lru_cache(None)
        def dfs(nums, start, end):
            if start > end:
                return 0
            ans = 0
            for i in range(start, end+1):
                left = dfs(nums, start, i+1)
                right = dfs(nums, i+1, end+1)
                ans = max(ans, i+left+right) # some function

            return ans