"""
351. Android Unlock Patterns
Medium

474

834

Add to List

Share
Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

All the dots in the sequence are distinct.
If the line segment connecting two consecutive dots in the sequence passes through any other dot, the other dot must have previously appeared in the sequence. No jumps through non-selected dots are allowed.
Here are some example valid and invalid unlock patterns:



The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.
The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.
The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.
The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.
Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.



Example 1:

Input: m = 1, n = 1
Output: 9
Example 2:

Input: m = 1, n = 2
Output: 65


Constraints:

1 <= m, n <= 9

"""

"""
Backtrack

at each node, path ending current is also pattern

if a move goes through another node partially, not through center, it is not required for that node to be visited already

or we can consider obstacles only, we have the following obstacles for the path pairs:
first row and third row has second row element as obstacles
first column and third column has second column element as obstacles
diagonal lines (1, 9) and (3, 7) has 5 as obstacles

being symetric, we only need to calculate pattern start at 1, 2, and 5, the ans is
4*(# of pattern start at 1) + 4*(# of pattern start at 2) + (# of pattern start at 5)

"""


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        def check(i, j, used):
            # is this valid move
            # first column and third column on same row
            if (i - 1) // 3 == (j - 1) // 3 and (i - 1) % 3 + (j - 1) % 3 == 2 and i != j and (i + j) % 2 == 0 and (
                    i + j) // 2 not in used:
                return False
            # first row and third row on same column
            if (i - 1) // 3 + (j - 1) // 3 == 2 and (i - 1) % 3 == (j - 1) % 3 and i != j and (i + j) % 2 == 0 and (
                    i + j) // 2 not in used:
                return False
            # corners diagonal across with mid (5) as obstacle
            if ((i == 1 and j == 9) or (i == 9 and j == 1) or (i == 3 and j == 7) or (i == 7 and j == 3)) and (
                    i + j) % 2 == 0 and (i + j) // 2 not in used:
                return False

            # otherwise, no obstacles
            return True

        def bt(cur, l, path):
            # start from node cur, with partial path, how many different patterns can we have for length l
            # print('cur=%s path=%s' % (cur, path))
            if len(path) == l:
                return 1
            pathset = set(path)
            ans = 0
            for i in range(1, 10):
                if i in pathset:
                    continue
                j = path[-1]
                if check(i, j, pathset):
                    ans += bt(i, l, path + [i])

            return ans

        ans = 0
        for l in range(m, n + 1):
            ans += 4 * bt(1, l, [1])
            ans += 4 * bt(2, l, [2])
            ans += bt(5, l, [5])

        return ans

"""
Backtrack

at each node, path ending current is also pattern

if a move goes through another node partially, not through center, it is not required for that node to be visited already

or we can consider obstacles only, we have the following obstacles for the path pairs:
first row and third row has second row element as obstacles
first column and third column has second column element as obstacles
diagonal lines (1, 9) and (3, 7) has 5 as obstacles

"""


class Solution1:
    def numberOfPatterns(self, m: int, n: int) -> int:

        def check(i, j, used):
            # is this valid move
            # first column and third column on same row
            if (i - 1) // 3 == (j - 1) // 3 and (i - 1) % 3 + (j - 1) % 3 == 2 and i != j and (i + j) % 2 == 0 and (
                    i + j) // 2 not in used:
                return False
            # first row and third row on same column
            if (i - 1) // 3 + (j - 1) // 3 == 2 and (i - 1) % 3 == (j - 1) % 3 and i != j and (i + j) % 2 == 0 and (
                    i + j) // 2 not in used:
                return False
            # corners diagonal across with mid (5) as obstacle
            if ((i == 1 and j == 9) or (i == 9 and j == 1) or (i == 3 and j == 7) or (i == 7 and j == 3)) and (
                    i + j) % 2 == 0 and (i + j) // 2 not in used:
                return False

            # otherwise, no obstacles
            return True

        ans = 0

        def bt(cur, path):
            nonlocal ans
            # print('cur=%s path=%s' % (cur, path))
            if m <= len(path) <= n:
                # print('path=%s' % '-'.join(list([str(p) for p in path])))
                ans += 1
            if len(path) == n:
                return
            for i in range(1, 10):
                if i in path:
                    continue
                j = path[-1]
                if check(i, j, set(path)):
                    bt(i, path + [i])

        for i in range(1, 10):
            bt(i, [i])

        return ans


def main():
    sol = Solution()
    assert sol.numberOfPatterns(1, 2) == 65, 'fails'

if __name__ == '__main__':
   main()