"""
1175. Prime Arrangements
Easy

298

408

Add to List

Share
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015


Constraints:

1 <= n <= 100

"""
"""
Math

find number of prime numbers, calculate number of permutations of these prime numbers, and multiple by number of permutations of non-prime numbers
"""
import math

"""
test if number is prime:
1. base case, 0, 1 false, 2, 3, 5, 7 true
2. verify if can be divided by 2 and 3
3. verify if can be divided by 6n-1 and 6n+1 (5, 7, 11, 13, etc)
4. if all above false, then it is prime

"""


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        # print(f"{n = } {i = }")
        return True


def check_prime(x):
    if x >= 2:
        for n in range(2, math.ceil(x / 2)):
            if (x % n) == 0:
                return False
        # after the complete for n loop
        return True
    else:
        return False


class Solution0:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        m = 1  # number of primes, first prime is 2.
        for i in range(3, n + 1, 2):  # only odd number could be a prime, if i > 2.
            factor = 3
            while factor * factor <= i:
                if i % factor == 0:
                    break
                factor += 2
            else:
                m += 1

        print(f"{m = }")

        return ((math.factorial(m) % MOD) * (math.factorial(n - m) % MOD)) % MOD


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        m = 1  # 2 is prime
        for i in range(3, n + 1, 2):  # only odd number could be a prime, if i > 2.
            if is_prime(i):
                m += 1

        print(f"{m = }")

        return ((math.factorial(m) % MOD) * (math.factorial(n - m) % MOD)) % MOD

def main():
    sol = Solution()
    assert sol.numPrimeArrangements(5) == 12, 'fails'

    assert sol.numPrimeArrangements(100) == 682289015, 'fails'

if __name__ == '__main__':
   main()