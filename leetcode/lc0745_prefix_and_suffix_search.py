"""
745. Prefix and Suffix Search
Hard

https://leetcode.com/problems/prefix-and-suffix-search/
"""

from typing import List

"""
Trie 

brutal force use two tries to store all words (or one tries to store each word and its reverse word[::-1]), and search prefix and suffix, return all indexes then intersect to find max index, but this TLE

To improve, we use two separate tries, but store at each node all indexes/weights of all of this node's children

time O(NK^2+QK) N number of words, K maximum length of word, K number of queries
space O(NK^2)

mistakes:
1. use two separate trie for prefix and suffix, not using one trie for both
2. instead of having one node store only weight/index for current word, have the node saves all weights with current prefix (all its children nodes)

"""


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.weights = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, weight):
        p = self.root
        p.weights.append(weight)
        for c in word:
            if not p.children.get(c):
                p.children[c] = TrieNode()
            p = p.children[c]
            p.weights.append(weight)

    def search(self, prefix):
        # print('prefix=%s' % prefix)
        p = self.root
        for c in prefix:
            if not p.children.get(c):
                return []
            p = p.children[c]

        # return weights
        return p.weights


class WordFilter:

    def __init__(self, words: List[str]):
        self.ptrie = Trie()
        self.strie = Trie()
        for idx, word in enumerate(words):
            self.ptrie.insert(word, idx)
            self.strie.insert(word[::-1], idx)

    def f(self, prefix: str, suffix: str) -> int:
        # print('prefix=%s' % prefix)
        p_weights = self.ptrie.search(prefix)
        # print('prefix=%s p_weights=%s' % (prefix, p_weights))
        # print('suffix=%s' % suffix)
        s_weights = self.strie.search(suffix[::-1])
        # print('suffix=%s s_weights=%s' % (suffix, s_weights))
        i, j = len(p_weights) - 1, len(s_weights) - 1
        while i >= 0 and j >= 0:
            if p_weights[i] == s_weights[j]:
                return p_weights[i]
            elif p_weights[i] > s_weights[j]:
                i -= 1
            else:  # p_weights[i] < s_weights[j]:
                j -= 1

        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

def main():

    obj = WordFilter(["apple"])
    assert obj.f(prefix="a", suffix="e") == 0, 'fails'

if __name__ == '__main__':
   main()