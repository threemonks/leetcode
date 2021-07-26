"""
451. Sort Characters By Frequency
Medium

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import collections

"""
Bucket sort

1. count frequency of each character
2. for frequency from low to high:
    output all characters with this frequency

time O(N)
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        sfreq = collections.Counter(s)

        sfreq_sorted = sorted(sfreq.items(), key=lambda x: x[1], reverse=True)

        result = ''
        for c, f in sfreq_sorted:
            result += c * f

        return result

def main():
    sol = Solution()
    assert sol.frequencySort("tree") in ["eetr", "eert"], 'fails'

    assert sol.frequencySort("caaabb") in ["aaabbc"], 'fails'


if __name__ == '__main__':
   main()