"""
953. Verifying an Alien Dictionary
Easy

1747

709

Add to List

Share
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List

"""
Hash Table

store order into hash table with letter as key, index as value.

compare each adjacent word, letter by letter
1. if found difference, and word1[j] > word2[j], this violates dict order, return False
2. if no difference, but word1 reach end, this does not violates dict order, continue to next word pair
3. if no difference, but word1 is longer and word2 reaches end first, this violates dict order, return False

If after checking all word pairs, no violation found, return True

"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}

        n = len(words)
        if n == 1:
            return True

        for i in range(1, n):
            word1, word2 = words[i - 1], words[i]
            j = 0
            while j < min(len(word1), len(word2)) and word1[j] == word2[j]:
                j += 1

            # if word1 is shorter, we are done compare here
            if j == len(word1):
                continue
            # if word2 is shorter, violates dictionary order
            if j == len(word2):
                return False

            # if word1[j] is larger than word2[j], this violates dictionary order
            if d[word1[j]] > d[word2[j]]:
                return False

        # no violation found
        return True


def main():
    sol = Solution()
    assert sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz") == True, 'fails'

    assert sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz") == False, 'fails'

    assert sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz") == False, 'fails'


if __name__ == '__main__':
   main()