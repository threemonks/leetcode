"""
1044. Longest Duplicate Substring
Hard

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".


Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""


Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.

"""
"""
Binary Search + Rolling Hash / Rabin-Karp

Note: given input string length 2<=s.length<=3*10^4, we need to use mod 2**63-1, as 10**9+7 is not big enough
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]
        base = 26
        MOD = 2 ** 63 - 1

        def search(k):
            nonlocal nums, base, n, s
            h = 0
            for i in range(k):
                h = (h * base + nums[i]) % MOD
            visited = set()
            visited.add(h)
            al = (base ** k) % MOD
            for start in range(1, n - k + 1):
                h = (h * base - nums[start - 1] * al + nums[start + k - 1]) % MOD
                if h in visited:
                    return start
                visited.add(h)
            return -1

        left, right = 1, n  # [) left close, right open
        res = 0
        while left < right:
            mi = left + (right - left) // 2
            start = search(mi)
            if start != -1:
                left = mi + 1
                res = start
            else:
                right = mi

        return s[res:res + left - 1]


def main():
    sol = Solution()
    assert sol.longestDupSubstring("banana") == "ana", 'fails'

    assert sol.longestDupSubstring("abcd") == "", 'fails'


if __name__ == '__main__':
   main()