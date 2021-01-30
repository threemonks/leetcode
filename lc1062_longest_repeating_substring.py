"""
1062. Longest Repeating Substring
Medium

Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.



Example 1:

Input: S = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: S = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: S = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: S = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.


Constraints:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500

"""
"""
Binary Search + Rolling Hash / Rabin-Karp

try to find repeating substring of length k, use binary search method to find k, which should be between 0 and n,
if we can repeating substring of length k, then we tray (k+n)/2

time O(N*log(N)) - log(N) for binary search, O(N) for Rabin-Karp
space O(N)
"""


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        base = 26  # only 26 characters
        MOD = 10 ** 9 + 7

        def helper(k):
            nonlocal nums, base, n
            visited = set()
            h = 0
            for i in range(k):
                h = (h * base + nums[i]) % MOD
            visited.add(h)
            al = (base ** k) % MOD
            for i in range(1, n - k + 1):
                h = (h * base - nums[i - 1] * al + nums[i + k - 1]) % MOD
                if h in visited:
                    return i
                visited.add(h)
            return -1

        left, right = 1, n  # [)
        while left < right:
            mi = left + (right - left) // 2
            if helper(mi) != -1:
                left = mi + 1
            else:
                right = mi

        return left - 1


def main():
    sol = Solution()
    assert sol.longestRepeatingSubstring("abcd") == 0, 'fails'

    assert sol.longestRepeatingSubstring("abbaba") == 2, 'fails'

    assert sol.longestRepeatingSubstring("aabcaabdaab") == 3, 'fails'

    assert sol.longestRepeatingSubstring("aaaaa") == 4, 'fails'

if __name__ == '__main__':
   main()