"""
319. Bulb Switcher
Medium

694

1323

Add to List

Share
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.



Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1


Constraints:

0 <= n <= 10^9

"""
import math

"""
Math

   b1 b2 b3 b4 b5 b6
r1 +  +  +  +   + +
r2 +  -  +  -   + -
r3 +  -  -  -   + + 
r4 +  -  -  +   + +
r5 +  -  -  +   - +
r6 +  -  -  +   - -

for 6, we have 1 and 4, 1 has one factor 1, 4 has only one factor 2 other than 1 and 4,
6 has factor 2 and 3 other than 1 and 4, so

factor_count (1) = 1
 2 => 2
 4 => 3
 6 => 4

 divisors come in pairs, except for perfect squares
 so only numbers that are perfect squares will have odd number of toggles, thus remains on
 so we only need to count # of perfect squares <= n

"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))

def main():
    sol = Solution()
    assert sol.bulbSwitch(1) == 1, 'fails'

    assert sol.bulbSwitch(4) == 2, 'fails'

if __name__ == '__main__':
   main()