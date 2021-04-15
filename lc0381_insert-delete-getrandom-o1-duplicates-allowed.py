"""
381. Insert Delete GetRandom O(1) - Duplicates allowed
Hard

1118

91

Add to List

Share
Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.


Example 1:

Input
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
Output
[null, true, false, true, 2, true, 1]

Explanation
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // return True. Inserts 1 to the collection. Returns true as the collection did not contain 1.
randomizedCollection.insert(1);   // return False. Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
randomizedCollection.insert(2);   // return True. Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
randomizedCollection.remove(1);   // return True. Removes 1 from the collection, returns true. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equally likely.


Constraints:

-2^31 <= val <= 2^31 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


Follow up: Could you implement the functions of the class with each function works in average O(1) time?

"""
from random import choice

"""
use list and dict {val: [indx list]} to store the value as list, and its index list

always remove last index of a given value.

Note list.remove(x) is not O(1)

time O(1) for insert, remove, and getRandom
"""


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.indices = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.indices:
            self.nums.append(val)
            self.indices[val].append(len(self.nums) - 1)
            return False
        else:
            self.nums.append(val)
            self.indices[val] = [len(self.nums) - 1]
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.indices:
            return False
        else:
            # store index of val to remove, and last val in self.nums to swap and pop
            idx, last = self.indices[val][-1], self.nums[-1]
            # swap last with val
            self.nums[idx] = last
            # update index for last
            self.indices[last].remove(len(self.nums) - 1)  # this is not O(1)
            self.indices[last].append(idx)
            # remove val value in self.nums (swapped out to last already)
            self.nums.pop()
            # remove index of val
            if len(self.indices[val]) == 1:
                del self.indices[val]
            else:
                self.indices[val].pop()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
"""

def main():

    obj = RandomizedCollection()
    obj.insert(1)
    obj.insert(1)
    obj.insert(2)
    obj.getRandom()
    obj.remove(1)
    obj.getRandom()

if __name__ == '__main__':
   main()