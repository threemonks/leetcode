"""
https://leetcode.com/discuss/interview-question/1012161/amazon-phone-interview-valid-dictionary-word-from-phone-number

You're given a phone number as a string of digits of variable length (N). You need to find all
possible valid words that can be formed from that number by using the letter mapping on the
phone, that is 2='abc', 3='def', 4='ghi', 5='jkl', 6='mno', 7='pqrs', 8='tuv' and 9='wxyz'.
You're responsible for building a build_options function which will return all the words that
can be spelled with those numbers.
You can assume you have a valid word dictionary like /var/lib/dict from Linux systems and a
function load_dict() that loads the dictionary into any datastructure you prefer, such as:
def load_dict(): [];
Which will return something like ['a','and','also',...'zebra']
Given build_options('76278')
Return ['roast', 'smart', 'snast']

Aspiring for L6 SDE III. 16+ years programmer, 9+ years Android.
I suggested backtracking ( recursion ) but it is exponential time-complexity, and load_dict() is not checking validity of current word, instead returns a data-structure, so I suggested Trie, but failed to implement even the base-case for a Trie based approach where we meet mid-way between traversing the input phone-number digits against valid Trie dictionary word formation.

Backtracking approach is a brute force method here as you're checking for all possible combinations of word against the word dictionary. The time to generate the combinations will O(4^n) in the worst case and O(3^n) if you ignore the " 9='wxyz' " case. Also, the check for the match is again going to cost you a lot in terms of space, if you convert the list into set. Remember that the dictionary can be of huge volume and space optimization is definitely needed.
If you avoid the conversion to set, then its going to take O(size(word_dict) * avg_word_size * 4^n) at worst, which is really bad.

The trie implementation is the optimal strategy here as you'll build the trie first and then check against the wordEnd to see if that word exists in the dictionary.
Time:

Build Trie - O(size(word_dict) * avg_word_size)
Backtracking(optimal) - O(4^n)
Note that we're ignoring the cases that don't have the corresponding letter in dictionary. That's some optimization there
Total time - O(size(word_dict) * avg_word_size) + O(4^n)

Took me around 45 mins to code and test the entire thing. Hope you find this useful

"""

word_dict = ['a','and','also', 'qnbpt', 'qnbut', 'qnbps', 'roast', 'smart', 'snast', 'zebra']
phone_pad = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

def load_dict():
    return word_dict

def build_options(number):
    trie = Trie(load_dict())
    trie.build_trie()
    return trie.search_word_with_number(number)


class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Trie():
    def __init__(self, word_dict):
        self.word_dict = word_dict
        self.root = TrieNode()

    def addWord(self, word):
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]
        root.isWordEnd = True

    def build_trie(self):
        for word in self.word_dict:
            self.addWord(word)

    def search_word_with_number(self, number):
        root = self.root
        self.res = []
        def dfs(path, root, start):
            if len(path) == len(number):
                if root.isWordEnd:
                    self.res.append(path)
                return

            digit = int(number[start])
            for letter in phone_pad[digit]:
                if letter not in root.children:
                    continue
                tmp = root
                root = root.children[letter]
                dfs(path + letter, root, start+1)
                root = tmp

        dfs('', root, 0)
        return self.res


assert(build_options('76278')) == ['qnbpt', 'roast', 'smart', 'snast']


def main():
    pass

if __name__ == '__main__':
    main()
