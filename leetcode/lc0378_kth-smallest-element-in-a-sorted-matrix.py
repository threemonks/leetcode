"""
378. Kth Smallest Element in a Sorted Matrix
Medium

4452

205

Add to List

Share
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n^2
"""
from typing import List

"""
Heap

use min heap, keep heap size <= k, and keep push elements into heap, and pop when size > k

time complexity: O(nlogk)
space O(k)
"""
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        q = []

        for i in range(m):
            for j in range(n):
                heapq.heappush(q, -matrix[i][j])
                if len(q) > k:
                    heapq.heappop(q)

        return -q[0]


def main():
    sol = Solution()
    assert sol.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8) == 13, 'fails'

    assert sol.kthSmallest(matrix = [[-5]], k = 1) == -5, 'fails'

if __name__ == '__main__':
   main()