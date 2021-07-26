"""
454. 4Sum II
Medium

https://leetcode.com/problems/4sum-ii/
"""
from typing import List

"""
brutal force + 2-sum

create all combinations for a+b+c, binary search it in hashmap of D (with counts)

TLE

time O(N^3)
"""
import collections


class Solution0:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A or not B or not C or not D:
            return 0

        dcounter = collections.Counter(D)

        abset = set()  # record z+b sum that finds no c+d totals to zero
        count = 0
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                sumab = a + b
                if sumab in abset:
                    continue
                count_ab = count
                for k, c in enumerate(C):
                    target = 0 - (a + b + c)
                    if target in dcounter:
                        count += dcounter[target]
                if count_ab == count:  # this sumab finds no match sum in cd
                    abset.add(sumab)

        return count


"""

create hashmap with counts for a+b, and also c+d, see if we can find matches that sum to zero between the two hashmaps

time O(N^2)
"""
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A or not B or not C or not D:
            return 0

        counts_ab = collections.defaultdict(int)
        counts_cd = collections.defaultdict(int)

        for a in A:
            for b in B:
                counts_ab[a + b] += 1

        count = 0

        for c in C:
            for d in D:
                count += counts_ab[-(c + d)]

        return count


def main():
    sol = Solution()
    assert sol.fourSumCount(A = [ 1, 2], B = [-2,-1], C = [-1, 2], D = [ 0, 2]) == 2, 'fails'

if __name__ == '__main__':
   main()