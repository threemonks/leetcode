"""
12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.



Example 1:

Input: num = 3
Output: "III"
Example 2:

Input: num = 4
Output: "IV"
Example 3:

Input: num = 9
Output: "IX"
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= num <= 3999

"""
"""
greedy
"""


class Solution0:
    def intToRoman(self, num: int) -> str:
        chardict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        base = [1, 5, 10, 50, 100, 500, 1000]
        base_index = len(base) - 1

        res = ''
        n = num
        while n and base_index >= 0:
            quotient, remainder = n // base[base_index], n % base[base_index]
            # print('n=%s base_index=%s base[base_index]=%s quotient=%s remainder=%s' % (n, base_index, base[base_index], quotient, remainder))
            if base[base_index] in [1, 10, 100, 1000] and 0 < quotient <= 3:
                res += chardict[base[base_index]] * quotient
                n = remainder
            elif base[base_index] in [1, 10, 100] and quotient == 4:
                res += chardict[base[base_index]] + chardict[base[base_index + 1]]
                n = remainder
            elif base[base_index] in [1, 10, 100] and quotient == 9:
                res += chardict[base[base_index]] + chardict[base[base_index + 2]]
                n = remainder
            elif base[base_index] in [1, 10, 100] and 5 <= quotient < 9:
                # use next base 5
                quotient5, remainder5 = n // base[base_index + 1], n % base[base_index + 1]
                res += chardict[base[base_index + 1]]
                n = remainder5
                base_index += 1  # we need to try this same base_index again (to cancel the base_index-=1 at end of loop)
            base_index -= 1
            # print('res=%s' % res)

        return res


"""
greedy, but handles 4s and 9s similar as 1s and 5s
observation
4s and 9s has its own representation, we can build that into the map
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        charmap = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        res = ''
        while num:
            for nc in charmap:
                if num >= nc[0]:
                    res += nc[1] * (num // nc[0])
                    num = num % nc[0]

        return res


def main():
    sol = Solution()
    assert sol.intToRoman(3) == "III", 'fails'

    assert sol.romanToInt(4) == "IV", 'fails'

    assert sol.romanToInt(9) == "IX", 'fails'

    assert sol.romanToInt(58) == "LVIII", 'fails'

    assert sol.romanToInt(1994) == "MCMXCIV", 'fails'


if __name__ == '__main__':
   main()