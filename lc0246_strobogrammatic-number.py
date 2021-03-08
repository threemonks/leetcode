"""
246. Strobogrammatic Number
Easy

278

545

Add to List

Share
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true


Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
"""
"""
Hash Table
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        digits = {'6': '9', '8': '8', '1': '1', '0': '0', '9': '6'}
        n = len(num)
        return all([num[i] == digits.get(num[n-1-i], -1) for i in range(n)])

def main():
    sol = Solution()
    assert sol.isStrobogrammatic("69") is True, 'fails'

    assert sol.isStrobogrammatic("962") is False, 'fails'


if __name__ == '__main__':
   main()