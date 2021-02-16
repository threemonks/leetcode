"""
68. Text Justification
Hard

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List

"""
two pointers, i, j point at start and end index of words of given line, calculate total extra spaces to pad for a line as maxWidth - len(' '.join(line)), if maxWidth - len(' '.join(line)) > num of words in line - 1, means some word gaps in left has one more space than right, all word spaces have (maxWidth - len(' '.join(line))) // (num of words in line - 1) extra spaces, but the left most (maxWidth - len(' '.join(line))) % (num of words in line - 1) has one extra space in addition to the average extra spaces.

time O(N) -- all words are checked exactly once
space O(N) -- result

mistakes:
1. treated last line same as single word line, but last line could have multiple words
2. left most word gaps with ONE more extra space than gaps to right
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        result = []

        i = 0
        while i < n:
            j = i + 1
            while j <= n and len(' '.join(words[i:j])) <= maxWidth:
                j += 1

            # now line has one word more than enough
            j -= 1
            line = words[i:j]
            i = j
            line_word_count = len(line)

            extra_spaces = maxWidth - len(' '.join(line))

            if line_word_count == 1:  # single word
                result.append(line[0] + ' ' * extra_spaces)
                continue
            elif j == n:  # last line
                result.append(' '.join(line) + ' ' * extra_spaces)
                continue

            line_slot_count = line_word_count - 1
            if extra_spaces > line_slot_count:
                avg_extra_space_per_slot = extra_spaces // line_slot_count
                left_slot_w_extra_space = extra_spaces % line_slot_count
            else:
                avg_extra_space_per_slot = 0
                left_slot_w_extra_space = extra_spaces
            res = ''
            for k in range(len(line)):
                if not res:
                    res += line[k]
                else:
                    if k <= left_slot_w_extra_space:
                        res += ' ' * avg_extra_space_per_slot + ' ' * 1 + ' ' + line[k]
                    else:
                        res += ' ' * avg_extra_space_per_slot + ' ' + line[k]

            result.append(res)

        return result


def main():
    sol = Solution()
    assert sol.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16) == [ "This    is    an", "example  of text", "justification.  " ], 'fails'

    assert sol.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16) == [ "What   must   be", "acknowledgment  ", "shall be        " ], 'fails'

    assert sol.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20) == [ "Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  " ], 'fails'

if __name__ == '__main__':
   main()