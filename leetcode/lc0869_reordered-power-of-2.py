"""
869. Reordered Power of 2
Medium

421

147

Add to List

Share
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.



Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
Example 3:

Input: n = 16
Output: true
Example 4:

Input: n = 24
Output: false
Example 5:

Input: n = 46
Output: true


Constraints:

1 <= n <= 109

"""
import collections

"""
get all permutations of digits, check if it is power of two (bin(n) has only one 1 bit)

mistakes:
1. reorder number has no leading zero
"""


class Solution0:
    def reorderedPowerOf2(self, N: int) -> bool:
        s = str(N)

        l = len(s)

        perm = [[]]
        for i in range(l):
            newperm = []
            for p in perm:
                for k in range(len(p) + 1):
                    newperm.append(p[:k] + [s[i]] + p[k:])

            perm = newperm[:]

        for p in perm:
            p = ''.join(p)
            if not p.startswith('0') and bin(int(p)).count("1") == 1:
                return True

        return False


"""
Count digits

since maximum number N is 10^9, 10^9 < 2^31, we can just check if N has same digits as any of 2^0, 2^1, 2^..., 2^31.
"""


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = collections.Counter(str(N))

        for i in range(31):
            if count == collections.Counter(str(1 << i)):
                return True

        return False


def main():
    sol = Solution()
    assert sol.reorderedPowerOf2(1) is True, 'fails'

    assert sol.reorderedPowerOf2(10) is False, 'fails'

    assert sol.reorderedPowerOf2(46) is True, 'fails'


if __name__ == '__main__':
   main()