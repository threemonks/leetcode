"""
556. Next Greater Element III
Medium

2851

388

Add to List

Share
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.



Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1


Constraints:

1 <= n <= 2^31 - 1

"""
"""
Brutal force Permutation

Note:
1. answer must fit within 32 bit integer, if not, return -1

time O(n!) - timeout
space O(n!)
"""


def permutations(nums):
    results = [[]]
    for num in nums:
        newres = []
        for r in results:
            for i in range(len(r) + 1):
                # print(f"{results = } {newres = } {i = } {r = } {num = }")
                newres.append(r[:i] + [num] + r[i:])
                # print(f"after updating newres {results = } {newres = } {i = } {r = } {num = }")
        results = newres

    return results


# from itertools import permutations
class Solution0:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        if int(''.join(sorted(s))) >= (1 << 31):
            return -1
        ans = math.inf

        for perm in permutations(list(s)):
            newint_s = ''.join(perm)
            # print(f"{perm = } {newint_s = }")
            if newint_s and not newint_s.startswith('0'):
                newint = int(newint_s)
                if newint > n:
                    ans = min(ans, newint)

        return ans if ans < (1 << 31) else -1


"""
Math

similar to leetcode 31, next permutation
1. start from right, look for longest increasing pattern
2. if the entire string is increasing, there's no answer
3. find the longest increasing pattern ending at i, i.e., nums[i-1]<nums[i], but for all j>i, nums[j-1]>nums[j],
  then we need to find the smallest digits in nums[i:] that is larger than nums[i-1], let's say that is index k
  then we swap nums[i-1] with nums[k]
  then we need to make all digits in nums[i:] increasing (since it was all the way decreasing to right, even after the digit swap), we can just reverse it

"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        if int(''.join(sorted(digits))) >= (1 << 31):
            return -1

        l = len(digits)
        p = -1
        for i in range(l - 1, -1, -1):
            if i - 1 >= 0 and digits[i - 1] < digits[i]:
                p = i - 1
                break

        if p == -1:  # we didn't find any non-decreasing pattern
            return -1

        k = -1
        for j in range(l - 1, p, -1):
            if digits[j] > digits[p]:
                # swap digits[p] and digits[j]
                digits[p:p + 1], digits[j:j + 1] = digits[j], digits[p]
                break

        # reverse digits[p+1:]
        digits = digits[:p + 1] + digits[p + 1:][::-1]

        ans = int(''.join(digits))
        return ans if ans < (1 << 31) else -1


def main():
    sol = Solution()
    assert sol.nextGreaterElement(n=12) == 21, 'fails'

    assert sol.nextGreaterElement(n=21) == -1, 'fails'

if __name__ == '__main__':
   main()