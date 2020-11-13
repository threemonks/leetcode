"""
1125. Smallest Sufficient Team
Hard

413

9

Add to List

Share
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

"""


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        n = len(req_skills)
        N = (1 << n)  # number of states

        dp = [math.inf for _ in range(N)]
        team = [[] for _ in range(N)]
        dp[0] = 0

        def get_new_state(req_skills, i, p):
            """
            given  people p skill sets, current state i, return the new state j
            """
            n = len(req_skills)
            for sk in p:
                for k in range(n):
                    if (i & (1 << k) == 0) and sk == req_skills[k]:
                        i += (1 << k)
                        break
            return i

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