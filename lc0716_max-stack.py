"""
716. Max Stack
Easy

1051

275

Add to List

Share
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.


Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.


Constraints:

-10^7 <= x <= 10^7
At most 104 calls will be made to push, pop, top, peekMax, and popMax.
There will be at least one element in the stack when pop, top, peekMax, or popMax is called.


Follow up: Could you come up with a solution that supports O(1) for each top call and O(logn) for each other call?
"""
import math

"""
Stack

observation:
use two stacks, first stack is the elements as usual, second stack is max element up to this index
for peekMax, it is just self[-1][1]
for popMax, we get current max via peekMax, then pop until we find the maximum in self[i][0], then push popped element back onto the stack.

time O(N)
space O(N)
"""


class MaxStack0(list):

    def push(self, x: int) -> None:
        m = max(x, self[-1][1] if self else -math.inf)
        self.append((x, m))

    def pop(self) -> int:
        return list.pop(self)[0]

    def top(self) -> int:
        return self[-1][0]

    def peekMax(self) -> int:
        if self:
            return self[-1][1]
        else:
            return None

    def popMax(self) -> int:
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        for item in reversed(b):
            self.push(item)

        return m


"""
LinkedList + SortedDict - sorted dict to keep track of max value index (node)

store stack as double linked list, store a map of value to list of node for given value

time: O(log(N)) for all except for peek, which is O(1)
space: O(N)
"""
from sortedcontainers import SortedDict


class Node:
    def __init__(self, val: int = 0, prev: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next


class MaxStack():
    def __init__(self, *args, **kwargs):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.maps = SortedDict()

    def push(self, x: int) -> None:
        # insert in front of tail
        node = Node(x, prev=self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail

        # update maps
        if x in self.maps:
            self.maps[x].append(node)
        else:
            self.maps[x] = [node]

    def pop(self) -> int:
        # remove self.tail.prev
        node = self.tail.prev
        node_prev = node.prev
        node_prev.next = self.tail
        self.tail.prev = node_prev

        # remove this node from maps as well
        nodes = self.maps[node.val]
        del nodes[-1]  # del last element from nodes1 O(1)
        if len(nodes) == 0:  # remove key if it has empty list
            del self.maps[node.val]

        return node.val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        key, nodes = self.maps.peekitem(-1)
        return key

    def popMax(self) -> int:
        # remove max value node, which is last element in the list associated with last (max) key in maps
        key, nodes = self.maps.peekitem(-1)
        node = nodes[-1]
        del nodes[-1]  # use del nodes[-1] to remove last element in nodes at O(1)
        if len(nodes) == 0:  # remove key if it has empty list
            del self.maps[node.val]

        # remove node from double linked list
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev

        return key


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


def main():

    obj = MaxStack()
    obj.push(5) #  // [5] the top of the stack and the maximum number is 5.
    obj.push(1) #   // [5, 1] the top of the stack is 1, but the maximum is 5.
    obj.push(5) #   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
    obj.top() #     // return 5, [5, 1, 5] the stack did not change.
    obj.popMax() #  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
    obj.top() #      // return 1, [5, 1] the stack did not change.
    obj.peekMax() # // return 5, [5, 1] the stack did not change.
    obj.pop() #     // return 1, [5] the top of the stack and the max element is now 5.
    obj.top() #     // return 5, [5] the stack did not change.

    obj = MaxStack()
    obj.push(5) #  // [5] the top of the stack and the maximum number is 5.
    obj.push(1) #   // [5, 1] the top of the stack is 1, but the maximum is 5.
    obj.popMax() #  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
    obj.peekMax() # // return 5, [5, 1] the stack did not change.


if __name__ == '__main__':
   main()