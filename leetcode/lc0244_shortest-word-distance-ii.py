"""
244. Shortest Word Distance II
Medium

584

167

Add to List

Share
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.


Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1


Constraints:

1 <= wordsDict.length <= 3 * 10^4
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""
from typing import List

"""
Hash Table / Two Pointers

use hash table to store word with  all its index (sorted list) as value

time O(N)
"""
from sortedcontainers import SortedList


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = dict()
        for i, word in enumerate(wordsDict):
            if word in self.words:
                self.words[word].add(i)
            else:
                self.words[word] = SortedList([i])

    def shortest(self, word1: str, word2: str) -> int:
        pos1 = self.words[word1]
        pos2 = self.words[word2]
        i, j = 0, 0
        ans = math.inf
        while i < len(pos1) and j < len(pos2):
            ans = min(ans, abs(pos1[i] - pos2[j]))
            if pos1[i] < pos2[j]:
                i += 1
            else:
                j += 1

        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)


def main():
    wordDistance = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    wordDistance.shortest("coding", "practice")  #return 3
    wordDistance.shortest("makes", "coding") # return 1

if __name__ == '__main__':
   main()