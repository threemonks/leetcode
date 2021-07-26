"""
1569. Number of Ways to Reorder Array to Get Same BST
Hard

Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
Example 2:

Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST:
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
Example 4:

Input: nums = [3,1,2,5,4,6]
Output: 19
Example 5:

Input: nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
Output: 216212978
Explanation: The number of ways to reorder nums to get the same BST is 3216212999. Taking this number modulo 10^9 + 7 gives 216212978.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.
"""
from typing import List

"""
DP

[3, 4, 5, 1, 2] // original array with root value is 3

[1, 2] // left sub-sequence, left_len = 2
[4, 5] // right sub-sequence, right_len = 2

first number 3 is root, all smaller numbers go to left subtree, all larger numbers go to right subtree, so we need to find number of ways to merge left and right subtree while keeping the relative order of numbers within the subtree unchanged
the number of ways to merge two arrays with length m and n, while keeping the elements order within one array unchanged, is C(m+n, m), which is the binomial coefficient (from Pascal triangle)

C(n, k) = n!/(k!*(n-k)!)

So we can take the root, calculate how many ways to order left subtree (left_count), how many ways to order right subtree (right_count), and how many ways to merge them, so the total would be (# of ways to merge * left_count * right_count)

number of ways to merge left (length m) and right subtrees (length n): consider total m+n elements, we need to pick m positions to place left subtree elements, then the remaining n positions for right subtree is also determined, so the total number of ways is 

C(m+n, m) = (m+n)!/(m!*n!)

let left_len = m, right_len = n, so the recursive relationship of total number of ways are:

left_count*right_count*(left_len+right_len)!//(left_len!*right_len!)

final result is dp(nums)-1 as we don't count the original

"""
import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 1000000007

        def dp(nums):
            if len(nums) <= 1:
                return 1

            root = nums[0]
            left = [num for num in nums if num < root]
            right = [num for num in nums if num > root]
            left_len = len(left)
            if left_len:
                left_count = dp(left)
            else:
                left_count = 1

            right_len = len(right)
            if right_len:
                right_count = dp(right)
            else:
                right_count = 1

            return left_count * right_count * (math.factorial(left_len + right_len) // (
                        math.factorial(left_len) * math.factorial(right_len))) % MOD

        return dp(nums) % MOD - 1

def main():
    sol = Solution()
    assert sol.numOfWays(nums = [2,1,3]) == 1, 'fails'

    assert sol.numOfWays(nums = [3,4,5,1,2]) == 5, 'fails'

    assert sol.numOfWays(nums = [1,2,3]) == 0, 'fails'

    assert sol.numOfWays(nums = [3,1,2,5,4,6]) == 19, 'fails'

    assert sol.numOfWays(nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]) == 216212978, 'fails'

if __name__ == '__main__':
   main()