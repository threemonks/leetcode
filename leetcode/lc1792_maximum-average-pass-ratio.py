"""
1792. Maximum Average Pass Ratio
Medium

"""
import heapq
import math
from typing import List

"""
Greedy / MinHeap

greedy with minheap, keeping track of pass ratio change when adding one extra student
each time add one extra student to the class with biggest percentage improvement

mistakes1:
1. was trying to consider each different assignment of extra student to different class as different case, that is N!, not possible
2. greedy needs a better way to define improvement therefore the best result in greedy, i.e., pass ratio improvement is the criteria for greedy

"""


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = [(-((p + 1) / (t + 1) - p / t), p, t) for p, t in classes]
        heapq.heapify(q)

        while extraStudents:
            v, p, t = heapq.heappop(q)  # take the one would have biggest ratio improvement
            p += 1
            t += 1
            heapq.heappush(q, (-((p + 1) / (t + 1) - p / t), p, t))  # add back this updated class
            extraStudents -= 1

        # now calculate best average pass ratio
        ratios = []
        while q:
            v, p, t = heapq.heappop(q)
            ratios.append(p / t)

        return sum(ratios) / len(ratios)

def main():
    sol = Solution()
    assert math.isclose(sol.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2), 0.78333, abs_tol=0.00002), 'fails'

    assert math.isclose(sol.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4), 0.53485, abs_tol=0.00002), 'fails'


if __name__ == '__main__':
   main()