"""
93. Restore IP Addresses
Medium

1964

588

Add to List

Share
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

0 <= s.length <= 3000
s consists of digits only.
"""
from functools import lru_cache
from typing import List

"""
Backtrack

brutal force bactrack with lru_cache

note:
1. needs to filter out impossible string (len > 12)

"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []

        @lru_cache(None)
        def backtrack(s1, path):
            if len(path) > 4 and not s:
                return
            if not s1:
                if len(path) == 4:
                    res.append('.'.join([str(p) for p in path]))
                return
            n = len(s)
            # one digit
            onedigit = int(s1[0])
            # two digits
            twodigits = -1
            if n >= 2 and s1[0] != '0':
                twodigits = int(s1[:2])
            # three digits
            threedigits = -1
            if n >= 3 and s1[0] != '0':
                threedigits = int(s1[:3])
            if 0 <= onedigit <= 9:
                backtrack(s1[1:], tuple(path + (onedigit,)))
            if 10 <= twodigits <= 99:
                backtrack(s1[2:], tuple(path + (twodigits,)))
            if 100 <= threedigits <= 255:
                backtrack(s1[3:], tuple(path + (threedigits,)))

        backtrack(s, ())

        return res

def main():
    sol = Solution()
    assert sol.restoreIpAddresses(s = "25525511135") == ["255.255.11.135","255.255.111.35"], 'fails'

    assert sol.restoreIpAddresses(s = "0000") == ["0.0.0.0"], 'fails'

    assert sol.restoreIpAddresses(s = "1111") == ["1.1.1.1"], 'fails'

    assert sol.restoreIpAddresses(s = "010010") == ["0.10.0.10","0.100.1.0"], 'fails'

    assert sol.restoreIpAddresses(s = "101023") == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"], 'fails'

if __name__ == '__main__':
   main()