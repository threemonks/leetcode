"""
https://leetcode.com/discuss/interview-question/1379050/Amazon-OA-July-2021

Kindle Direct Publishing, Amazon's e-book selfpublishing platform, is working on a new feature to help authors use
special text characters in different ways. They have asked for your help in beta testing a new part of the feature involving
round and square brackets. Given a string that consists of characters (, ), [, ) and ?, determine how many ways it can be split
into two non-empty substrings such that the characters in each substring can be rearranged into a balanced string.
A sequence of round and square brackets can be rearranged into a balanced sequence if and only if the number of opened and closed
bracket is equal for both types of the brackets. The question marks can take the place of any needed character,
and the substrings together must contain the entire string.

Note: A substring is a contiguous group of characters in a string.
Sample Case 1
Sample Input For Custom Testing
STDIN
Function
– – – – –
(((?

s = '(((?'
Sample Output
Explanation s = (((?
There are 3 splits into two non-empty substrings:
(and (? 2.(( and (? 3.((( and ?
None has two balanced substrings.

"""

import collections


def findPair(a):
    res=0
    freq=collections.Counter(a)
    if abs(freq["("]-freq[")"])+abs(freq["["]-freq["]"])>freq["?"]:
        return None

    countRound,countSquare,countQuestion=0,0,0
    for c in a:
        if c=="(":
            countRound+=1
        elif c==")":
            countRound-=1
        elif c=="[":
            countSquare+=1
        elif c=="]":
            countSquare-=1
        elif c=="?":
            countQuestion+=1

        if abs(countRound) + abs(countSquare) <= countQuestion:
            # left is correct
            res+=1

    return res-1

def main():

    assert findPair(a="(()())(()[][))(?)(") == 5, 'fails'

    assert findPair(a="(((?") == -1, 'fails'

if __name__ == '__main__':
    main()
