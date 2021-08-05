"""
373. Find K Pairs with Smallest Sums
Medium

2233

141

Add to List

Share
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000
"""
from typing import List

"""
Heap

idea:
similar to a k sorted list merge, with k sorted lists being

nums1[0], nums2[0] -> nums1[1], nums2[0] -> nums1[2], nums2[0] -> ...
nums1[0], nums2[1] -> nums1[1], nums2[1] -> nums1[2], nums2[1] -> ...
nums1[0], nums2[2] -> nums1[1], nums2[2] -> nums1[2], nums2[2] -> ...
...

so to solve this, we add head of each list (node being a pair index) into pq (along with pair sum as sorting field), and keep pop the smallest one, until we get k items


"""
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)

        if not m or not n:
            return []

        ans = []
        pq = []  # min heapq sorted by pair sum

        # add all [0, 0], [0, 1], [0, 2] ... into pq
        for i in range(m):
            heapq.heappush(pq, [nums1[i] + nums2[0], i, 0])

        while k and pq:
            pair = heapq.heappop(pq)
            ans.append([nums1[pair[1]], nums2[pair[2]]])
            i, j = pair[1], pair[2]
            # next better pair could be A: {after(nums1), nums2} or B: {nums1. after(nums2)}
            # but we already added all nums1*, so we should only add after(nums2)
            j += 1
            if j < n:
                heapq.heappush(pq, [nums1[i] + nums2[j], i, j])
            k -= 1

        return ans


def main():
    sol = Solution()
    assert sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3) == [[1,2],[1,4],[1,6]], 'fails'

    assert sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2) == [[1,1],[1,1]], 'fails'

    assert sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3) == [[1,3],[2,3]], 'fails'

if __name__ == '__main__':
   main()