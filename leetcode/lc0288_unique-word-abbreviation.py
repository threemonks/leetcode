"""
288. Unique Word Abbreviation
Medium

147

1547

Add to List

Share
The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.

For example:

dog --> d1g because there is one letter between the first letter 'd' and the last letter 'g'.
internationalization --> i18n because there are 18 letters between the first letter 'i' and the last letter 'n'.
it --> it because any word with only two characters is an abbreviation of itself.
Implement the ValidWordAbbr class:

ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
There is no word in dictionary whose abbreviation is equal to word's abbreviation.
For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.


Example 1:

Input
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
Output
[null, false, true, false, true, true]

Explanation
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // return false, dictionary word "deer" and word "dear" have the same abbreviation "d2r" but are not the same.
validWordAbbr.isUnique("cart"); // return true, no words in the dictionary have the abbreviation "c2t".
validWordAbbr.isUnique("cane"); // return false, dictionary word "cake" and word "cane" have the same abbreviation  "c2e" but are not the same.
validWordAbbr.isUnique("make"); // return true, no words in the dictionary have the abbreviation "m2e".
validWordAbbr.isUnique("cake"); // return true, because "cake" is already in the dictionary and no other word in the dictionary has "c2e" abbreviation.


Constraints:

1 <= dictionary.length <= 3 * 10^4
1 <= dictionary[i].length <= 20
dictionary[i] consists of lowercase English letters.
1 <= word.length <= 20
word consists of lowercase English letters.
At most 5000 calls will be made to isUnique.
"""
from collections import defaultdict
from typing import List

"""
String / Design

We are trying to search for a word in a dictionary. If this word (also this word’s abbreviation) is not in the dictionary OR this word and only it’s abbreviation in the dictionary. We call a word’s abbreviation unique.

"""


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.words = set(dictionary)
        self.maps = defaultdict(int)

        for word in set(dictionary):
            wordabbr = self.abbrv(word)
            self.maps[wordabbr] += 1

    def abbrv(self, word):
        if len(word) > 2:
            word = word[0] + str(len(word) - 2) + word[-1]

        return word

    def isUnique(self, word: str) -> bool:
        wordabbr = self.abbrv(word)
        if word not in self.words and self.maps[wordabbr] == 0:
            return True
        elif word in self.words and self.maps[wordabbr] == 1:
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

def main():
    obj = ValidWordAbbr(["deer", "door", "cake", "card"])
    assert obj.isUnique("dear") is False, 'fails'

    assert obj.isUnique("cart") is True, 'fails'

    assert obj.isUnique("cane") is False, 'fails'

    assert obj.isUnique("make") is True, 'fails'

    assert obj.isUnique("cake") is True, 'fails'

if __name__ == '__main__':
   main()