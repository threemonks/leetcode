"""
1229. Meeting Scheduler
Medium

"""
from typing import List

"""
Two Pointers

similar to 986, take one interval from each person, get their intersection,  if it is > duration, it is valid, if not, move forward with whoever end point is sooner

time: O(M+N)
space: O(1)

mistakes:
1. only need to return interval of length duration (even though the two person's schedule intersection is likely > duration)
2. interval [1,1] is of length 1
"""


class Solution:
    def minAvailableDuration(self, A: List[List[int]], B: List[List[int]], duration: int) -> List[int]:
        A, B = sorted(A), sorted(B)  # sort A and B by start time
        m, n = len(A), len(B)

        i, j = 0, 0
        while i < m and j < n:
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if start <= end and end >= start + duration:
                return [start, start + duration]

            # now skip the list with smaller end pointer
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return []


def main():
    sol = Solution()
    assert sol.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8) == [60,68], 'fails'

    assert sol.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12) == [], 'fails'


if __name__ == '__main__':
   main()