"""
1381. Design a Stack With Increment Operation
Medium

564

48

Add to List

Share
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.


Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.


Constraints:

1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.

"""
"""
Design

use list to implement stack

mistakes:
1. k could be larger than len(self.nums)
"""


class CustomStack0:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.nums = []

    def push(self, x: int) -> None:
        if len(self.nums) < self.maxSize:
            self.nums.append(x)

    def pop(self) -> int:
        if self.nums:
            return self.nums.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.nums))):
            self.nums[i] += val


"""
Design

use inc array to record increments to be done for nums[0...i] in increment[i]
at each pop, we pop both nums and inc, return the sum of popped value from nums and inc
after this, we need to add inc[-1] into its previous element, so that this inc[-1] logic is applied all remaining elements after this pop.

time O(1) for all operations
mistakes1:
1. increment could be on top of previous inc value
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.nums = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.nums) < self.maxSize:
            self.nums.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.inc:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[
                -1]  # keep this inc_val application to all remaining elements before this popped index
        return self.nums.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(
                self.inc)) - 1] += val  # apply add value val to min(k, len(self.nums)), could be in addition to previous inc change


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

def main():
    obj = CustomStack(3)

    obj.push(1)
    obj.push(2)
    assert obj.pop() == 2, 'fails'
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.increment(5, 100)
    obj.increment(2, 100)
    assert obj.pop() == 103, 'fails'
    assert obj.pop() == 202, 'fails'
    assert obj.pop() == 201, 'fails'
    assert obj.pop() == -1, 'fails' # empty


if __name__ == '__main__':
   main()