"""
423. Reconstruct Original Digits from English
Medium

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

"""
import collections

"""
Hash Map

Observation

note unique characters in some digit words, and after we considering some digit words, some remaining digit words have unique letters again

zero: Only digit with z
two: Only digit with w
four: Only digit with u
six: Only digit with x
eight: Only digit with g

After that, we can count remaining unique characters
three: only digit with h after eight
five: only digit with f after four
seven: only digit with s after six
nine: only digit with i after five, six, and eight
one: only digit with n after seven and nine

The odd ones for easy looking, each one's letters all also appear in other digit words:
one, three, five, seven, nine

"""


class Solution:
    def originalDigits(self, s: str) -> str:
        counts = collections.defaultdict(int)
        for c in s:
            counts[c] += 1

        # hashmap holding output digit -> its frequency
        out = {}
        # letter z only presents in zero
        out['0'] = counts['z']

        # letter w only presents in two
        out['2'] = counts['w']

        # letter u only presents in four
        out['4'] = counts['u']

        # letter x only presents in six
        out['6'] = counts['x']

        # letter g only presents in eight
        out['8'] = counts['g']

        # letter g only presents in three and eight
        out['3'] = counts['h'] - out['8']

        # letter f only presents in four and five
        out['5'] = counts['f'] - out['4']

        # letter s only presents in six and seven
        out['7'] = counts['s'] - out['6']

        # letter i only presents in five and six, nine and eight
        out['9'] = counts['i'] - out['5'] - out['6'] - out['8']

        # letter n only presents in one, seven and nine
        out['1'] = counts['n'] - out["7"] - 2 * out['9']

        return ''.join([k * out[k] for k in sorted(out.keys())])


def main():
    sol = Solution()
    assert sol.originalDigits("owoztneoer") == '012', 'fails'

    assert sol.originalDigits("fviefuro") == '45', 'fails'


if __name__ == '__main__':
   main()