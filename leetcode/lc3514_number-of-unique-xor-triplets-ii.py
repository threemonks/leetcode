"""
3514. Number of Unique XOR Triplets II
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).

 

Example 1:

Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:

(0, 0, 0) → 1 XOR 1 XOR 1 = 1
(0, 0, 1) → 1 XOR 1 XOR 3 = 3
(0, 1, 1) → 1 XOR 3 XOR 3 = 1
(1, 1, 1) → 3 XOR 3 XOR 3 = 3
The unique XOR values are {1, 3}. Thus, the output is 2.

Example 2:

Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.

 

Constraints:

1 <= nums.length <= 1500
1 <= nums[i] <= 1500

"""
"""
bitmanipulation

unique value is either nums[i], or nums[i]^nums[j]^nums[k] where i < j < k

create a double_xor list, and use value from that list to xor with each nums[k] to get new triplets
use one loop to track the update to triplets, as well as addition to double_xor (for pairs ending with nums[k])

time O(n^2)
"""
from leetcode.lc_tools import almost_equal


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        single_xor = set(nums) # count all nums[i]
        double_xor = set() # paris we've seen so far
        triplets = set(single_xor) #include singles in answer

        for k in range(n):
            num_k = nums[k]

            # generate triplets from current k + existing_doubles
            for dx in double_xor:
                triplets.add(dx ^ num_k)

            # add new doubles ending at k
            for i in range(k):
                double_xor.add(nums[i] ^ num_k)

        return len(triplets)    



def main():
    sol = Solution()
    assert almost_equal(sol.uniqueXorTriplets(nums=[1,3]), 2), 'fails'

    assert almost_equal(sol.uniqueXorTriplets(nums = [6,7,8,9]), 4), 'fails'

if __name__ == '__main__':
   main()
