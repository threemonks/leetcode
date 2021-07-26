"""
332. Reconstruct Itinerary
Medium

2925

1331

Add to List

Share
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.


Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""
from typing import List

"""
Backtrack / DFS modified

mistakes:
1. 'JFK' is the start
2. all edges (tickets) must be used once and only once, so we keep track of used[orig][i] (where i is index of dest within the dest lists of this orig), not seen(nodes)
3. same city could appear multiple times in same route due to ticket could connect same city to different city
   so we cannot used seen to track vertices, instead, we need to track each ticket self.used[orig][i] (i is index of dest within the list of dests of this orig) to make sure it is used once and exactly once
4. need to return True as soon as we have a valid path of length self.flgihts+1, and propagate this True back to stop further DFS into other paths.

"""

from collections import defaultdict, deque


class Solution0:
    def visit(self, node, path):
        # print('visiting node=%s path=%s' % (node, path))
        if len(path) == self.flights + 1:
            self.route = path[:]
            return True  # return True so we can propagate back to stop further DFS traverse other route, since we already got a valid route
        for i, nxt in enumerate(self.adj_list[node]):
            if not self.used[node][i]:
                # mark this ticket as used before next recursion
                self.used[node][i] = True
                ret = self.visit(nxt, path + [nxt])
                # unmark this ticket as unused when we backtrack (we are trying a different route now)
                self.used[node][i] = False
                if ret:  # first valid path found should be lowest in lexcical order, so do not process further
                    return True

        return False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flights = len(tickets)

        self.adj_list = defaultdict(list)
        self.used = defaultdict(list)

        for a, b in sorted(tickets):
            self.adj_list[a].append(b)

        # sort adjacency list on lexical order
        # note we could have multiple identical flights, i.e., same origin and destination
        # so we keep track of each of such ticket used using dict of list (destinations)
        for k in self.adj_list.keys():
            self.adj_list[k].sort()  # sort so we travel possible destination from this origin in lexical order
            self.used[k] = [False] * len(self.adj_list[k])

            # print(self.adj_list)
        self.route = []
        self.visit('JFK', ['JFK'])

        return self.route


"""
DFS traverse all edges once and exactly once
"""


class Solution:
    def visit(self, node):
        while self.adj_list[node]:
            # remove this node (edge) so we visit the edge exactly once
            self.visit(self.adj_list[node].pop(
                0))  # maybe we can store adj_list[node] reversed so we can just pop() which is quicker
        # no more destination to go, last airport, add
        self.route.insert(0, node)  # could use append, and do reverse at final result

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flights = len(tickets)

        self.adj_list = defaultdict(list)

        for a, b in sorted(tickets):
            self.adj_list[a].append(b)
            self.adj_list[a].sort()  # sort so we travel possible destination from this origin in lexical order

        # print(self.adj_list)
        self.route = []
        self.visit('JFK')

        return self.route


def main():
    sol = Solution()
    assert sol.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) == ["JFK","MUC","LHR","SFO","SJC"], 'fails'

    assert sol.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"], 'fails'


if __name__ == '__main__':
   main()
