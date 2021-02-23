"""
211. Design Add and Search Words Data Structure
Medium

https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class WordNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            if not p.children.get(c):
                p.children[c] = WordNode()
            p = p.children[c]

        p.is_word = True

    def _search(self, word: str, parent=None) -> bool:
        p = parent
        for idx, c in enumerate(word):
            if c == '.':
                for pp in p.children:
                    if self._search(word[idx + 1:], p.children.get(pp)):
                        return True
                return False
            else:
                if not p.children.get(c):
                    return False
                p = p.children[c]

        return p is not None and p.is_word is True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

def main():

    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    assert obj.search("pad") is False, 'fails'
    assert obj.search("bad") is True, 'fails'
    assert obj.search(".ad") is True, 'fails'
    assert obj.search("b..") is True, 'fails'

if __name__ == '__main__':
   main()