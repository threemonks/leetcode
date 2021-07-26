"""
202. Happy Number
Easy

3217

524

Add to List

Share
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 2^31 - 1

"""
"""
Hash Table

Use hash table to store numbers encountered, to detect cycle

time O(log(N)) <= number of digits ~ log(N)
space log(N)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        def get_next(x):
            # get next n by summing squares of each digit of n
            sums = 0
            while x >= 1:
                sums += (x % 10) * (x % 10)
                x //= 10
            return sums

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


def main():
    sol = Solution()
    assert sol.isHappy(n = 19) is True, 'fails'

    assert sol.isHappy(n = 2) is False, 'fails'


if __name__ == '__main__':
   main()