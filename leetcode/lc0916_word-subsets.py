"""
916. Word Subsets
Medium

We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.


Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].

"""
import collections
from typing import List

"""
Observation:

For a is a superset of every word b in array B, we can just check if a is a superset of a super word b that consists of of all word in B including multiplicity

mistakes:
1. for each of b is a subset of a, we can combine all words in B, find their maximum frequence of each letter, only need to check if this superset word b is in a

time O(A+B)
space O(A.length+B.length)
"""


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bcounts = collections.defaultdict(int)
        for b in B:
            bc = collections.Counter(b)
            for c in bc:
                bcounts[c] = max(bcounts[c], bc[c])

        acounts = {a: collections.Counter(a) for a in A}
        awords = sorted(acounts.keys())

        result = []
        for aw in awords:
            ac = acounts[aw]
            ackeyset = set(ac.keys())
            bckeys = bcounts.keys()
            if any([((bk not in ackeyset) or (bcounts[bk] > ac[bk])) for bk in bckeys]):
                continue
            result.append(aw)

        return result


def main():
    sol = Solution()
    assert sol.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]) == ["facebook","google","leetcode"], 'fails'

    assert sol.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]) == ["apple","google","leetcode"], 'fails'

    assert sol.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]) == ["facebook","google"], 'fails'

    assert sol.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]) == ["google","leetcode"], 'fails'

    assert sol.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]) == ["facebook","leetcode"], 'fails'

if __name__ == '__main__':
   main()