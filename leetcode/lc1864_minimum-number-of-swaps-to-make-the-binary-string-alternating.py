"""

Medium

166

20

Add to List

Share
Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.



Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1


Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
"""
"""
Greedy

let ones be number of '1' in s, zeros be number of '0' in s, the converted string would be same length as original string, but started with either '1' or '0', and alternating.

The problem has three possible cases:
1. ones - zeros > 1 or zeros - ones > 1:
   not possible
2. ones - zeros = 1 or zeros - ones = 1:
   if ones > zeros, the minimum swap result alternating string would start with '1'
   else zeros > ones, the minimum swap result alternating string would start with '0'
   we count mismatched positions between original string and converted alternating string, it would take mismatches/2 swaps to make it alternating.
3. ones == zeros
    the minimum swap result alternating string could either start with '0' or '1', we try both alternating string, compare with original string, count number of mismatches, take the minimum of the two, the required swaps would be half the min mismatches.

"""


class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        ones = s.count('1')
        zeros = s.count('0')

        def helper(s, c):
            # minswaps for s to be converted into alternating binary string starting with c
            counts = 0
            for ch in s:
                if ch != c:
                    counts += 1
                c = '1' if c == '0' else '0'

            return counts // 2

        # if count differ >= 2, cannot become alternate
        if ones > zeros + 1 or zeros > ones + 1:
            return -1

        # if ones > zeros => the best answer would be 1xxx
        if ones > zeros:
            return helper(s, '1')
        elif zeros > ones:
            return helper(s, '0')
        else:  # ones == zeros
            return min(helper(s, '1'), helper(s, '0'))

def main():
    sol = Solution()

    assert sol.minSwaps(s = "111000") == 1, 'fails'

    assert sol.minSwaps(s = "010") == 0, 'fails'

    assert sol.minSwaps(s = "1110") == -1, 'fails'


if __name__ == '__main__':
   main()