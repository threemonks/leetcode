"""
402. Remove K Digits
Medium

2839

124

Add to List

Share
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
"""
use stack to store ealier (from left) smallest digits, and pop at most k digits, and pop early and larger ones

time O(n)
space O(n)
"""


class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        n = len(nums)
        if n <= k:
            return "0"

        stack = []
        pop_count = 0

        for i, num in enumerate(nums):
            while stack and num < stack[-1] and pop_count < k:
                stack.pop()
                pop_count += 1
            stack.append(num)
            # print(stack)
        # if there's more digits left in stack than needed
        while stack and pop_count < k:
            stack.pop()
            pop_count += 1

        # print(stack)
        res = ''.join(stack).lstrip('0')
        return res if res else "0"


def main():
    sol = Solution()
    assert sol.removeKdigits("1432219", 3) == "1219", 'fails'

    assert sol.removeKdigits("10200", 1) == "200", 'fails'

    assert sol.removeKdigits("10", 2) == "0", 'fails'

    assert sol.removeKdigits("112", 1) == "11", 'fails'

if __name__ == '__main__':
   main()