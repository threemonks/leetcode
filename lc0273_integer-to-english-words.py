"""
273. Integer to English Words
Hard

1482

3698

Add to List

Share
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


Constraints:

0 <= num <= 2^31 - 1
"""
import math

"""
Math

observation:
1. split by chunks (every 3 digits), billions, millions, and thousands
2. note hundreds all need special handling
3. all tens and teens need special handling
4. corner case 1000, 1000,000, or 100

1,234,567,891
b   m   th 

"""


class Solution:
    def numberToWords(self, num: int) -> str:
        words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
                 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
                 }

        if num <= 20:
            return words[num]

        tens = list(range(90, -1, -10))

        if num >= 10 ** 9:
            if num % (10 ** 9):
                return self.numberToWords(num // (10 ** 9)) + " Billion " + self.numberToWords(num % (10 ** 9))
            else:
                return self.numberToWords(num // (10 ** 9)) + " Billion"
        elif num >= 10 ** 6:
            if num % (10 ** 6):
                return self.numberToWords(num // (10 ** 6)) + " Million " + self.numberToWords(num % (10 ** 6))
            else:
                return self.numberToWords(num // (10 ** 6)) + " Million"
        elif num >= 10 ** 3:
            if num % (10 ** 3):
                return self.numberToWords(num // (10 ** 3)) + " Thousand " + self.numberToWords(num % (10 ** 3))
            else:
                return self.numberToWords(num // (10 ** 3)) + " Thousand"
        elif num >= 10 ** 2:
            if num % (10 ** 2):
                return self.numberToWords(num // (10 ** 2)) + " Hundred " + self.numberToWords(num % (10 ** 2))
            else:
                return self.numberToWords(num // (10 ** 2)) + " Hundred"
        else:
            for t in tens:
                if num == t:
                    return words[t]
                elif num > t:
                    return words[t] + ' ' + words[num - t]


def main():
    sol = Solution()
    assert sol.numberToWords(num = 123) == "One Hundred Twenty Three", 'fails'

    assert sol.numberToWords(num = 12345) == "Twelve Thousand Three Hundred Forty Five", 'fails'

    assert sol.numberToWords(num = 1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven", 'fails'

    assert sol.numberToWords(num = 1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One", 'fails'

if __name__ == '__main__':
   main()