"""
1125. Smallest Sufficient Team
Hard

In a project, you have a list of required skills req_skills, and a list of people.  The i-th person people[i] contains a list of skills that person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill.  We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.



Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]


Constraints:

1 <= req_skills.length <= 16
1 <= people.length <= 60
1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
Elements of req_skills and people[i] are (respectively) distinct.
req_skills[i][j], people[i][j][k] are lowercase English letters.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.

"""
import math
from functools import lru_cache
from typing import List

"""
DP 背包 状态压缩 bitmask
"""
"""
observation:

use bitmask to represent a given skill is set or not
dp[i] := minimum number of person required to set skill represented by bitmask i, i.e., i=5 b0101 means skill 2 and skill 0 is set (starting from right)

Time O(N(people) * 2^N(req_skills))
Space O(2^N(req_skills))

"""


class Solution0:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        n = len(req_skills)
        N = (1 << n)  # number of states

        dp = [math.inf for _ in range(N)]
        team = [[] for _ in range(N)]
        dp[0] = 0

        # people_skills is a array of people skillset bitmap
        people_skills = [0 for _ in range(len(people))]
        for idx, skillset in enumerate(people):
            for skill in skillset:
                if skill in req_skills:
                    people_skills[idx] |= 1 << req_skills.index(skill)

        # print('people_skills=%s' % people_skills)

        for skillset in range(N):
            for idx, p in enumerate(people):
                new_skillset = skillset | people_skills[idx]
                # print('i=%s j=%s idx=%s p=%s' % (i, j, idx, str(p)))
                if dp[new_skillset] > dp[skillset] + 1:
                    dp[new_skillset] = dp[skillset] + 1
                    team[new_skillset] = team[skillset] + [idx]
                # print('idx=%s dp=%s team=%s' % (idx, str(dp), str(team)))
            # print('i=%s dp=%s team=%s' % (i, str(dp), str(team)))

        # print('dp=%s team=%s' % (str(dp), str(team)))
        if dp[N - 1] != math.inf:
            return team[N - 1]
        else:
            return []


from functools import lru_cache

"""
DP recursive with memoization
"""


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m, n = len(req_skills), len(people)
        mapping = {v: i for i, v in enumerate(req_skills)}  # skill to its index

        people_skill_masks = [0] * n  # people id to its skill bit masks
        for i, p in enumerate(people):
            for skill in p:
                if skill in mapping:
                    people_skill_masks[i] |= (1 << mapping[skill])  # 0000 0010 | 0000 0001 => 0000 0011

        full_mask = (1 << m) - 1

        @lru_cache(None)
        def dp(masks):
            if masks == full_mask:  # base case
                return []

            ans = [0] * (
                        n + 1)  # default is list of people, and want max, so use [0] * (n+1), similar to math.inf if ans is to look for number of people
            for i, psm in enumerate(people_skill_masks):
                nxt_mask = masks | psm
                if nxt_mask != masks:
                    ans = min(ans, [i] + dp(nxt_mask),
                              key=len)  # if we need number of people, 1+dp(nxt_mask), and would be just min, without define key func, but we are returning actual people list, so we are comparing number of people in the list to return least number of people

            return ans

        return dp(0) # would start from dp(full_mask) if we need to use subsets, then start with full_mask will make it easier to get and use subsets mask

def main():
    sol = Solution()
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    assert sol.smallestSufficientTeam(req_skills, people) == [0, 2], 'fails'

    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    assert sol.smallestSufficientTeam(req_skills, people) == [1, 2], 'fails'

if __name__ == '__main__':
   main()