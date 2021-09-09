"""
418. Sentence Screen Fitting
Medium

675

336

Add to List

Share
Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.



Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
Example 3:

Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.


Constraints:

1 <= sentence.length <= 100
1 <= sentence[i].length <= 10
sentence[i] consists of lowercase English letters.
1 <= rows, cols <= 2 * 104
"""
from typing import List

"""
Greedy

Imagine that s is the sentence repeated infinitely and s.substring(0, i) is the part that can be fitted into the text file with given rows and cols.
Then, the answer we want is i/n -- i.e. number of repetitions of the sentence.
When fitting each row of the text file with the sentence, we just need to check if the current offset i falls on a word or not, if it does, we need to revert the offset back to the beginning of the word, otherwise, we just keep fitting the next row.

"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "

        l = len(s)

        ans = 0
        i = 0 # which char in s we will start at beginning of this line

        for r in range(rows):
            # start at r, does s[(start+cols)%l] ends at whitespace?
            i += cols
            while s[i%l] != ' ': # if last char of the row is not whitespace, go back to a space (word cannot span rows)
                i -= 1
            # now we are at a whitespace, advance i by 1 since next row will start at the char after this whitespace
            i += 1

        return i // l

def main():
    sol = Solution()
    assert sol.wordsTyping(sentence = ["hello","world"], rows = 2, cols = 8) == 1, 'fails'

    assert sol.wordsTyping(sentence = ["a", "bcd", "e"], rows = 3, cols = 6) == 2, 'fails'

    assert sol.wordsTyping(sentence = ["i","had","apple","pie"], rows = 4, cols = 5) == 1, 'fails'

if __name__ == '__main__':
   main()