## Start typing here
"""
david

david
daniel
adavidson

      []
    d
   a
  v n
 i
d
"""
from collections import deque


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Given a string `username`, insert the string into the data structure and return
    def insert(self, username):
        p = self.root
        for c in username:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]

        p.word = True

    # Given a string `username`, return a boolean whether the username exists
    def contains(self, username):  # david
        p = self.root
        for c in username:
            if c not in p.children:
                return False
            p = p.children[c]

        return p is not None and bool(p.word)

    # Given a string `prefix`, return a list of all usernames that start with the given prefix.
    def startsWith(self, prefix):
        if not prefix:
            return []
        p = self.root
        for c in prefix:
            if c not in p.children:
                return []
            p = p.children[c]

        ans = []

        word = prefix
        if p:
            if p.word:
                ans.append(prefix)
            q = deque([[p, word]])
            while q:
                node, cur_word = q.popleft()
                for c in node.children:
                    if node.children[c].word:
                        ans.append(cur_word + c)
                    q.append([node.children[c], cur_word + c])

        return ans


trie = Trie()
trie.insert("david")
trie.insert("davidson")
trie.insert("bob")
# print(trie.contains('david'))
print(trie.startsWith('davidabc'))
assert trie.contains('david') is True, 'fails'
assert trie.contains('alice') is False, 'fails'
assert trie.startsWith('david') == ["david", "davidson"], 'fails'
assert trie.startsWith('davidson') == ["davidson"], 'fails'
assert trie.startsWith('davidabc') == [], 'fails'
assert trie.contains('') is False, 'fails'
assert trie.startsWith('') == [], 'fails'