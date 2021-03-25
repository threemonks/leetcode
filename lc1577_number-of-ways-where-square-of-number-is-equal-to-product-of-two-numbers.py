"""
1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
Medium

Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.


Example 1:

Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8).
Example 2:

Input: nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explanation: All Triplets are valid, because 1^2 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
Example 3:

Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
Output: 2
Explanation: There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].
Example 4:

Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
Output: 0
Explanation: There are no valid triplets.


Constraints:

1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 10^5


"""
import collections
from typing import List

"""
Hash Table / Counter
"""


class Solution0:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def count(nums1, nums2):
            ans = 0
            counter2 = collections.Counter(nums2)
            for n1 in nums1:
                target = n1 ** 2
                for n2 in counter2:
                    n3 = target // n2
                    if target % n2 or n3 not in counter2:
                        continue
                    if n3 == n2:  # square in nums2
                        ans += counter2[n2] * (counter2[n2] - 1)
                    elif n3 != n2:
                        ans += counter2[n2] * counter2[n3]

            return ans // 2  # (n1, n2, n3) and (n1, n3, n2) is considered one triplet

        return count(nums1, nums2) + count(nums2, nums1)


"""
Hash Table / Counter

precompute counter/hash table for squares
"""


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        cnt1 = collections.Counter([num * num for num in nums1])

        cnt2 = collections.Counter([num * num for num in nums2])

        ans = 0
        for i in range(n1):
            for j in range(i + 1, n1):
                p = nums1[i] * nums1[j]
                ans += cnt2[p]

        for i in range(n2):
            for j in range(i + 1, n2):
                p = nums2[i] * nums2[j]
                ans += cnt1[p]

        return ans


def main():
    sol = Solution()
    assert sol.numTriplets(nums1 = [7,4], nums2 = [5,2,8,9]) == 1, 'fails'

    assert sol.numTriplets(nums1 = [1,1], nums2 = [1,1,1]) == 9, 'fails'

    assert sol.numTriplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7]) == 2, 'fails'

    assert sol.numTriplets(nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]) == 0, 'fails'

if __name__ == '__main__':
   main()