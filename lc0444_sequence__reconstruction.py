"""
444. Sequence Reconstruction
Medium

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.



Example 1:

Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true


Constraints:

1 <= n <= 10^4
org is a permutation of {1,2,...,n}.
1 <= segs[i].length <= 10^5
seqs[i][j] fits in a 32-bit signed integer.


UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.
"""
from typing import List

"""
basic idea is to do topological sort of seqs, and if the sort result equals to org, and there's only one way to sort, then we return True. otherwise return False.

If len(adj_list) != len(org): return False # cannot uniquely reconstruct

sources = all nodes with indegrees=0

if sources > 1 at any point, that means we have at least two different way to topologically sort, so it is not unique

BFW sort of seqs
"""
import collections

"""
basic idea is to do topological sort of seqs, and if the sort result equals to org, and there's only one way to sort, then we return True. otherwise return False.

if any number in seq < 1 or > n, that means it is out of range of org.

sources = all nodes with indegrees=0

if sources > 1 at any point, that means we have at least two different way to topologically sort, so it is not unique

and the topological sort output must be the same as org, that would means unique topological sort output, and same as org

BFS sort of seqs
"""
import collections


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        n = len(org)
        adj_list = collections.defaultdict(list)  # # adjacency list of graph
        indegrees = collections.defaultdict(int)  # count of incoming edges

        # a. build the graph
        for seq in seqs:
            for i in range(len(seq) - 1):
                if seq[i] < 1 or seq[i + 1] < 1 or seq[i] > n or seq[i + 1] > n:
                    return False
                adj_list[seq[i]].append(seq[i + 1])
                indegrees[seq[i + 1]] += 1  # first one in seq has no income edge from this seq
        # print('adj_list=%s' % adj_list)
        # print('indegrees=%s' % indegrees)

        # find all sources (nodes with indegree=0)
        sources = collections.deque()
        for seq in seqs:
            for num in seq:
                if indegrees[num] == 0 and num not in sources:
                    sources.append(num)
        # print('sources=%s' % sources)

        sorted_list = []
        while sources:
            if len(sources) > 1:  # more than one way to start the topological sort, not unique
                # print('len(sources)>1: %s' % sources)
                return False
            vertex = sources.popleft()
            sorted_list.append(vertex)
            if vertex in adj_list:
                for child in adj_list[vertex]:
                    indegrees[child] -= 1
                    if indegrees[child] == 0:
                        sources.append(child)

        # print(sorted_list)
        return sorted_list == org


def main():
    sol = Solution()
    assert sol.sequenceReconstruction([1,2,3], [[1,2],[1,3]]) is False, 'fails'

    assert sol.sequenceReconstruction([1,2,3], [[1,2]]) is False, 'fails'

    assert sol.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]]) is True, 'fails'

    assert sol.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]) is True, 'fails'

if __name__ == '__main__':
   main()