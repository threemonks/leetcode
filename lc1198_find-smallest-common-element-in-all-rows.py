"""
1198. Find Smallest Common Element in All Rows
Medium

Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.



Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5


Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in strictly increasing order.

"""
import math
from collections import defaultdict
from typing import List
from collections import defaultdict
"""
Hash Table
"""

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n = len(mat)
        freq = defaultdict(int)

        for i in range(n):
            for j in range(len(mat[i])):
                freq[mat[i][j]] += 1

        mx = math.inf
        for key in freq.keys():
            if freq[key] == n:
                mx = min(mx, key)

        return mx if mx < math.inf else -1


def main():
    sol = Solution()
    assert sol.smallestCommonElement(mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]) == 5, 'fails'


if __name__ == '__main__':
   main()