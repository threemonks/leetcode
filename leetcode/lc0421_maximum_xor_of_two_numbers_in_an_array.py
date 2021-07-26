"""
421. Maximum XOR of Two Numbers in an Array
Medium

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
"""
from typing import List

"""
brutal force

TLE
"""


class Solution0:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        n = len(nums)
        res = -math.inf
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, nums[i] ^ nums[j])

        return res


"""
Bitwise Trie (binary number)

Bitwise Trie has two children, zero, and one.

Store most significant bit at root, and less significant bit towards leaf, all numbers are stored at leaf node

time O(N)
space O(2^N)
"""
from collections import defaultdict


# Trie represents binary numbers, so each node has only two children, zero, and one
# and each leaf node will hold a value if it represents a number

class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        p = self.root
        for b in range(31, -1, -1):  # store most significant bit at root, less significant bit towards leaf
            if (1 << b) & number:
                if not p.one:
                    p.one = TrieNode()
                p = p.one
            else:
                if not p.zero:
                    p.zero = TrieNode()
                p = p.zero

        p.value = number  # store value at leaf node for easier access


class Solution1:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()

        for num in nums:
            trie.insert(num)

        max_xor = 0

        # now try to find max XOR counterparty number for each element of nums[i]
        # we start from root, try to find as many bits that can XOR with num's corresponding bit and get 1 as possible
        # keep repeating this until we are at leaf node
        # and record the XOR result, and update global max XOR result if possible
        for num in nums:
            p = trie.root
            for b in range(31, -1, -1):  # most significant bit from root
                if (1 << b) & num:  # num has this bit as 1
                    if p.zero:  # search for child 0 as we want maximum XOR value between num and the number stored along this path
                        p = p.zero
                    else:
                        p = p.one  # next optimal, will give smaller XOR result with num, but we still need to traverse down to leaf node as deeper level might still contribute 1s to the result (though less significant)
                else:
                    if p.one:
                        p = p.one
                    else:
                        p = p.zero  # next optimal, will give smaller XOR result with num, but we still need to traverse down to end
                # at each step, we also try to update max xor in case this is the last (max) xor counterparty we can find for num
                if p and p.value is not None:
                    max_xor = max(max_xor, num ^ p.value)
            # at end of trie/leaf node, if there's a number, it is the max XOR counterparty for num we find
            if p and p.value is not None:
                max_xor = max(max_xor, num ^ p.value)

        # when we are done searching all num's XOR counterparty, we find the max_xor among all in nums
        return max_xor


"""
Greedy / Bit manipulation

idea is to convert all numbers to binary, and construct maximum XOR result bit by bit, starting from left most one (most significant one)

steps:
1. The max possible results is 2^31, i.e., we try to build answer from 31st bit, down to 0th bit
2. for each of the bit we are building, we shift answer left by 1 bit, so it's smallest bit is 0
3. Create set of all possible starts of numbers (prefixes), using num>>i. On the first iterations it will be first digit, on the next one first two digits and so on
4. then we try to find if any num would find its complement (XOR result in 1 in smallest (i-th) bit) in prefixes, if found, that means we can update answer i-th bit to 1, if not leave this bit as 0
5. repeat step 2 to 4 until we are done

time O(N)
"""


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1  # shift ans left by 1 bit, so we can work on if we can set next bit (left most)
            prefixes = set([x >> i for x in nums])  # all prefixes of length (L-i) that has i-th bit as 1
            candidate = ans | 1  # potential candidate would be ans with smallest bit set to 1
            # if candidate^p exists in prefixes, that means there are two items in prefixes that can XOR
            # and result in 1 for this bit, thus can contribute to ans's i-th (smallest) bit
            if any(bool(candidate ^ p in prefixes) for p in prefixes):
                ans |= candidate  # update smallest bit of ans from candidate if valid candidate found
            # if no pairs in prefixes can set i-th bit for ans, then it remains 0

        return ans


def main():
    sol = Solution()
    assert sol.findMaximumXOR([3,10,5,25,2,8]) == 28, 'fails'

    assert sol.findMaximumXOR([0]) == 0, 'fails'

    assert sol.findMaximumXOR([2,4]) == 6, 'fails'

    assert sol.findMaximumXOR([8,10,2]) == 10, 'fails'

    assert sol.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]) == 127, 'fails'

if __name__ == '__main__':
   main()