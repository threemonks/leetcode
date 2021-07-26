"""
1461. Check If a String Contains All Binary Codes of Size K
Medium
"""
"""
String / Bit Manipulation / Set

check if String has at least 2**k different subsets

"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()

        for i in range(k, len(s) + 1):
            if s[i - k:i] not in seen:
                seen.add(s[i - k:i])
            if len(seen) >= 2 ** k:
                return True

        return False


"""
Rolling Hash of each bit of strng s

"""


class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        mask = (1 << k) - 1  # bit mask to keep only k bits of numbers
        curr = 0  # starting value

        for i in range(len(s)):
            curr = ((curr << 1) & mask) | (int(s[i]))  # left shift one bit, then add latest bit of s
            # only want hash when i-k+1 > 0
            if i >= k - 1 and curr not in seen:
                seen.add(curr)
            if len(seen) >= 2 ** k:
                return True

        return False


def main():
    sol = Solution()
    assert sol.hasAllCodes(s = "00110110", k = 2) == True, 'fails'

    assert sol.hasAllCodes(s = "00110", k = 2) == True, 'fails'

    assert sol.hasAllCodes("0110", k = 2) == False, 'fails'

    assert sol.hasAllCodes(s = "0000000001011100", k = 4) == False, 'fails'

if __name__ == '__main__':
   main()