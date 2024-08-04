"""
Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!


d = {“foo”, “bar”, “baz”}
setup(d) → void // pre-processing
isMatch(word) → T/F // whether or not the word is in the dictionary


Examples:
isMatch(“foo”) → T
isMatch(“abc”) → F
isMatch(“f.o”) → T // the “.” character matches any one character
isMatch(“.”) → F // no one letter words in the dictionary
isMatch(“..”) → F // no two letter words in the dictionary
isMatch(“...”) → T // there are three letter words in the dictionary

isMatch(“...abcdefg”)
isMatch(“abcdefg...”)
     []
   f
 o
o
time O(N*M) N - max(length of word), M max(len(query word))

"""
from collections import defaultdict


class TrieNode:
    def __init__(self, val):
        self.chilren = defaultdict()
        self.isword = False
        #self.wordcounts = {length: count}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]

        p.isword = True

    def query(self, root, word):
        p = root
        for i, c in enumerate(word):
            if c == '.':
                for child in p.children.values():
                    if self.query(child, word[i + 1:]):
                        return True
                    p = child
            else:
                if c not in p.children:
                    return False
                p = p.children[c]

        return p is not None and p.isword


class Matcher:
    def __init__(self):
        self.trie = TrieNode()

    def setup(self, d):
        for word in d:
            self.trie.insert(word)

    def isMatch(self, pattern):
        return self.trie.query(self.trie.root, pattern)