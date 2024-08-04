from functools import lru_cache

class Solution0:
    """ K size subsets """
    def unique_ways(self, counts, k):
        n = len(counts)
        nums = []
        for i in range(n):
            cnt = min(10, counts[i])
            while cnt:
                nums.append(i)
                cnt -= 1

        res = 0
        def backtrack(nums, l):
            nonlocal res
            # base case
            if l == k:
                return 1
            ans = 0
            for i in range(len(nums)):
                if i>=1 and nums[i] == nums[i-1]:
                    continue
                ans += backtrack(nums[i+1:], l+1)

            return ans
        res = backtrack(nums, 0)
        return res

"""
thoughts
we need total of k numbers
we can pick 0, 1, 2, ..., counts[i] i's, 
then we have k-counts[i] remaining spots that we can pick from i+1 and later numbers
sum all the ways we pick 0, 1, 2, ..., counts[i] will be the answer

base case:
if picked k numbers, it is 1 unique way
if we reached last digit, stop

"""
class Solution:
    def unique_ways(self, counts, k):
        n = len(counts)
        MOD = 10**9+7

        def backtrack(counts, k, index):
            # k is remaining number of numbers to pick
            # index is current numbers being explored
            print('k=%s index=%s' % (k, index))
            # base case
            if k == 0: return 1
            if index == len(counts): return 0

            ans = 0
            for i in range(counts[index]+1):
                if k-i < 0: return ans
                ans += backtrack(counts, k-i, index+1)
            print('ans=%s' % ans)
            return ans % MOD

        return backtrack(counts, k, 0)

class Solution2:
    def get_count(self, n, numbers):
        total = 0
        if len(numbers) < 1 or sum(numbers) < n:
            return total
        if len(numbers) == 1:
            if numbers[0] >= n:
                return 1
            else:
                return 0

        c = numbers[0]

        for i in range(min(c, n), -1, -1):
            total += self.get_count(n-i, numbers[1:])

        return total

def main():
    sol = Solution()

    assert sol.unique_ways([5,6,1], k=10) == 5
    # print(sol.unique_ways([1,1,1,1,1, 1,1,1,1,2], k=10))
    assert sol.unique_ways([2, 2, 1], k=3) == 5
    # assert sol.unique_ways([1,1,1,1,1, 1,1,1,1,2], 10) == 10

    # assert sol.get_count(3, [2, 3, 1]) == 6, 'fails'

if __name__ == "__main__":
    main()