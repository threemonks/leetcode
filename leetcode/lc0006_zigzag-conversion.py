"""
6. ZigZag Conversion
Medium

"""
import itertools
"""
we build a grid to store the zigzag patterns from top to bottom, and left to right
for row%(row-1) == 0, we fill entire row
otherwise, we fill a char at position rows-1-r%(rows-1)
until entire string is done

when finish, tranpose the string array and join back into one string

time O(N)
"""
class Solution:
    def convert(self, s: str, rows: int) -> str:
        if rows == 1: # nothing to do
            return s

        n = len(s)

        cells = []
        i = 0
        r = 0
        while i < n:
            if r % (rows-1) == 0: # entire row
                cells.append(list(s[i:i+rows]))
                i += rows
            else: # add one letter at rows-1-r%(rows-1) position
                emptys = [' '] * rows
                emptys[rows-1-r%(rows-1)] = s[i] # zigzag, this goes from bottom to up.
                cells.append(emptys)
                i += 1
            r += 1

        # print(cells)

        # transpose cells
        cells1 = list(map(list, itertools.zip_longest(*cells)))
        # print(cells1)

        return ''.join([''.join([s for s in s1 if s]) for s1 in cells1]).replace(' ', '')


def main():
    sol = Solution()
    assert sol.convert(s = "PAYPALISHIRING", rows = 3) == "PAHNAPLSIIGYIR", 'fails'

    assert sol.convert(s = "PAYPALISHIRING", rows = 4) == "PINALSIGYAHRPI", 'fails'

    assert sol.convert(s = "A", rows = 1) == "A", 'fails'


if __name__ == '__main__':
   main()