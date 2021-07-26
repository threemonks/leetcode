"""
275. H-Index II
Medium

547

844

Add to List

Share
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in an ascending order, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.



Example 1:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,2,100]
Output: 2


Constraints:

n == citations.length
1 <= n <= 105
0 <= citations[i] <= 1000
citations is sorted in ascending order.

"""
from typing import List

"""
Binary Search

binary search for index where citations[i] >= n-i

time O(log(N))
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if citations[mid] >= n - mid:
                hi = mid
            else:
                lo = mid + 1

        return n - lo

def main():
    sol = Solution()
    assert sol.hIndex(citations = [0,1,3,5,6]) == 3, 'fails'

    assert sol.hIndex(citations = [1,2,100]) == 2, 'fails'

if __name__ == '__main__':
   main()