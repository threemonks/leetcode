"""
692. Top K Frequent Words
Medium

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
import heapq
import collections
from typing import List
"""
using builtin lib Counter and heapq
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        topk = heapq.nsmallest(k, [(-count, word) for (word, count) in counter.items()])

        return [word for count, word in topk]

"""
using Counter
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        return [v[0] for v in sorted([(item, -count) for item, count in counter.items()], key=lambda x: (x[1], x[0]))][:k]


def main():
    sol = Solution()
    assert sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"], 'fails'

    assert sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"], 'fails'


if __name__ == '__main__':
   main()