"""
859. Buddy Strings
Easy

1635

1056

Add to List

Share
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.


Constraints:

1 <= s.length, goal.length <= 2 * 10^4
s and goal consist of lowercase letters.
"""
"""
compare char by char, record differences, see if there are two being different, if these can swap to make the first same as second

it is really two cases:
1. s == goal, and s[i] == s[j] for i != j, i.e., there exists at least one duplicate chars
2. s != goal, but s[i] == goal[j] and s[j] == goal[i]

"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # s == goal
        if s == goal and len(set(s)) < len(s):  # there are duplicate characters
            return True

        # s != goal
        n = len(s)

        diffs = list()

        for i in range(n):
            if s[i] != goal[i]:
                diffs.append(i)

        if len(diffs) != 2:
            return False

        i, j = diffs
        if s[i] == goal[j] and s[j] == goal[i]:
            return True
        else:
            return False

def main():
    sol = Solution()
    assert sol.buddyStrings(s = "ab", goal = "ba") is True, 'fails'

    assert sol.buddyStrings(s = "ab", goal = "ab") is False, 'fails'

    assert sol.buddyStrings(s = "aa", goal = "aa") is True, 'fails'

if __name__ == '__main__':
   main()