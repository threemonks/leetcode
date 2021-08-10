"""
385. Mini Parser
Medium

308

1017

Add to List

Share
Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.

Each element is either an integer or a list whose elements may also be integers or other lists.



Example 1:

Input: s = "324"
Output: 324
Explanation: You should return a NestedInteger object which contains a single integer 324.
Example 2:

Input: s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789


Constraints:

1 <= s.length <= 5 * 10^4
s consists of digits, square brackets "[]", negative sign '-', and commas ','.
s is the serialization of valid NestedInteger.

"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

"""
Stack

"[123,[456,[789]]]"
 [, => append cur to stack, reset cur, push [ into stack
 ] => close current cur, pop from stack until we meet [, construct NestedInteger from popped items (could be empty list)
-,# => construct number

note:
1. when finish iterating s, there's still content left in cur, which needs to be processed
2. items are added into NestedInteger in reverse order
3. empty brackets pair, just push NestedInteger() into stack

time O(N)
"""


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        cur = ''
        for i, c in enumerate(s):
            if c == '[':
                if cur:
                    stack.append(NestedInteger(value=int(cur)))
                    cur = ''
                stack.append(c)
            elif c == ']':
                items = []
                if cur:
                    stack.append(NestedInteger(value=int(cur)))
                    cur = ''
                while stack[-1] != '[':
                    items.append(stack.pop())
                stack.pop()  # remove [ from stack
                if len(items) >= 1:
                    res = NestedInteger()
                    for item in items[::-1]:
                        res.add(item)
                    stack.append(res)
                else:  # empty bracket pair [], add a NetstedInteger with None value
                    stack.append(NestedInteger())
            elif c == ',':
                if cur:
                    stack.append(NestedInteger(value=int(cur)))
                    cur = ''
            elif c.isdigit() or c == '-':
                cur += c

            # print('i=%s c=%s cur=%s stack=%s' % (i, c, cur, stack))

        # if there's still char in cur, complete it and push it into stack
        if cur:
            stack.append(NestedInteger(value=int(cur)))

        return stack[-1]
