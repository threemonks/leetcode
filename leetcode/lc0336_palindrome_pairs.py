"""
336. Palindrome Pairs
Hard

https://leetcode.com/problems/palindrome-pairs/
"""
from typing import List
import collections

"""
Trie

Observation:

Different ways two words can form a palindrome:
1. equal length, but reverse, word1 == word2[::-1], empty string as remaining suffix (also valid palindrome)
    CAT TAC
or not equal length, assuming len(word1)>len(word2), can form palindrome if:

2. word1 startswith word2[::-1], and if we remove word2[::-1] from word1, the remaining suffix of word1 is a palindrome
    CATSOLOS TAC
3. word2 ends with word1[::-1], and word2 prefix (excluding word1[::-1]) is a palindrome
    CAT SOLOSTAC

So the idea is to store all words reversed with index into Trie, and also store valid palindrome suffix with each prefix/word, which will allow us to search for given prefix and if the remaining part (suffix) of the word forms palindrome.

Algorithm:
For each word, reverse and identify its palindrome prefixes (suffixes of the reversed word). Insert the word into the Trie, mark the final letter as ending, attach word index. Also, while inserting, note any points where the remainder of the word is a palindrome suffix by including the index in an additional list.

Then we go through the list of words, lookup each in the Trie. Any of the following conditions give us palindrome pairs:
1. we have no letters left on the word, and are at a word end node (case 1, equal length and reverse)
2. we have no letters left on the word, and there are indexes in the list attached to the node (palindromes_below) (case 2)
3. we have a palindrome left on the word and are on a word end node (case 3)

"""
import collections

"""
Trie

Observation:

Different ways two words can form a palindrome:
1. equal length, but reverse, word1 == word2[::-1], empty string as remaining suffix (also valid palindrome)
    CAT TAC
or not equal length, assuming len(word1)>len(word2), can form palindrome if:

2. word1 startswith word2[::-1], and if we remove word2[::-1] from word1, the remaining suffix of word1 is a palindrome
    CATSOLOS TAC
3. word2 ends with word1[::-1], and word2 prefix (excluding word1[::-1]) is a palindrome
    CAT SOLOSTAC

So the idea is to store all words reversed with index into Trie, and also store valid palindrome suffix with each prefix/word, which will allow us to search for given prefix and if the remaining part (suffix) of the word forms palindrome.

Algorithm:
For each word, reverse and identify its palindrome prefixes (suffixes of the reversed word). Insert the word into the Trie, mark the final letter as ending, attach word index. Also, while inserting, note any points where the remainder of the word is a palindrome suffix by including the index in an additional list.

Then we go through the list of words, lookup each in the Trie. Any of the following conditions give us palindrome pairs:
1. we have no letters left on the word, and are at a word end node (case 1, equal length and reverse)
2. we have no letters left on the word, and there are indexes in the list attached to the node (palindromes_below) (case 2)
3. we have a palindrome left on the word and are on a word end node (case 3)

"""
import collections

"""
Trie

Observation:

Different ways two words can form a palindrome:
1. equal length, but reverse, word1 == word2[::-1], empty string as remaining suffix (also valid palindrome)
    CAT TAC
or not equal length, assuming len(word1)>len(word2), can form palindrome if:

2. word1 startswith word2[::-1], and if we remove word2[::-1] from word1, the remaining suffix of word1 is a palindrome
    CATSOLOS TAC
3. word2 ends with word1[::-1], and word2 prefix (excluding word1[::-1]) is a palindrome
    CAT SOLOSTAC

So the idea is to store all words reversed with index into Trie, and also store valid palindrome suffix with each prefix/word, which will allow us to search for given prefix and if the remaining part (suffix) of the word forms palindrome.

Algorithm:
For each word, reverse and identify its palindrome prefixes (suffixes of the reversed word). Insert the word into the Trie, mark the final letter as ending, attach word index. Also, while inserting, note any points where the remainder of the word is a palindrome suffix by including the index in an additional list.

Then we go through the list of words, lookup each in the Trie. Any of the following conditions give us palindrome pairs:
1. we have no letters left on the word, and are at a word end node (case 1, equal length and reverse)
2. we have no letters left on the word, and there are indexes in the list attached to the node (palindromes_below) (case 2)
3. we have a palindrome left on the word and are on a word end node (case 3)

mistakes:
1. index default -1 indicates not end of word
2. store palindromes_below (indicates a reversed word with prefix ending at this node has all remaining part (suffix) being palindrome)
3. output palindrome pair needs to make sure in correct order (note the extra suffix palindrome (or prefix palindrome considering reversing)), and trie stores reversed word

time O(k^2*N) - k: longest word length, N: number of words, for each word O(N), insert into trie O(k), also check whether remaining part is palindrome O(k) => O(N*k^2)
space O((k+N)^2) trie
"""
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.index = -1  # if word ends at this node
        self.palindromes_below = []  # contains indexes for all words below this node, whose remaining part below this node are palindrome


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        p = self.root
        for i, c in enumerate(word):
            if word[i:] == word[i:][::-1]:
                p.palindromes_below.append(index)
            if p.children.get(c) is None:
                p.children[c] = TrieNode()
            p = p.children[c]

        p.index = index

    def query(self, word, index):
        # find a word in trie that would concetnate with current word to form a palindrome
        result = []
        p = self.root
        for i, c in enumerate(word):
            #  case 3 trie has word (reversed) matching my prefix, and my remaining suffix is palindrome
            if p.index >= 0 and word[i:] == word[i:][::-1]:
                result.append([index,
                               p.index])  # why is this p.index, index, not index, p.index? because words inserted are reversed?
            if p.children.get(c) is None:
                break
            p = p.children[c]
        else:
            # case 1, equal length
            if p.index >= 0 and p.index != index:
                result.append([index, p.index])
            # case 2, my word ends, trie has words with matching suffix and prefix is palindrome
            for pb_index in p.palindromes_below:
                result.append([index, pb_index])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        # insert words reversed, since when look for word pair to concatneate into palindrome
        # we are looking for words when reversed, has same prefix as current work being checked
        # and the remaining suffix part of longer word being palindrome
        for index, word in enumerate(words):
            trie.insert(word[::-1], index)

        result = []
        for index, word in enumerate(words):
            pp = trie.query(word, index)
            result.extend(pp)

        return result


def main():
    sol = Solution()
    assert sol.palindromePairs(words = ["abcd","dcba","lls","s","sssll"]) == [[0,1],[1,0],[3,2],[2,4]], 'fails'

    assert sol.palindromePairs(words = ["bat","tab","cat"]) == [[0,1],[1,0]], 'fails'

    assert sol.palindromePairs(words = ["a",""]) == [[0,1],[1,0]], 'fails'


if __name__ == '__main__':
   main()
