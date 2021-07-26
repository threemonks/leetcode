"""
1947. Maximum Compatibility Score Sum
Medium

4

0

Add to List

Share
There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1. The answers of the students are represented by a 2D integer array students where students[i] is an integer array that contains the answers of the ith student (0-indexed). The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array that contains the answers of the jth mentor (0-indexed).

Each student will be assigned to one mentor, and each mentor will have one student assigned to them. The compatibility score of a student-mentor pair is the number of answers that are the same for both the student and the mentor.

For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1], then their compatibility score is 2 because only the second and the third answers are the same.
You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.

Given students and mentors, return the maximum compatibility score sum that can be achieved.



Example 1:

Input: students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
Output: 8
Explanation: We assign students to mentors in the following way:
- student 0 to mentor 2 with a compatibility score of 3.
- student 1 to mentor 0 with a compatibility score of 2.
- student 2 to mentor 1 with a compatibility score of 3.
The compatibility score sum is 3 + 2 + 3 = 8.
Example 2:

Input: students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
Output: 0
Explanation: The compatibility score of any student-mentor pair is 0.


Constraints:

m == students.length == mentors.length
n == students[i].length == mentors[j].length
1 <= m, n <= 8
students[i][k] is either 0 or 1.
mentors[j][k] is either 0 or 1.
"""
from collections import defaultdict
from typing import List

"""
Backtrack / DFS with bitmask

use DFS to pair each student with each mentor, and update the max score can get with this pairing

Note that we can just iterate student one by one, and use bitmask to try all different mentors with this student

mistakes:
1. recrusive dfs does not need to use bitmask for student, only bitmask for mentor, as we can process student one by one from 0 to m-1.
"""
from functools import lru_cache


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        fullmask = (1 << m) - 1

        @lru_cache(None)
        def get_score(i, j):
            return sum([students[i][k] == mentors[j][k] for k in range(n)])

        @lru_cache(None)
        def bt(cur, ment):
            # stud bitmask which student is picked so far
            # ment bitmask which mentor is picked so far
            if cur == m:
                return 0

            # try to turn on one bit in stud, and one bit in ment, and add the result score
            ans = 0
            for j in range(m):
                if (ment >> j) & 1:
                    continue
                # pair i and j, and update score
                newscore = get_score(cur, j)
                ans = max(ans, bt(cur + 1, ment | (1 << j)) + newscore)

            return ans

        res = bt(0, 0)
        bt.cache_clear()
        get_score.cache_clear()

        return res


class Solution1:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        pair_scores = defaultdict(int)
        n = len(students)

        for i in range(n):
            for j in range(n):
                pair_scores[i, j] = sum(ans_i == ans_j for ans_i, ans_j in zip(students[i], mentors[j]))

        @cache
        def dfs(cur, mask):
            if cur == n:
                return 0
            return max(dfs(cur + 1, mask | (1 << j)) + pair_scores[cur, j] for j in range(n) if not mask & (1 << j))

        return dfs(0, 0)

def main():
    sol = Solution()
    assert sol.maxCompatibilitySum(students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]) == 8, 'fails'

    assert sol.maxCompatibilitySum(students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]) == 0, 'fails'


if __name__ == '__main__':
   main()