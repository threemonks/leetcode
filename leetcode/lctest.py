import math


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        sign = 1
        if n[0] == '-':
            sign = -1
            n = n[1:]

        ans = ''
        if sign == 1:
            for c in n:
                if ord(c) - ord('0') > x:
                    ans += c
                else:
                    ans += str(x)
                    x = -math.inf
                    ans += c
                print('c=%s ans=%s' % (c, ans))
        else:  # negative
            for c in n:
                if ord(c) - ord('0') < x:
                    ans += c
                else:
                    ans += str(x)
                    x = math.inf
                    ans += c
        return ans

def main():
    sol = Solution()
    assert sol.maxValue("28824579515", 8) == "828824579515", 'fails'


if __name__ == '__main__':
   main()