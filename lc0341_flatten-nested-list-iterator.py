"""
341. Flatten Nested List Iterator
Medium

2109

800

Add to List

Share
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.


Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10^6, 10^6].
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> ['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
from collections import deque

"""
Recursive

"""


class NestedIterator0:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = deque()

        def get_int(nested_integer):
            if nested_integer.isInteger():
                return [nested_integer.getInteger()]
            else:
                ans = []
                for ni in nested_integer.getList():
                    for i in get_int(ni):
                        ans.append(i)

                return ans

        for ni in nestedList:
            for i in get_int(ni):
                self.nums.append(i)

    def next(self) -> int:
        return self.nums.popleft()

    def hasNext(self) -> bool:
        return len(self.nums) > 0


"""
Stack
"""


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = deque()

        stack = []

        for ni in nestedList[::-1]:
            stack.append(ni)

        while stack:
            nested_integer = stack.pop()
            if nested_integer.isInteger():
                self.nums.append(nested_integer.getInteger())
            else:
                for ni in nested_integer.getList()[::-1]:
                    stack.append(ni)

    def next(self) -> int:
        return self.nums.popleft()

    def hasNext(self) -> bool:
        return len(self.nums) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
