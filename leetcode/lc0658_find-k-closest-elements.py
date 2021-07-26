"""
658. Find K Closest Elements
Medium

2941

350

Add to List

Share
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4

"""
from typing import List

"""
Heap

put arr[i]-x into heap, pop smallest for k times

time O(N+k*log(N))
"""
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hq = [(abs(a - x), a) for i, a in enumerate(arr)]
        heapq.heapify(hq)

        ans = []
        while k:
            ans.append(heapq.heappop(hq)[1])
            k -= 1

        return sorted(ans)


def main():
    sol = Solution()
    assert sol.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3) == [1, 2, 3, 4], 'fails'

    assert sol.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1) == [1, 2, 3, 4], 'fails'

if __name__ == '__main__':
   main()