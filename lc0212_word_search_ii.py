"""
212. Word Search II
Hard

https://leetcode.com/problems/word-search-ii/

"""
from collections import defaultdict
from typing import List

from collections import defaultdict

"""
Backtracking with Trie

optimizations:
1. Backtrack along the nodes in Trie, so we pass root node along with backtracking call
2. gradually prune the nodes in Trie during backtracking
3. keep words in the Trie (then we don't need to pass prefix along with backtrack recursive call, and no need to rebuild word from prefix)
4. remove the matched words from the Trie

TLE

"""

class TrieNodeDict:
    def __init__(self):
        self.children = defaultdict(TrieNodeDict)
        self.is_word = False

class TrieDict:
    def __init__(self):
        self.root = TrieNodeDict()

    def insert(self, word):
        p = self.root
        for c in word:
            p = p.children[c]

        p.is_word = True

    def search(self, word):
        p = self.root
        for c in word:
            if p.children.get(c) is None:
                return False
            p = p.children.get(c)

        return p is not None and p.is_word is True

    def startsWith(self, prefix):
        p = self.root
        for c in prefix:
            if p.children.get(c) is None:
                return False
            p = p.children.get(c)

        return p is not None

class Solution0:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        trie = TrieDict()
        for word in words:
            trie.insert(word)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []

        def backtrack(row, col, curr, parent):
            # base case
            c = board[row][col]
            node = parent.children.get(c)
            if not node:
                return
            if node.is_word:
                result.append(curr+c)
                node.is_word = False # remove this word after we identified it to speed up performance

            # mark node as visited for this path
            board[row][col] = '#' # mark with # to avoid revisiting this node along this same path

            # explore all valid neighbors
            for nrow, ncol in [(row+dr, col+dc) for dr, dc in dirs if 0<=row+dr<m and 0<=col+dc<n]:
                backtrack(nrow, ncol, curr+c, node)

            # restore the letter in this node for other path explorations
            board[row][col] = c

        for i in range(m):
            for j in range(n):
                if trie.startsWith(board[i][j]):
                    backtrack(i, j, '', trie.root)

        return result


"""
Backtracking with Trie

optimizations:
1. Backtrack along the nodes in Trie, so we pass root node along with backtracking call
2. gradually prune the nodes in Trie during backtracking
3. keep words in the Trie (then we don't need to pass prefix along with backtrack recursive call, and no need to rebuild word from prefix)
4. remove the matched words from the Trie

Try to improve
1. remove trie.search startsWith
2. trie children use array and ord(c)-ord('a')

still TLE
"""

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False

char2idx = lambda x: ord(x)-ord('a')

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for c in word:
            if not p.children[char2idx(c)]:
                p.children[char2idx(c)] = TrieNode()
            p = p.children[char2idx(c)]

        p.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = []

        def backtrack(row, col, curr, parent):
            # base case
            c = board[row][col]
            if c == '#':
                return
            node = parent.children[char2idx(c)]
            if not node:
                return
            if node.is_word:
                result.append(curr+c)
                node.is_word = False # remove this word after we identified it to speed up performance

            # mark node as visited for this path
            board[row][col] = '#' # mark with # to avoid revisiting this node along this same path

            # explore all valid neighbors
            for nrow, ncol in [(row+dr, col+dc) for dr, dc in dirs if 0<=row+dr<m and 0<=col+dc<n]:
                backtrack(nrow, ncol, curr+c, node)

            # restore the letter in this node for other path explorations
            board[row][col] = c

        for i in range(m):
            for j in range(n):
                if trie.root.children[char2idx(board[i][j])]:
                    backtrack(i, j, '', trie.root)

        return result

def main():
    sol = Solution()
    assert sorted(sol.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"])) == sorted(["eat","oath"]), 'fails'

    assert sol.findWords(board = [["a","b"],["c","d"]], words = ["abcb"]) == [], 'fails'

    assert sol.findWords([["a"]], ["a"]) == ['a'], 'fails'


if __name__ == '__main__':
   main()