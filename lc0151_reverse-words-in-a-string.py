"""
151. Reverse Words in a String
Medium

1796

3335

Add to List

Share
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"


Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        curword = ''
        for c in s:
            if c == ' ':
                if curword:
                    words.append(curword)
                    curword = ''
            else:
                curword += c

        if curword:
            words.append(curword)

        return ' '.join(words[::-1])


def main():
    sol = Solution()
    assert sol.reverseWords(s = "the sky is blue") == "blue is sky the", 'fails'

    assert sol.reverseWords(s = "  hello world  ") == "world hello", 'fails'

    assert sol.reverseWords(s = "a good   example") == "example good a", 'fails'

    assert sol.reverseWords(s = "  Bob    Loves  Alice   ") == "Alice Loves Bob", 'fails'

    assert sol.reverseWords(s = "Alice does not even like bob") == "bob like even not does Alice", 'fails'

if __name__ == '__main__':
   main()
