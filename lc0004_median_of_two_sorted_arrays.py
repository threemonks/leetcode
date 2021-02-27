"""
4. Median of Two Sorted Arrays
Hard

https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
from typing import List

"""
Binary Search

idea

Two find media, is to split the sorted array into two parts, where number of items in left part equals to number of items in right part, and largest item in left part are less than smallest item in right part.

For given array A of length m, there's m+1 way to cut it, i.e., cut at i = 0, 1, ..., m, which corresponds to left part length 0, 1, 2, ..., m.

For this problem, we have two sorted arrays, A, and, B, lets say we cut A at index i, and cut B at index j, and split into two parts

     left part          |    right part

A[0], A[1], ..., A[i-1] | A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1] | B[j], B[j+1], ..., B[n-1]

for this cut to help us identify median, we need the cut to meet the following two conditions:

1. len(left part) == len(right part)
2. max(left part) <= max(right part)

Once we have this two conditions met, we then have media = (max(left part) + min(rigt part))/2

With the above cut A cut between i-1 and i, B cut between j-1 and j, the two conditions above are equivalent to:
1. 2*(i+j) = (m+n) or (m+n+1) if m+n is odd <=> assume m > n, then for i = 0, ..., m, we need j = (m+n+1)/2 - i
2. A[i-1] <= B[j] and B[j-1] <= A[i]

So the process is:
search i in range(0, m+1), find i such that
    j = (m+n+1)/2 - i and A[i-1] <= B[j] and B[j-1] <= A[i]

https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
https://zhuanlan.zhihu.com/p/70654378


"""


class Solution0:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # we need to make sure n > m so that j=(m+n+1)//2 - i is not negative
        # we swap A and B if necessary
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)

        m, n = len(A), len(B)

        ans = None
        lo, hi = 0, m + 1  # left inclusive, right exclusive
        while lo <= hi:
            i = lo + (hi - lo) // 2
            j = (m + n + 1) // 2 - i
            if 0 <= i - 1 < m and 0 <= j < n and A[i - 1] > B[
                j]:  # needs to decrease i because A[i-1] too big, to decrease i, we decrease hi
                hi = i - 1
            elif 0 <= i < m and 0 <= j - 1 < n and B[j - 1] > A[
                i]:  # needs to decrease j because B[j-1] too big, to decrease j, we need to increase i
                lo = i + 1
            else:  # (0<=i-1<m and 0<=j<n and A[i-1] <= B[j]) and (0<=i<m and 0<=j-1<n and B[j-1] <= A[i]):

                # when we exit while loop, lo >= hi
                # print('i=%s j=%s' % (i, j))
                if (m + n) % 2 == 1:
                    ans = max(A[i - 1] if 0 <= i - 1 < m else -math.inf, B[j - 1] if 0 <= j - 1 < n else -math.inf)
                else:
                    ans = (max(A[i - 1] if 0 <= i - 1 < m else -math.inf,
                               B[j - 1] if 0 <= j - 1 < n else -math.inf) + min(A[i] if 0 <= i < m else math.inf,
                                                                                B[j] if 0 <= j < n else math.inf)) / 2

                return ans


"""
Recursive Binary search

Search for k=(m+n+1)/2 k-th item, which recursively calls to find 2-th item.

https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2499/Share-my-simple-O(log(m%2Bn))-solution-for-your-reference
for example，a=[1 2 3 4 6 9]and, b=[1 1 5 6 9 10 11]，total numbers are 13， you should find the seventh number , int(7/2)=3, a[3]<b[3], so you don't need to consider a[0],a[1],a[2] because they can't be the seventh number. Then find the fourth number in the others numbers which don't include a[0]a[1]a[2]. just like this , decrease half of numbers every time
"""


class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if (m + n) % 2 == 1:
            return self.find_kth(A, B, (m + n) // 2)
        else:
            return (self.find_kth(A, B, (m + n) // 2) + self.find_kth(A, B, (m + n) // 2 - 1)) / 2

    def find_kth(self, a, b, k):
        # find k-th smallest element of array a and b combined
        if not b: return a[k]
        if not a: return b[k]

        ka, kb = len(a) // 2, len(b) // 2

        # if k is bigger than sum of a and b's median indices
        # means the k-th element still exist in some larger part of the combined array
        # we can ignore one of a or b's first half
        if ka + kb < k:
            # if a's median is bigger than b's median, b's first half does not include k, can be ignored
            if a[ka] > b[kb]:
                return self.find_kth(a, b[kb + 1:], k - kb - 1)  # exclude b[:kb+1], also reduce k by kb+1
            else:  # a's first half does not include k, can be ignored
                return self.find_kth(a[ka + 1:], b, k - ka - 1)  # exclude a[:ka+1], also reduce k by ka+1
        # when k is smaller than sum of a and b's median indices
        # means the k-th element still exist in some smaller part of the combined array
        # we can ignore one of a or b's second half
        else:
            # if a's median is bigger than b's, than a's second half can be ignore
            if a[ka] > b[kb]:
                return self.find_kth(a[:ka], b, k)  # exclude a's second half, but don't change k
            else:  # a's median is smaller than b's, then b's second half can be ignored
                return self.find_kth(a, b[:kb], k)  # exclude b's second half, but don't change k


def main():
    sol = Solution()
    assert sol.findMedianSortedArrays(A = [1,3], B = [2]) == 2, 'fails'

    assert sol.findMedianSortedArrays(A = [1,2], B = [3,4]) == 2.5, 'fails'

    assert sol.findMedianSortedArrays(A = [0,0], B = [0,0]) == 0.0, 'fails'

    assert sol.findMedianSortedArrays(A = [], B = [1]) == 1.0, 'fails'

    assert sol.findMedianSortedArrays(A = [2], B = []) == 2.0, 'fails'

if __name__ == '__main__':
   main()