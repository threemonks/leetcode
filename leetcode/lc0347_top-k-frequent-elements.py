"""
347. Top K Frequent Elements
Medium

5443

286

Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List

"""
Bucket Sort

1. there's at most n distinct numbers, so create n buckets
2. put each number into its bucket based on its freq count
3. concatenate lists of buckets for index from n to 0, until we have accumulated ans of length >= k, then break

"""
from collections import Counter


class Solution0:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)

        buckets = [[] for _ in range(n + 1)]

        for num, count in counter.items():
            buckets[count].append(num)

        ans = []
        for i in range(n, -1, -1):
            ans.extend(buckets[i])
            if len(ans) >= k:
                break

        return ans


"""
Heap

sort, store (-count, num) into heap, keep pop until we get k numbers

"""
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)

        hq = []

        for num, count in counter.items():
            heapq.heappush(hq, [-count, num])

        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(hq)[1])

        return ans


def main():
    sol = Solution()
    assert sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1, 2], 'fails'

    assert sol.topKFrequent(nums = [1], k = 1) == [1], 'fails'


if __name__ == '__main__':
   main()