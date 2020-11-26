"""
1446. Consecutive Characters
Easy

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1


Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.

"""
from typing import List


class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        max_power = 1
        l = len(s)
        curr_power = 1
        for i in range(1, l):
            if s[i] == s[i - 1]:
                curr_power += 1
                max_power = max(max_power, curr_power)
            else:
                curr_power = 1
                max_power = max(max_power, curr_power)

        return max_power
def main():
    sol = Solution()
    assert sol.maxPower("leetcode") == 2, 'fails'

    assert sol.maxPower("abbcccddddeeeeedcba") == 5, 'fails'

    assert sol.maxPower("triplepillooooow") == 5, 'fails'

    assert sol.maxPower("hooraaaaaaaaaaay") == 11, 'fails'

    assert sol.maxPower("tourist") == 1, 'fails'



if __name__ == '__main__':
   main()