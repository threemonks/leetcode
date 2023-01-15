"""
370. Range Addition
Medium
1.5K
76
company
Citadel
company
Amazon
company
Google
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.



Example 1:


Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Example 2:

Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]


Constraints:

1 <= length <= 10^5
0 <= updates.length <= 10^4
0 <= startIdxi <= endIdxi < length
-1000 <= inci <= 1000
"""
# Definition for a binary tree node.
from typing import List


"""
Prefix sum

for query [start, end, delta], we perform this
nums[start] += delta
nums[end+1] -= delta if end+1 is within range

at end, we perform prefix sum
nums[i] += nums[i-1]

time: O(max(length, len(updates))
"""
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0 for _ in range(length)]

        # apply updates at beginning of range, remove updates at right after end of range
        for s, e, d in updates:
            nums[s] += d
            if e+1 < length:
                nums[e+1] -= d

        # now do prefix sum
        for i in range(1, length):
            nums[i] += nums[i-1]

        return nums


def main():
    sol = Solution()
    assert sol.getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]) == [-2,0,3,5,3], 'fails'

    assert sol.getModifiedArray(length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]) == [0,-4,2,2,2,4,4,-4,-4,-4], 'fails'

if __name__ == '__main__':
   main()