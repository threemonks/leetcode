"""
820. Short Encoding of Words
Medium

A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.



Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
Example 2:

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].



Constraints:

1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.

"""
import collections
from typing import List
import collections

"""
Trie

1. define a trie
2. insert all words reversed, store its depth along with node, with root node representing '#' with depth 1
3. sum depths of all leave nodes
"""


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = False
        self.depth = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.depth = 1

    def insert(self, word):
        p = self.root
        depth = 1
        for ch in word:
            if not p.children.get(ch):
                p.children[ch] = TrieNode()
            depth += 1
            p = p.children[ch]

        p.word = True
        p.depth = depth


class Solution0:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = [reversed(word) for word in words]
        n = len(words)

        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = 0
        root = trie.root
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            if not cur.children:
                # leave node, add its depth to ans
                ans += cur.depth
            else:
                for child in cur.children.values():
                    queue.append(child)

        # now we just need to get sum of all leaves depth
        return ans


"""
Trie

1. define a trie
2. insert all words reversed, store its depth along with node, with root node representing '#' with depth 1
3. sum depths of all leave nodes

use a dict instead of actual Trie class

Note:
    leaves is a tuple of (node, word len+1), so when 'me' is first added, the node value is {}, length is 2+2, but when 'time' is added, that node value  for length 2+1 is updated to {'e': {'me': {}}}, and a new element of node value {} and length 4+1 is added
"""


class Solution1:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        leaves = []
        root = dict()
        for word in set(words):
            cur = root
            for ch in word[::-1]:
                if ch not in cur:
                    cur[ch] = dict()
                cur = cur[ch]
            leaves.append((cur, len(word) + 1))

        return sum(depth for node, depth in leaves if len(node) == 0)


"""
Set

1. Build a set of words.
2. Iterate on all words and remove all suffixes of every word from the set.
3. Finally the set will the set of all encoding words.
4. Iterate on the set and return sum(word's length + 1 for every word in the set)
"""


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)

        for word in words.copy():
            for i in range(1, len(word)):
                words.discard(word[i:])  # remove all suffixes of word of length 1 to len(word)-1 from words, if exists

        # now just sum the length of remaining word in words
        return sum([len(word) + 1 for word in words])


def main():
    sol = Solution()
    assert sol.minimumLengthEncoding(words = ["time", "me", "bell"]) == 10, 'fails'

    assert sol.minimumLengthEncoding(words = ["t"]) == 2, 'fails'


if __name__ == '__main__':
   main()