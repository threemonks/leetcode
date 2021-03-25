"""
870. Advantage Shuffle
Medium

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9

"""
import collections
from typing import List

"""
Greedy

Intuition

Since we want to get as many element in A in place larger than its corresonding item in B as possible, we should try to use as small A[i] as possible at i, as long as A[i] > B[i], i.e., greedily use smallest possible value A[i]>B[i]

So we sort A and B, for each smallest B[j], find smallest A[i] that's larger than B[j], put into assigned dict, any smaller number in A that's not used for a corresponding B[j] could be ignored (put into remaining list, as they cannot add to score)

And the result would be [A[assigned[b]] or remaining.pop() for b in originalB]

mistakes:
1. smallest a=A[i] that's larger than given b, could have duplicates
"""


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sorted_B = sorted(B)
        sorted_A = sorted(A)

        assigned = collections.defaultdict(list)
        # holds b with its corresponding pair item in A that has advantage (smallest such a), might have duplicate
        remaining = []  # elements in A that cannot be paired with any element in B

        j = 0  # index of B tracking which b has been paired
        for a in sorted_A:
            if a > sorted_B[j]:
                assigned[sorted_B[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # reconstruct answer from assigned and remaining
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]


def main():
    sol = Solution()
    assert sol.advantageCount(A = [2,7,11,15], B = [1,10,4,11]) == [2,11,7,15], 'fails'

    assert sol.advantageCount(A = [12,24,8,32], B = [13,25,32,11]) == [24,32,8,12], 'fails'



if __name__ == '__main__':
   main()