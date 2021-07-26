"""
128. Longest Consecutive Sequence
Hard

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109


Follow up: Could you implement the O(n) solution?

"""
from typing import List

"""
consider consecutive elements sequence as an island (disjoint set union find)
Note 1 we store index of nums into the dsu, and use a hashmap to store number to index, so that we can easily find if a new number num should be unioned with an known number or not (if num+1 or num-1 exists in the hashmap)
     2 we use union by size, so that we can easily find the largest group
"""


class DSUBySize:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.size[xp] > self.size[yp]:
                self.parent[yp] = xp
                self.size[xp] += self.size[yp]
            else:
                self.parent[xp] = yp
                self.size[yp] += self.size[xp]


class Solution0:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dsu = DSUBySize(n)

        seen = dict()

        for i in range(n):
            if nums[i] in seen:
                continue
            seen[nums[i]] = i
            if nums[i] - 1 in seen:
                dsu.union(i, seen[nums[i] - 1])
            if nums[i] + 1 in seen:
                dsu.union(i, seen[nums[i] + 1])

        return max(dsu.size)


"""
sort and count consecutive sequence
time O(n*log(n))
"""


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)

        nums = sorted(nums)

        res = 0
        count = 1  # element of current sequence
        for i in range(n):
            if i - 1 >= 0:
                if nums[i] > nums[i - 1] + 1:  # reset sequence
                    count = 1
                elif nums[i] == nums[i - 1] + 1:
                    count += 1
            res = max(res, count)

        return res


"""
convert list to hashset, for each number num in current group we are exploring/counting, check if its next sequential number (num+1) is in hashset, if so, inrease current sequence length by 1
time O(n+n) = O(n) - the while loop only works once for full length at most, so it is O(n+n)=O(n)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numset = set(nums)

        global_streak = 0

        for num in numset:
            if num - 1 not in numset:  # if preceding sequential number does not exist, start new streak
                current_num = num
                current_streak = 1

                while current_num + 1 in numset:  # find the entire streak
                    current_num += 1
                    current_streak += 1

                global_streak = max(global_streak, current_streak)

        return global_streak

def main():
    sol = Solution()
    assert sol.longestConsecutive([100,4,200,1,3,2]) == 4, 'fails'

    assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9, 'fails'


if __name__ == '__main__':
   main()