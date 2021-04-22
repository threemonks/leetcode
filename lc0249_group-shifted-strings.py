"""
249. Group Shifted Strings
Medium

752

154

Add to List

Share
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.



Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]


Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict

"""
Hash Table

calculate the word character ord difference, which should remain the same while shifting
we store word character ord value difference, then convert it back to char (based at 'a'), so that the result is a canonical form or 'abcd...z' that we can store as key
if we do word[i]-word[i-1], sincew word[i] could be smaller char than word[i-1], to simulate the circular shift, we do the following

(ord(word[i])-ord(word[i-1])+26)%26

which guarantees the result is a number between 0 and 25

mistakes1:
1. word[i] could be smaller than word[i-1], needs to mod 26
"""


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strings:
            key = ''.join([chr((ord(word[i]) - ord(word[i - 1]) + 26) % 26 + ord('a')) for i in range(1, len(word))])
            # print('word=%s key=%s' % (word, key))
            groups[key].append(word)

        return list(groups.values())

def main():
    sol = Solution()
    assert sol.groupStrings(strings = ["abc","bcd","acef","xyz","az","ba","a","z"]) == [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']], 'fails'

    assert sol.groupStrings(strings = ["a"]) == [["a"]], 'fails'


if __name__ == '__main__':
   main()