"""
943. Find the Shortest Superstring
Hard

435

73

Add to List

Share
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.


Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"


Note:

1 <= A.length <= 12
1 <= A[i].length <= 20

"""
import math
from functools import lru_cache
from typing import List

"""
observation

this is basically a travel salesman problem, strings array is list of cities, overlaps between any two string A[i] and A[j], is the distance of travel from city i to j

use integer (bitmask) to represent a state, where some set of A[i]s have been selected, but we also need to keep in the state which string is used last within that set, as the last string in that set will decide the cost with the next string to pick (i.e., travel distance), so we define state as

dp[bitset][last] := minimum distance after select strings with indexes represented as bit in mask, with i-th string be last in this set, then we can develop dp[new_bitset][j] = max(dp[bitset][i] + distance(A[i], A[j])
where new_bitset = bitset | (1<<j) # adding j-th bit into bitset, with condition that j-th bit was not set in bitset before this update

distance(A[i], A[j]) = when connect A[i] and A[j] with A[j] overlaps with A[i] as much as possible, the length increases caused by appending A[j]

to reconstruct the substring, we need to reconstruct the optimal path, in order to reconstruct the optimal path, for each dp[bitset][last], we need to represents what its last_prev is

        
basic logic:

A = ["alex","loves","leetcode"]
        
bitset = 0b111 # represents a state where all three words have been selected

dp[1<<len(A)][len(A)]
dp[bitset][last] := shortest path we traveled the cities in biset, and the last stop is "last"

for bitset from 0b000 to 0b111: # this needs to loop from 0b000 to 0b111 in order, to ensure below update logic works
    for last in all possible lasts in bitset:
        bitset_prev = bitset - last
        for last_prev in (all last of bitset_prev):
            dp[bitset][last] = min(dp[bitset_prev][last_prev]+distance(last_prev, last))
            # also record parent of dp[bitset][last], so that we can reconstruct the path
            parent[bitset][last] = last_prev

time O(n^2 * 2^n)
space O(n^2)

brutal force DFS would be time O(n!)

"""
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A) # number of words
        N = (1<<n) # number of states
        # print('n=%s N=%s' % (n, N))

        dp = [[math.inf for _ in range(n)] for _ in range(N)]
        parent = [[-1 for _ in range(n)] for _ in range(N)]
        # initialize
        dp[0][0] = 0

        # initialize one word set, the distance would be the word size (set with one city only)
        for i in range(n):
            dp[(1<<i)][i] = len(A[i])

        @lru_cache(None)
        def distance(i, j):
            """
            distance from A[i] to A[j], i..e, attaching A[j] to A[i], the length increasement
            """
            nonlocal A
            for l in range(len(A[j]), -1, -1):
                if A[i].endswith(A[j][:l]):
                    return len(A[j])-l
            return len(A[j])

        for bitset in range(N):
            # print('\nbitset=%s ' % bitset, end='')
            for last in range(n):
                # print(' last=%s ' % last, end='')
                bitset_prev = bitset - (1<<last)
                if bitset_prev == 0: # cannot work on this?
                    continue
                for last_prev in range(n):
                    # if last_prev not in bitset_prev, skip
                    if (bitset_prev & (1<<last_prev)) == 0:
                        continue
                    if dp[bitset][last] > dp[bitset_prev][last_prev]+distance(last_prev, last):
                        dp[bitset][last] = dp[bitset_prev][last_prev]+distance(last_prev, last)
                        parent[bitset][last] = last_prev
                        # print(' dp[%s][%s]=%s ' % (bitset, last, dp[bitset][last]), end='')

        # now find the smallest dp[N-1][*]
        ret = math.inf
        last = None # this is the end city of travel, or last word we use in the superstring
        for i in range(n):
            if dp[N-1][i] < ret:
                ret = dp[N-1][i]
                last = i

        # now reconstruct the path and output
        bitset = N-1
        path = [last]
        while parent[bitset][last] != -1:
            last_prev = parent[bitset][last]
            path.append(last_prev)
            bitset = bitset - (1<<last)
            last = last_prev

        path = path[::-1]

        def combine(a, b):
            """
            combine string a and b, with b overlapping a as much as possible
            """
            for l in range(len(b), -1, -1):
                if a.endswith(b[:l]):
                    return a + b[l:]
            return a+b


        ans = A[path[0]]
        for i in range(1,len(path)):
            ans = combine(ans, A[path[i]])

        return ans


def main():
    sol = Solution()
    assert (sol.shortestSuperstring(["alex","loves","leetcode"]) == "alexlovesleetcode" or sol.shortestSuperstring(["alex","loves","leetcode"]) == "leetcodelovesalex"), 'fails'

    assert sol.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"]) == "gctaagttcatgcatc", 'fails'

if __name__ == '__main__':
   main()