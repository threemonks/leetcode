"""
1707. Maximum XOR With an Element From Array
Hard

https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
"""
from typing import List

"""
Bitwise Trie

Following hints, for each query, we filter nums to valid numbers and build trie just for that query, but this TLE.

use one new Trie for each query will result in TLE

sort query and nums first, and use same trie, this way the trie only has values for small numbers when the query was for a smaller range, and as the query asks for larger number, we grow trie (by adding larger nums that meets the new requirement of queries)

time O(sort) - sort nums and queries O(N*log(N) + M*log(M))
space O(N)

mistakes:
1. to test if p has value, use p.value is not None, not p.value
2. to get max XOR, when x & (1 << i) == 1, we pick t.zero first (optimal to maximize XOR result), but if t.zero is None, we also try t.one (less optimal)
3. At each step when we attempt to get 1 for i-th bit, we also need to test if t is None (as we might have no such branch because no value along that branch)
4. After we finish iterating all bits (2^31), we need to update result nx_xor again, because the result could be updated by numbers from last iteration (i=0)
5. try to build a new trie at each step will timeout, instead, we sort both nums and queries from smaller to large, so for each query in queries, we only add those newly (not added yet) valid nums into trie, this guarantees queries always get right result, yet keeps trie size at minimal
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        p = self.root
        for i in range(32)[::-1]:
            curr = (num >> i) & 1  # extract i-th bit of num
            if curr not in p:
                p[curr] = {}
            p = p[curr]

    def query(self, num):
        # query to find value that returns max XOR value with num
        if not self.root:
            return -1
        ans, p = 0, self.root
        for i in range(32)[::-1]:
            curr = (num >> i) & 1  # extract i-th bit of num
            if 1 - curr in p:  # if XOR of curr exists, update answer
                ans |= (1 << i)
                p = p[1 - curr]
            else:  # else, proceed with curr (less optimal)
                p = p[curr]

        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # sort nums so that we insert smaller ones first as necessary
        nums = sorted(nums)
        # sort queries so that when we query smaller number, the trie only contains values for those range
        # as we query for larger numbers, we add larger values from nums  into trie,
        # (that were not within query range earlier, but are within range now)
        # we also need to keep the original index, so that we can order result accordingly
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        print(queries)
        trie = Trie()
        j = 0
        result = [-1] * len(queries)
        for i, (x, m) in queries:
            while j < len(nums) and nums[
                j] <= m:  # only add element from nums <= m, and not added to trie yet (in prevoius query)
                trie.insert(nums[j])
                j += 1

            y = trie.query(x)

            result[i] = y

        return result


def main():
    sol = Solution()
    assert sol.maximizeXor(nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]) == [3,3,7], 'fails'

    assert sol.maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]) == [15,-1,5], 'fails'



if __name__ == '__main__':
   main()