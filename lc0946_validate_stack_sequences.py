"""
946. Validate Stack Sequences
Medium

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Constraints:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.

"""

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for p in pushed:
            stack.append(p)
            print('stack=%s' % stack)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                print('stack=%s' % stack)
                print('j=%s' % j)

        return not stack and j == len(popped)

def main():
    sol = Solution()
    assert sol.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]) is True, 'fails'

    assert sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]) is False, 'fails'

    assert sol.validateStackSequences([1,0,2], [2,1,0]) is False, 'fails'

if __name__ == '__main__':
   main()