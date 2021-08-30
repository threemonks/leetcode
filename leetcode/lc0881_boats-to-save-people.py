"""
881. Boats to Save People
Medium

1488

51

Add to List

Share
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.



Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)


Constraints:

1 <= people.length <= 5 * 10^4
1 <= people[i] <= limit <= 3 * 10^4
"""
from typing import List

"""
Greedy / Two Pointers

sort people, since each boat can at most take two person, if we sort people, use two pointers (left, right) to track each end, if we add people[right] (heaviest one), then either we can add people[left] (lightest one remaining), or we can only fit people[right], and then need to start a new boat (since even the lightest one cannot be added to the boat with people[right])

time O(NlogN)
space O(N)
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n = len(people)

        ans = 0
        i, j = 0, n - 1
        while i <= j:
            if people[j] + people[i] <= limit:
                ans += 1
                i += 1
                j -= 1
            else:  # only people[j] can fit on this boat
                ans += 1
                j -= 1

        return ans


def main():
    sol = Solution()
    assert sol.numRescueBoats(people = [1,2], limit = 3) == 1, 'fails'

    assert sol.numRescueBoats(people = [3,2,2,1], limit = 3) == 3, 'fails'

    assert sol.numRescueBoats(people = [3,5,3,4], limit = 5) == 4, 'fails'

if __name__ == '__main__':
   main()