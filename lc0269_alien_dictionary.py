"""
269. Alien Dictionary
Hard

There is a new alien language that uses the English alphabet. However, the order among letters are unknown to you.

You are given a list of strings words from the dictionary, where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language, and return it. If the given input is invalid, return "". If there are multiple valid solutions, return any of them.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
import collections
from typing import List

"""
observation:
words are sorted in lexicographically => for each pair of immediately adjacent words words[i] and words[i+1], the first character that is different in this two words gives a pair of adj nodes of the graph
construct the graph using this adjacency list, and output the graph as topologically sorted
special case:
  abc, ab => invalid order
"""


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # no word, or word only but more than 1 character, will not determine an order properly
        if not words:
            return ""

        adj_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)

        for i in range(len(words)):
            for c in words[i]:
                indegrees[c] = 0

        for i in range(len(words) - 1):
            s = words[i]
            t = words[i + 1]
            if len(s) > len(t) and s.startswith(t): # take care of invalid order "abc", "ab"
                return ""

            for j in range(min(len(s), len(t))):
                if s[j] == t[j]:
                    continue
                else:
                    if t[j] not in adj_list[s[j]]:  # avoid adding same edge twice, causing incorrect inderee count
                        adj_list[s[j]].append(t[j])
                        indegrees[t[j]] += 1
                    # once we encounter an pair of chars not match, remaining chars order does not matter
                    break

        print('adj_list=%s' % adj_list)
        print('indegrees=%s' % indegrees)

        sources = collections.deque()
        for c in indegrees.keys():
            if indegrees[c] == 0:
                sources.append(c)
        print('sources=%s' % sources)

        sorted_list = []
        while sources:
            vertex = sources.pop()
            sorted_list.append(vertex)
            if vertex in adj_list:
                children = adj_list[vertex]
                for child in children:
                    indegrees[child] -= 1
                    if indegrees[child] == 0:
                        sources.append(child)

        print("sorted_list=%s" % sorted_list)
        if len(sorted_list) != len(indegrees):  # detect cycle
            return ""
        else:
            return "".join(sorted_list)


def main():
    sol = Solution()
    assert sol.alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf", 'fails'

    assert sol.alienOrder(["z","x"]) == "zx", 'fails'

    assert sol.alienOrder(["z","x","z"]) == "", 'fails'

    assert sol.alienOrder(["z","z"]) == "z", 'fails'

    assert sol.alienOrder(["abc", "ab"]) == "", 'fails'

    assert sol.alienOrder(["wrt", "wrtkj"]) == 'jktrw', 'fails'

    assert sol.alienOrder(["ac","ab","zc","zb"]) == "cbaz", 'fails'

if __name__ == '__main__':
   main()