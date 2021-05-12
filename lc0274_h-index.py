"""
274. H-Index
Medium

912

1499

Add to List

Share
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000

"""
from typing import List

"""
Binary Search

sort citations, then binary search for index where citations[i] >= n-i

time O(log(N))
"""


class Solution0:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)

        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if citations[mid] >= n - mid:
                hi = mid
            else:
                lo = mid + 1

        return n - lo


"""
Hash Table

papers: sum of all counts with citations >= k, or number of papers having at least k citations, then h-index is largest k s.t. k<=papers[k]

"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)
        # count papers for each citation
        for c in citations:
            papers[min(n, c)] += 1

        # find h-index
        k = n
        s = papers[n]
        while k > s:
            k -= 1
            s += papers[k]

        return k

def main():
    sol = Solution()
    assert sol.hIndex(citations = [3,0,6,1,5]) == 3, 'fails'

    assert sol.hIndex(citations = [1,3,1]) == 1, 'fails'

if __name__ == '__main__':
   main()