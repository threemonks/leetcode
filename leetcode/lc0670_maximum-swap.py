"""
670. Maximum Swap
Medium

1680

98

Add to List

Share
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.


Constraints:

0 <= num <= 108

"""
"""
Array / Greedy

from left to right, for each digit, find the rightmost largest digit (9, 8, ..., digits[i]) in this num that is also to its right, swap this two digits

2736 => 7236
736 => 763
9973 => 9973
98368 => 98863

notes:
1. 10 needs to be extracted into two digits, so do while num > 9 ... num//=10
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        while num > 9:
            digits.append(num % 10)
            num = num // 10

        digits.append(num)

        digits = digits[::-1]

        # print('digits=%s' % digits)

        def find_swap(digits):
            n = len(digits)
            for i in range(n):
                for d in range(9, digits[i], -1):
                    for j in range(n - 1, i, -1):
                        if digits[j] == d:
                            digits[i], digits[j] = digits[j], digits[i]
                            return

        # print('before swap digits=%s' % digits)
        find_swap(digits)
        # print('after swap digits=%s' % digits)

        # convert digits back to num
        ans = 0
        for d in digits:
            ans = ans * 10 + d

        return ans


def main():
    sol = Solution()
    assert sol.maximumSwap(num = 2736) == 7236, 'fails'

    assert sol.maximumSwap(num=9973) == 9973, 'fails'

    assert sol.maximumSwap(98368) == 98863, 'fails'

    assert sol.maximumSwap(10909091) == 90909011, 'fails'

if __name__ == '__main__':
   main()