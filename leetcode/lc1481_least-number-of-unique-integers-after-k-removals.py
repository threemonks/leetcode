"""
1481. Least Number of Unique Integers after K Removals
Medium

481

48

Add to List

Share
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.



Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
from typing import List

"""
Greedy

we want to greedily remove those integers with less count first

note:
can use bucket sort (bucket.size = len(arr)) to obtain O(1) time complexity

time O(Nlog(N)) # sort
"""
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)

        counts = sorted([(count, num) for num, count in counter.items()])

        n = len(counts)
        removed = 0
        for i in range(n):
            removed += counts[i][0]
            if removed > k:
                return n - i
            elif removed == k:
                return n - i - 1


def main():
    sol = Solution()
    assert sol.findLeastNumOfUniqueInts(arr = [5,5,4], k = 1) == 1, 'fails'

    assert sol.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3) == 2, 'fails'


if __name__ == '__main__':
   main()