"""
425. Word Squares
Hard
https://leetcode.com/problems/word-squares/
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p.words.append(word)
            p = p.children[c]

        p.is_word = True

    def search(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]

        return p is not None and p.is_word is True

    def startsWith(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p.children:
                return []
            p = p.children[c]

        if p is not None:
            return p.words
        else:
            return []

"""
Trie Backtrack
process one row at a time, each row verify if it satisfy square requirement with all previous rows, if not backtrack
until last row

notes:
backtrack approach seems very slow

mistakes:
1. for 2nd row and later, we can use longer prefix (instead of just one char) to find better matched potential words
"""
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        results = []
        def backtrack(row, matrix):
            # print('row=%s matrix=%s' % (row, matrix))
            # base case
            if row >= len(matrix[0]):
                # print('row=%s result %s' % (row, matrix))
                results.append(matrix)
                return
            prefix = ''.join([word[row] for word in matrix[:row]])
            prefix_words = trie.startsWith(prefix)
            # print('checking prefix %s prefix_words=%s' % (matrix[0][row], prefix_words))
            for pword in prefix_words:
                # validate pword
                if any([pword[j] != matrix[j][row] for j in range(1, row)]):
                    continue
                # add this pword
                # print('row=%s matrix=%s adding pword=%s' % (row, matrix, pword))
                # explore further
                backtrack(row+1, matrix + [pword])
                # backtrack

        for word in words:
            backtrack(1, [word])

        return results


def main():
    sol = Solution()
    assert sol.wordSquares(["area","lead","wall","lady","ball"]) == [ [ "wall", "area", "lead", "lady"], [ "ball", "area", "lead", "lady"] ], 'fails'

    assert sol.wordSquares(["abat","baba","atan","atal"]) == [ [ "baba", "abat", "baba", "atan"], [ "baba", "abat", "baba", "atal"] ], 'fails'

if __name__ == '__main__':
   main()