"""
1429. First Unique Number
Medium

278

13

Add to List

Share
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.


Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
Example 2:

Input:
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
[null,-1,null,null,null,null,null,17]
Explanation:
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17
Example 3:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output:
[null,809,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
"""
from typing import List

"""
Design

use a deque to hold unique ones, but do lazy remove from deque when check for showFirstUnique
use dict to hold counts

to achieve O(1) for showFirstUnique, we can use DoublyLinkedList to store nodes as they arrive, but then the counts dict would hold both a count of the node, as well as pointer to the actual LinkedList node. so whenever we add a value causing it to be not unique anymore, we remove it from the doublylinked list.

note:
1. check for empty nums
2. when populating counts, note input nums could have duplicates

time: O(1) for add
      amortized O(1) for showFirstUnique
"""
from collections import deque, defaultdict


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = deque()
        self.counts = defaultdict(int)
        for num in nums:
            self.nums.append(num)
            self.counts[num] += 1

    def showFirstUnique(self) -> int:
        while self.counts and self.nums and self.counts[self.nums[0]] > 1:
            self.nums.popleft()

        if self.nums:
            return self.nums[0]
        else:
            return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.counts:
            self.counts[value] += 1
        else:
            self.counts[value] = 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
