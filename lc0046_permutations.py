"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""
"""
dfs/backtracking
iterate through the nums list, pick the first element, append it to current running partial list (a path from tree root to current node), to build new partial list, along with remaining elements of nums, to pass into recursive call.
If the running partial list has expected length, add it to result list
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(arr, path, res):
            nonlocal n
            if len(path) == n:
                res.append(path)
            for i in range(len(arr)):
                dfs(arr[:i] + arr[i+1:], path + [arr[i]], res)

        res = []
        dfs(nums, [], res)
        return res

def main():
    sol = Solution()
    assert sol.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], 'fails'

    assert sol.permute([0,1]) == [[0,1],[1,0]], 'fails'

    assert sol.permute([1]) == [[1]], 'fails'

if __name__ == '__main__':
   main()