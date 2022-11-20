"""838. Push Dominoes
Medium

3037

182

Add to List

Share
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."


Constraints:

n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.'.
"""
"""
Repeatedly applying impact until no impact can be done

Note:
1. only save the updated nodes after we scan the entire list once and applied necessary changes
"""


class Solution0:
    def push(self):
        """
        return number of changes we did in this round
        """
        # print(f"{self.dominoes = }")
        # print(f"{self.runs = }")
        n = len(self.dominoes)
        c = 0
        doms = self.dominoes[:]  # make a local copy so we can update it for all nodes before we save back the change
        for i in range(n):
            if i == 0:
                if self.dominoes[i] == '.' and i + 1 < n and self.dominoes[i + 1] == 'L':
                    doms[i] = 'L'
                    c += 1
                    # print(f"c+1 {i = } {doms = }")
            elif i == n - 1:
                if self.dominoes[i] == '.' and i - 1 >= 0 and self.dominoes[i - 1] == 'R':
                    doms[i] = 'R'
                    c += 1
                    # print(f"c+1 {i = } {doms = }")
            else:  # middle pieces
                if self.dominoes[i] == '.':
                    if self.dominoes[i - 1] == 'R' and self.dominoes[i + 1] != 'L':
                        doms[i] = 'R'
                        c += 1
                        # print(f"c+1 {i = } {doms = }")
                    elif self.dominoes[i - 1] != 'R' and self.dominoes[i + 1] == 'L':
                        doms[i] = 'L'
                        c += 1
                        # print(f"c+1 {i = } {doms = }")

        self.dominoes = doms[:]
        self.runs += 1
        # print(f"{c = } {self.dominoes = }")
        return c

    def pushDominoes(self, dominoes: str) -> str:
        self.dominoes = list(dominoes)
        n = len(self.dominoes)
        self.runs = 0

        while self.push():  # stop only when there's no more change
            pass

        return ''.join(self.dominoes)


"""
Adjacent symbols

any non vertical piece will never change, so we only need to consider vertical ones
for vertical ones, each side could have 2 types of pieces (L or R), beacuse a vertical piece would be considered as part of the consecutive vertical pieces, there's a total of 2x2=9 cases, assuming we extend the entire string with L at beginning  and R at end (which should have no impact on result)
* for a pattern A...B, when A == B, then it should be rewrite into "AAAAAAA"
* for a pattern "R...L", then we will write "RRRLLL", or "RRR.LLL" if we have an odd number of dots. If the initial symbols are at positions i and j, we can check our distance k-i and j-k to decide at position k whether to write 'L', 'R' or '.'
* for pattern "L....R", we don't do anything - skip this case

"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if
                   x != '.']  # only non-dot symbols have impact / would change vertical pieces (dots)
        # extend with dummy start and end
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        # print(f"{symbols = }")
        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            # print(f"{i = } {x = } {j = } {y = }")
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:  # RL
                for k in range(i + 1, j):
                    if k - i > j - k:
                        ans[k] = 'L'
                    elif k - i < j - k:
                        ans[k] = 'R'
                    else:
                        ans[k] = '.'
            # print(f"{ans = }")

        # print(f"{ans = }")
        return "".join(ans)


def main():
    sol = Solution()
    assert sol.pushDominoes(dominoes = "RR.L") == "RR.L", 'fails'

    assert sol.pushDominoes(dominoes = ".L.R...LR..L..") == "LL.RR.LLRRLL..", 'fails'

if __name__ == '__main__':
   main()