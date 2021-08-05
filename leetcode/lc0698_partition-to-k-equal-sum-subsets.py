"""
698. Partition to K Equal Sum Subsets
Medium

3420

202

Add to List

Share
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 10^4
The frequency of each element is in the range [1, 4].

"""
from typing import List

"""
Backtrack

fill all nums from largest to smallest

TLE

note:
1. sort nums reverse
2. iterate sorted nums from large to small one by one, the dfs function is iterating, no need to try all different numbers from idx .. n again within dfs

Two Game Changers in This Solution:

1, if sums[j] == 0: break

The key is, sums[j] == 0 means for all k > j, sum[k] == 0; because this algorithm always fill the previous buckets before trying the next.
So if by putting nums[i] in this empty bucket can't solve the game, putting nums[i] on other empty buckets can't solve the game either.
2, nums.sort(reverse=True)

Always start from big numbers for this kind of problem, just by doing it yourself for a few times you will find out that the big numbers are the easiest to place.

NP hard problem
time complexity: O(N^k)
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums = sorted(nums, reverse=True)  # try large numbers first, this is usually more optimal than not sorting
        sums = sum(nums)
        if sums % k != 0:
            return False

        buckets = [0 for _ in range(k)]

        target = sums // k
        n = len(nums)

        def dfs(idx):
            # which bucket should current num idx be put into to get a valid solution?
            if idx == n and set(buckets) == set([target]):
                return True
            for j in range(k):
                # try to add number idx into bucket[j]
                buckets[j] += nums[idx]
                if buckets[j] <= target and dfs(idx + 1):
                    return True
                buckets[j] -= nums[idx]
                # if nums[idx] does not work when we put it into a empty bucket
                # there's no need to try to put it into any other empty bucket
                if buckets[j] == 0:
                    break

            return False

        return dfs(0)


class Solution1:
    def canPartitionKSubsets(self, nums, k):
        buckets = [0] * k
        target = sum(nums) // k

        # We want to try placing larger numbers first
        nums.sort(reverse=True)

        # DFS determines which bucket to put the 'current element' (nums[idx] ) into
        def dfs(idx):
            # If we've placed all of the items, we're done;
            # check if we correctly made k equal subsets of
            # size sum(nums) // k
            if idx == len(nums):
                return set(buckets) == set([target])

            # For each bucket
            for i in range(k):
                # Try adding the current element to it
                buckets[i] += nums[idx]

                # If it's a valid placement and we correctly placed the next element, we're
                # done placing the current element.
                if buckets[i] <= target and dfs(idx + 1):
                    return True

                # Otherwise, remove the current element from the ith bucket and
                # try the next one.
                buckets[i] -= nums[idx]

                # This is an optimization that is not strictly necessary.
                # If bucket[i] == 0, it means:
                #   - We put nums[idx] into an empty bucket
                #   - We tried placing every other element after and failed.
                #   - We took nums[idx] out of the bucket, making it empty again.
                # So trying to put nums[idx] into a _different_ empty bucket will not produce
                # a correct solution; we will just waste time (we place elements left to right,
                # so if this bucket is now empty, every one after it is too).
                #
                # Otherwise (bucket[i] > 0), we just go to the next bucket and
                # try placing nums[idx] there. If none of them work out, we wind up
                # breaking out of the loop when range(k) ends and returning False.
                if buckets[i] == 0:
                    break

            # We couldn't place the current element anywhere that
            # leads to a valid solution, so we will need to backtrack
            # and try something else.
            return False

        # Start by trying to place nums[0]
        return dfs(0)

def main():
    sol = Solution()
    assert sol.canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4) == True, 'fails'

    assert sol.canPartitionKSubsets(nums = [1,2,3,4], k = 3) == False, 'fails'


if __name__ == '__main__':
   main()