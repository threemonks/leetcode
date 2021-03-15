"""
8. String to Integer (atoi)
Medium

"""


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.lstrip()
        if s.startswith('+') or s.startswith('-'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        num = 0
        if not s or not s[0].isdigit():
            return 0

        for idx, c in enumerate(s):
            if not c.isdigit():
                break
            num = num * 10 + int(c)

        num = sign * num
        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return num


def main():
    sol = Solution()
    assert sol.myAtoi(s = "42") == 42, 'fails'

    assert sol.myAtoi(s = "   -42") == -42, 'fails'

    assert sol.myAtoi(s = "4193 with words") == 4193, 'fails'

    assert sol.myAtoi(s = "words and 987") == 0, 'fails'

    assert sol.myAtoi(s = "-91283472332") == -2147483648, 'fails'



if __name__ == '__main__':
   main()