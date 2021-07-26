"""
398. Random Pick Index
Medium

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

"""
import collections
import random
from typing import List
import random

import random
"""
for elements with duplicates, store its index as a list, when asked to pick this number, we pick one index from the list randomly

This one is faster than the reservior sampling/rejection sampling

"""

class Solution0:

    def __init__(self, nums: List[int]):
        self.pos = collections.defaultdict(list)

        for i, num in enumerate(nums):
            self.pos[num].append(i)


    def pick(self, target: int) -> int:
        return self.pos[target][random.randint(0,len(self.pos[target])-1)]

"""
Resevoir sampling

count = 0
nums size is n
for any index i in 0...n, we pick index i with probabliy 1/count if nums[i]==target,
then when the process finishes, all items have been picked with probability 1/n

Note: first item index=0 is always picked, but with 1/2 probability the second item (index=1) will be picked to replace index 0, and index 2 will be picked with probability 1/3 to replace previous result, so on
this method works for picking target num with equal probability from infinitely long stream

mistakes:
1. random.randint(0, n) is inclusiving on both end, i.e., it will pick any number from 0 to n with 1/(n+1) probability
2. we increase count only after we found target == nums[i], i.e., we are counting how many target we have seen in nums so far, then we replace result with the new index with probability 1/count, randint(0, count)==0
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res, count = -1, 0
        for i, num in enumerate(self.nums):
            if target == num:
                count += 1
                if random.randint(1, count) == 1: # starts from randint(0, 0), always pick index 0, 1/2 probability pick index 1, etc
                    res = i

        return res


"""
Reservoir Sampling / Rejection Sampling

pick from all index randomly (uniform distribution), only return if the value is desired target value

choose using the available random distribution, and reject any value out of range (or not equal desired target), only keep the ones within desired range or target, then this sampling is still same distribution (conditional probability)
"""
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        n = len(self.nums)
        index = randint(0, n - 1)
        while self.nums[index] != target:
            index = randint(0, n - 1)

        return index


def main():
    sol = Solution([1,2,3,3,3])
    assert sol.pick(3) in (2,3,4), 'fails'
    assert sol.pick(1) == 0, 'fails'

if __name__ == '__main__':
   main()