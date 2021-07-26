"""
1774. Closest Dessert Cost
Medium

You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:

There must be exactly one ice cream base.
You can add one or more types of topping or have no toppings at all.
There are at most two of each type of topping.
You are given three inputs:

baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
target, an integer representing your target price for dessert.
You want to make a dessert with a total cost as close to target as possible.

Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.



Example 1:

Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
Output: 10
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.
Example 2:

Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
Output: 17
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 3
- Take 1 of topping 0: cost 1 x 4 = 4
- Take 2 of topping 1: cost 2 x 5 = 10
- Take 0 of topping 2: cost 0 x 100 = 0
Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.
Example 3:

Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
Output: 8
Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.
Example 4:

Input: baseCosts = [10], toppingCosts = [1], target = 1
Output: 10
Explanation: Notice that you don't have to have any toppings, but you must have exactly one base.


Constraints:

n == baseCosts.length
m == toppingCosts.length
1 <= n, m <= 10
1 <= baseCosts[i], toppingCosts[i] <= 104
1 <= target <= 104

"""
from typing import List

"""

Greedy

notes:
1. iterate base cost outside of helper function improves performance
2. sort base and topping costs, so that we can early prune, as soon as the diff between current cost and target is larger than best diff we have so far

time: O(M*3^N) M - number of bases, N - # of toppings
"""


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # sort so that we can early prune
        baseCosts = sorted(baseCosts)
        toppingCosts = sorted(toppingCosts)
        n, m = len(baseCosts), len(toppingCosts)

        best = baseCosts[0]  # require one base
        min_diff = abs(target - best)

        def backtrack(basecost, toppings):
            nonlocal min_diff, target, best
            # base case
            if len(toppings) > m:
                return

            cost = basecost
            for i, tc in enumerate(toppings):
                cost += toppingCosts[i] * tc

            if abs(cost - target) < min_diff or (abs(cost - target) == min_diff and cost < best):
                min_diff = abs(cost - target)
                best = cost

            # early pruning
            if cost - target > min_diff:
                return

            # try same base different toppings
            backtrack(basecost, toppings + [0])
            backtrack(basecost, toppings + [1])
            backtrack(basecost, toppings + [2])

        for basecost in baseCosts:
            backtrack(basecost, [])  # [] is topping count for corresponding index

        return best


def main():
    sol = Solution()
    assert sol.closestCost(baseCosts = [1,7], toppingCosts = [3,4], target = 10) == 10, 'fails'

    assert sol.closestCost(baseCosts = [2,3], toppingCosts = [4,5,100], target = 18) == 17, 'fails'

    assert sol.closestCost(baseCosts = [3,10], toppingCosts = [2,5], target = 9) == 8, 'fails'

    assert sol.closestCost(baseCosts = [10], toppingCosts = [1], target = 1) == 10, 'fails'



if __name__ == '__main__':
   main()