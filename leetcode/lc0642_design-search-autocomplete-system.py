"""
642. Design Search Autocomplete System
Hard

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.


Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.


Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.


"""
import collections
from typing import List

"""
Trie

observation
stores history hit count with Trie node, and also all sentences for given prefix at the prefix node

keep history of input chars, and reset it when '#' is received

time O(k*l) l: number of sentences, k: sentence avg length

"""


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0
        self.sentences = []  # store sentences below this node # how about hotness degree?


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, count=1):
        p = self.root
        for c in s:
            p = p.children[c]
            if s not in p.sentences:
                p.sentences.append(s)

        p.count += count

    def search(self, prefix):
        p = self.root
        for c in prefix:
            if p.children.get(c) is None:
                break
            p = p.children[c]

        return p is not None and p.count > 0

    def get_count(self, s):
        p = self.root
        for c in s:
            if p.children.get(c) is None:
                break
            p = p.children[c]

        if p:
            return p.count
        else:
            return 0

    def query(self, prefix):
        p = self.root
        for c in prefix:
            if p.children.get(c) is None:
                return []
            p = p.children[c]

        results = []
        for s in p.sentences:
            count = self.get_count(s)
            results.append((-count, s))  # reverse so that it compares same direction as string comparison

        # sort by count, then sentence, and return first three sentences
        return [s for c, s in sorted(results)[:3]]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.data = dict(zip(sentences, times))
        self.trie = Trie()
        for s, count in zip(sentences, times):
            self.trie.insert(s, count)

        self.inputs = ''

    def input(self, c: str) -> List[str]:
        if c == '#':  # process sentence entered so far
            self.trie.insert(self.inputs)
            # after processing, reset self.inputs
            self.inputs = ''
            return []
        else:  # longer prefix
            self.inputs += c
            results = self.trie.query(self.inputs)
            return results


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

def main():
    obj = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
    assert obj.input('i') == ["i love you", "island","i love leetcode"], 'fails'
    assert obj.input(' ') == ["i love you","i love leetcode"], 'fails'
    assert obj.input('a') == [], 'fails'
    assert obj.input('#') == [], 'fails'


if __name__ == '__main__':
   main()