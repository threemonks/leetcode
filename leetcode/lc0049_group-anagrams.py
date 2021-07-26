"""
49. Group Anagrams
Medium

5287

231

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
from typing import List
from collections import defaultdict

"""
Hash Table

use sorted word (canonical form) as key, group all words

time O(N*M*log(M)) - N is strs length, M is word length
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        worddct = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            worddct[key].append(word)

        return list(worddct.values())


def main():
    sol = Solution()
    assert sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], 'fails'

    assert sol.groupAnagrams(strs = [""]) ==  [[""]], 'fails'

    assert sol.groupAnagrams(strs = ["a"]) ==  [["a"]], 'fails'

if __name__ == '__main__':
   main()