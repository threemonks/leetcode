"""
526. Beautiful Arrangement
Medium

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.



Example 1:

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 15
"""
"""
Permutations via Backtrack brutal force

take first number from remaining array, insert into each position in running partial path, to create new partial path
base case: len(path) == n
note only return valid permutations

time O(N!) - bounded by total number of possible permutations (though there are pruning due to beautiful requirement)
space O(N) - depth of tree

TLE

mistakes:
1. perm is 1-indexed, so when loop with index, we need to shift index i
"""


class Solution0:
    def countArrangement(self, n: int) -> int:
        result = []

        def dfs(path, k):
            if len(path) == n:
                if all([(p % (i + 1) == 0 or (i + 1) % p == 0) for i, p in enumerate(path)]):
                    result.append(path)
                return
            if k == n + 1:
                return

            for i in range(len(path) + 1):
                dfs(path[:i] + [k] + path[i:], k + 1)

        dfs([], 1)

        return len(result)


"""
Permutations via Backtrack brutal force

take any number from remaining elements k through n, append to current permutation result path, to form a new partial result, then recursive call with new index k+1
base case: len(path) == n
note only return valid permutations

TLE

time O(N!) - bounded by total number of possible permutations (though there are pruning due to beautiful requirement)
space O(N) - depth of tree

"""


class Solution1:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        result = []

        def dfs(path, nums):
            if len(path) == n:
                if all([(p % (i + 1) == 0 or (i + 1) % p == 0) for i, p in enumerate(path)]):
                    result.append(path)
                return
            if not nums:
                return

            for i in range(len(nums)):
                dfs(path + [nums[i]], nums[:i] + nums[i + 1:])

        dfs([], nums)

        return len(result)


"""
Permutations via Backtrack brutal force with early pruning

observation:
the above brutal force backtrack to general all possible permutations and only check if valid at very end would TLE, lets prune at time of insertion any element tha would violate the beautiful requirement

take any number from remaining elements k through n, append to current permutation result path, to form a new partial result, then recursive call with new index k+1
base case: len(path) == n
note only return valid permutations

time O(N!) - bounded by total number of possible permutations (though there are pruning due to beautiful requirement)
space O(N) - depth of tree

"""


class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        result = []

        def dfs(path, nums):
            if len(path) == n:
                result.append(path)
                return
            if not nums:
                return

            for i in range(len(nums)):
                if nums[i] % (1 + len(path)) == 0 or (1 + len(path)) % nums[i] == 0:
                    dfs(path + [nums[i]], nums[:i] + nums[i + 1:])

        dfs([], nums)

        return len(result)


def main():
    sol = Solution()
    assert sol.countArrangement(2) == 2, 'fails'

    assert sol.countArrangement(1) == 1, 'fails'


if __name__ == '__main__':
   main()