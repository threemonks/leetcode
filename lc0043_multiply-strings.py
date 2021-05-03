"""
43. Multiply Strings
Medium

2486

991

Add to List

Share
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
"""
String

consider each char of string of integer as node in linked list, multiply corresponding digit and add to corresponding digit in result
     1 2 3
x    3 2 1
----------
     1 2 3
   2 4 6
 3 6 9
so i-th (from right) digit of num1 and j-th (from right) digit of num2 goes to i+j-1-th (from right) digit of answer

mistakes:
1. k-th digits contribution comes from i+j=k-1 for any 0<=i<m and 0=j<n
2. we need get all k-th digits contributions summed together before applying carry from previous digits
3. deal with zeros because we might have answer of length m+n or m+n-1.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        m, n = len(num1), len(num2)

        i, j = 0, 0
        ans = [0] * (m+n)
        carry = [0] * (m+n)
        for k in range(m+n):
            for i in range(k+1):
                j = k-i
                v1 = ord(num1[i]) - ord('0') if i < m else 0
                v2 = ord(num2[j]) - ord('0') if j < n else 0
                val = v1 * v2
                ans[k] += val
            # calculate carry for next digit when all prod to this digit are done
            if k+1 < m+n:
                carry[k+1] = (ans[k]+carry[k]) // 10
            ans[k] = (ans[k]+carry[k]) % 10

        # drop all zeros from right exept for last one
        while len(ans) > 1 and ans[-1] == 0:
            ans = ans[:-1]

        # reverser ans and convert back to string
        return ''.join([str(a) for a in ans[::-1]])

def main():
    sol = Solution()
    assert sol.multiply(num1 = "2", num2 = "3") == '6', 'fails'

    assert sol.multiply(num1 = "123", num2 = "456") == "56088", 'fails'

if __name__ == '__main__':
   main()