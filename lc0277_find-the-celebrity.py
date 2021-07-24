"""
277. Find the Celebrity
Medium

1693

170

Add to List

Share
Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.



Example 1:


Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.


Constraints:

n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1


Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?

"""
# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

"""
Brutal Force

build graph using know(a, b)
find vertex with outdegree=0 and indegree=n-1

time O(N^2)

TLE

mistakes:
1. no need to build graph (adj_list), just need to count indegree/outdegree
"""


class Solution0:
    def findCelebrity(self, n: int) -> int:
        indegree = [0 for _ in range(n)]
        outdegree = [0 for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if knows(i, j):
                    outdegree[i] += 1
                    indegree[j] += 1
                if knows(j, i):
                    outdegree[j] += 1
                    indegree[i] += 1

        for i in range(n):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i

        return -1


"""
Greedy

knows(i, j) == True => i is not celebrity
knows(i, j) == False => j is not celebrity

so in each call, we can eliminate at least one potential candidate as celebrity.
1. pick any initial celebrity candidate, scan through entire list, each step eliminate one candidate
2. after we finish the array scan, we have one celebrity candidate left, we then scan entire array again to see if all other person knows this candidate

mistakes:
1. test case [[0, 1], [1, 0]] means person 
"""


class Solution:
    def findCelebrity(self, n: int) -> int:

        cand = 0  # potential celebrity
        for i in range(n):
            if knows(cand, i):  # cand is not celebrity because i does not know cand
                cand = i

        # now cand == n-1, check if it is celebrity
        for i in range(n):
            if (i != cand and knows(cand, i)) or not knows(i, cand):
                return -1

        return cand