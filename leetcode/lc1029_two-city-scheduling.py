"""
1029. Two City Scheduling
Medium

1977

205

Add to List

Share
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.



Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086


Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000
"""
from typing import List

"""
Greedy

calculate diff of each pair, sort diffs, half diff will have positive sign, half have negative sign, to minimize total sum of pair diffs with these sign assignment
steps:
1. sort pair diffs,
2. smaller half get positive sign (picking second element in costs)
3. large half have negative sign (picking first element in costs)

"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        diffs = []
        for i in range(n):
            diffs.append((costs[i][1] - costs[i][0], i))

        diffs = sorted(diffs)

        # smaller half of diffs have positive sign, means we pick second element in costs
        # large half of diffs have negative sign, means we pick first element in costs

        ans = 0
        for i in range(n // 2):
            ans += costs[diffs[i][1]][1]

        for i in range(n // 2, n):
            ans += costs[diffs[i][1]][0]

        return ans


def main():
    sol = Solution()

    assert sol.twoCitySchedCost(costs = [[10,20],[30,200],[400,50],[30,20]]) == 110, 'fails'

    assert sol.twoCitySchedCost(costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]) == 1859, 'fails'

    assert sol.twoCitySchedCost(costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]) == 3086, 'fails'

if __name__ == '__main__':
   main()

