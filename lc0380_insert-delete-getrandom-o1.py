"""
380. Insert Delete GetRandom O(1)
Medium

3503

207

Add to List

Share
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.


Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-2^31 <= val <= 2^31 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


Follow up: Could you implement the functions of the class with each function works in average O(1) time?

"""
"""
python dict/set would give O(1) for insert and remove, but not getRandom.

So we would use a list to and store list index into dict, this will allow us still insert in O(1) into dict, append to list is also O(1)
and we can swap and remove from end of list, which is also O(1)

With dict storing {val: index}, getRandom can use random.choice(list), which is also O(1)
"""

import random

"""
python dict/set would give O(1) for insert and remove, but not getRandom.

So we would use a list to and store list index into dict, this will allow us still insert in O(1) into dict, append to list is also O(1)
and we can swap and remove from end of list, which is also O(1)

With dict storing {val: index}, getRandom can use random.choice(list), which is also O(1)
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.indices = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indices:
            return False
        else:
            self.nums.append(val)
            self.indices[val] = len(self.nums) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.indices:
            # get hold of index of val, and last value in self.nums (to swap and pop last)
            idx, last = self.indices[val], self.nums[-1]
            # store last value into position idx
            self.nums[idx] = last
            # update index for value last
            self.indices[last] = idx
            # remove last value (val) from list
            self.nums.pop()
            # remove index of val
            del self.indices[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)


"""
python set, and O(N) time to getRandom()
"""

class RandomizedSet1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.nums:
            return False
        else:
            self.nums.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.nums:
            self.nums.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return list(self.nums)[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def main():

    obj = RandomizedSet()
    obj.insert(1)
    obj.remove(2)
    obj.insert(2)
    obj.getRandom()
    obj.remove(1)
    obj.insert(2)
    obj.getRandom()

if __name__ == '__main__':
   main()