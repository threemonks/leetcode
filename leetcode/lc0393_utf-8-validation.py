"""
393. UTF-8 Validation
Medium

314

1344

Add to List

Share
Given an integer array data representing the data, return whether it is a valid UTF-8 encoding.

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.



Example 1:

Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.


Constraints:

1 <= data.length <= 2 * 10^4
0 <= data[i] <= 255
"""
from typing import List

"""
Bit Manipulation

0xxxx => single bytes
110xxxx 10x
1110xxx 10x 10x
11110xx 10x 10x 10x
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        expecting_bytes = 0
        for num in data:
            num = (num & 255)
            if not num & (1 << 7):  # start with 0
                if expecting_bytes != 0:
                    # print('expecting bytes before single byte')
                    return False
            elif num & (1 << 7) and not (num & (1 << 6)):  # continuing bytes
                expecting_bytes -= 1
                if expecting_bytes < 0:
                    # print('expecting bytes negative before continuing')
                    return False
            else:  # non-continuing
                if expecting_bytes != 0:
                    # print('expecting bytes before non-continuing byte')
                    return False
                if num & (1 << 7) and num & (1 << 6) and not (num & (1 << 5)):  # 110xxxxx 2 byte
                    expecting_bytes = 1
                elif num & (1 << 7) and num & (1 << 6) and num & (1 << 5) and not num & (1 << 4):  # 1110xxxx 3 byte
                    expecting_bytes = 2
                elif num & (1 << 7) and num & (1 << 6) and num & (1 << 5) and num & (1 << 4) and not num & (
                        1 << 3):  # 11110xxx 4 byte
                    expecting_bytes = 3
                else:  # max four bytes
                    # print('invalid start of non-continuing')
                    return False

        # print('expecting_bytes=%s' % expecting_bytes)
        return expecting_bytes == 0


def main():
    sol = Solution()
    assert sol.validUtf8(data = [197,130,1]) == True, 'fails'

    assert sol.validUtf8(data = [235,140,4]) == False, 'fails'

if __name__ == '__main__':
   main()