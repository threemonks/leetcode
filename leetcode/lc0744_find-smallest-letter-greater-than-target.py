"""
744. Find Smallest Letter Greater Than Target
Easy

774

867

Add to List

Share
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""
from typing import List

"""
One pass

use ans to keep track of smallest letter > target
use globalmin to keep track of global min, in case there's no letter > target, then we need to wrap around.

note:
1. letters are sorted non-descending

"""


class Solution0:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        globalmin = letters[0]
        ans = None
        for c in letters:
            if c > target:
                return c

                ans = min(ans, c) if ans else c
            globalmin = min(globalmin, c)

        return ans if ans else globalmin


"""
Binary Search
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        lo, hi = 0, n
        while lo < hi:
            mi = (hi + lo) // 2
            if target < letters[mi]:
                hi = mi
            else:
                lo = mi + 1

        return letters[lo % len(letters)]

def main():
    sol = Solution()
    assert sol.nextGreatestLetter(letters = ["c","f","j"], target = "a") == 'c', 'fails'

    assert sol.nextGreatestLetter(letters = ["c","f","j"], target = "c") == 'f', 'fails'

    assert sol.nextGreatestLetter(letters = ["c","f","j"], target = "d") == 'f', 'fails'

    assert sol.nextGreatestLetter(letters = ["c","f","j"], target = "g") == 'j', 'fails'

    assert sol.nextGreatestLetter(letters = ["c","f","j"], target = "j") == 'c', 'fails'

if __name__ == '__main__':
   main()