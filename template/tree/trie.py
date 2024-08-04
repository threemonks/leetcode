import collections


class TrieNode0:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False


class Trie0:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        """
        p = self.root
        length = len(word)
        for level in range(length):
            if not p.children[ord(word[level]) - ord('a')]:
                p.children[ord(word[level]) - ord('a')] = TrieNode()
            p = p.children[ord(word[level]) - ord('a')]

        p.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        p = self.root
        length = len(word)
        for level in range(length):
            if not p.children[ord(word[level]) - ord('a')]:
                return False
            p = p.children[ord(word[level]) - ord('a')]

        return p is not None and p.is_word is True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        length = len(prefix)
        for level in range(length):
            if not p.children[ord(prefix[level]) - ord('a')]:
                return False
            p = p.children[ord(prefix[level]) - ord('a')]

        return p is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
use defaultdict to store children makes code simplier (might be slower than array)

mistakes:
1. to create a new node p.children[c] = TrieNode()
2. defaultdict dct[key] creates non-existing using default value of the type, dct.get(key) will return None for non-existing key
"""
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        """
        p = self.root
        for c in word:
            if p.children.get(c) is None:
                p.children[c] = TrieNode()
            p = p.children.get(c)

        p.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        p = self.root
        for ch in word:
            p = p.children.get(ch)
            if p is None:
                return False

        return p is not None and p.is_word is True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for ch in prefix:
            p = p.children.get(ch)
            if p is None:
                return False

        return p is not None


def main():
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True

    trie = Trie()
    assert trie.startsWith('a') is False

if __name__ == '__main__':
   main()