"""
1434. Number of Ways to Wear Different Hats to Each Other
Hard

There are n people and 40 types of hats labeled from 1 to 40.

Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the conditions.
First person choose hat 3, Second person choose hat 4 and last one hat 5.
Example 2:

Input: hats = [[3,5,1],[3,5]]
Output: 4
Explanation: There are 4 ways to choose hats
(3,5), (5,3), (1,3) and (1,5)
Example 3:

Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Output: 24
Explanation: Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.
Example 4:

Input: hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
Output: 111


Constraints:

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] contains a list of unique integers.

"""
import collections
import math
from functools import lru_cache
from typing import List

"""
dp 背包 状态压缩
基本方法是循环所有物品，然后循环所有状态，每个状态表示每个物品选择放还是不放

dp[hat_state] := number of ways to wear different hats given a bitmask (hats used)

for p in persons: # n<10
    dp_new = dp # save dp as we need a new start when we check another person, if we don't use dp_new for each loop for a new person, then we would need a 2-d dp[hat_state][person]
    for state in states [00000, ..., 111111]: # each bit represents a hat i being used
        for hat for hats_for_this_person[p]:
            if hat has been taken in state:
                continue
            new_state = state + hat # bit and
            dp_new[new_state] += dp[state]
    dp = dp_new

return sum(dp[state] for all state with 10 1 bits)

since there's 40 hats, hat state would be 2^40 for hat, this is too large for 32 bit integer as bitmask, so we consider use bitmask for person choice state, and loop through hats in outside loop

dp[state] := number of ways to wear different hats given a bitmask for number of person checked
for hat in hats: # n < 40
    dp_new = dp 
    for state in states (0, ..., 1111111111): # each bit represents a person i being checked
        for person in person_for_this_hat[hat]:
            if this person already has hat in state:
                continue
            new_state = state + person # bit and
            dp_new[new_state] += dp[state]
    dp = dp_new            

return dp[1111111111]

"""
class Solution0:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        N = (1<<n)
        M = 10**9+7
        # construct persons_for_hat from hats
        persons_for_hat = {}
        for idx, hat_list in enumerate(hats):
            for hat in hat_list:
                if hat in persons_for_hat:
                    persons_for_hat[hat].append(idx)
                else:
                    persons_for_hat[hat] = [idx]

        dp = [0 for _ in range(N)]
        dp[0] = 1

        for hat in range(1, 41): # total 40 hats
            dp_new = dp[:]
            for state in range(N): # each bit represents a person i being checked
                if hat not in persons_for_hat:
                    continue
                for person in persons_for_hat[hat]:
                    if ((state>>person)&1) == 1:
                        continue
                    new_state = state + (1<<person) # bit and
                    dp_new[new_state] += dp[state]
                    dp_new[new_state] %= M
            dp = dp_new

        return dp[N-1]


"""
dp bitmask with recursion

we could iterate all persons, and use bitmask represents which hat this person wears, check under each state (this person wear certain hat), how does it impact other user's choice, then the number of states is 2^40, which is too big

alternatively, we can iterate all hats, and use bitmask to represents which person this hat is assigned to, and check under each state, how later hats can assign (cannot assign to person who already has hat), the number of states is 2^10
"""


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        MOD = 10 ** 9 + 7

        h2p = collections.defaultdict(list)  # each member list are the persons that would wear this hat (hat number as key)
        for i in range(n):
            for h in hats[i]:
                h2p[h].append(i)

        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dp(i, mask):
            if mask == full_mask:  # base case, all persons have hat
                return 1
            if i == 41:  # all hats have been tried, but found no valid distribution, so this path contributes 0 type of ways to wear
                return 0

            ans = dp(i + 1, mask)  # hat is not assigned to a person
            for p in h2p[i]:  # check all person that prefers this hat
                if mask & (1 << p) == 0:  # if this person does not have a hat yet
                    ans += dp(i + 1, mask | (
                                1 << p))  # possible solution, check next hat to see if it can form a valid distribution

            return ans % MOD

        return dp(0, 0)


def main():
    sol = Solution()
    assert sol.numberWays([[3,4],[4,5],[5]]) == 1, 'fails'

    assert sol.numberWays([[3,5,1],[3,5]]) == 4, 'fails'

    assert sol.numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]) == 24, 'fails'

    assert sol.numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]) == 111, 'fails'

if __name__ == '__main__':
   main()