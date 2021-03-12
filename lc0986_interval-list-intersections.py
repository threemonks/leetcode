"""
986. Interval List Intersections
Medium

"""
from typing import List

"""
Interval / Sweep line

workflow:
1. iterate both intervals while there are still left
2. if there are overlap iv1[0] <= iv2[0] <= iv1[1] or iv2[0] <= iv1[0] <= iv2[1], add intersect to result
   and increase index on the shorter one (iv1[1] < iv2[1] or iv2[1] < iv1[1]), or both if the two intervals ends at same number
3. if there's no overlap, skip the one that's to left
4. repeat 2 and 3

time O(M+N)
space O(M+N)
"""


class Solution0:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        result = []

        l1, l2 = len(firstList), len(secondList)
        idx1, idx2 = 0, 0
        while idx1 < l1 and idx2 < l2:
            interval1 = firstList[idx1]
            interval2 = secondList[idx2]
            # there's overlap
            if interval1[0] <= interval2[0] <= interval1[1] or interval2[0] <= interval1[0] <= interval2[1]:
                # add intersection to result
                result.append((max(interval1[0], interval2[0]), min(interval1[1], interval2[1])))
                if interval1[1] < interval2[1]:  # interval1 is smaller, used up, move its index to right
                    idx1 += 1
                elif interval1[1] > interval2[1]:  # interval2 is smaller, used up, move its index to right
                    idx2 += 1
                else:  # interval1[1] == interval2[1], ends at same number, move toh
                    idx1 += 1
                    idx2 += 1
            else:  # no overlap
                if interval1[0] > interval2[1]:  # interval2 is on left of interval1
                    idx2 += 1
                else:  # interval2[0] >= interval1[1]: # interval1 is on left of interval2
                    idx1 += 1

        return result


"""
Interval

simplified
"""


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            # lo: intersection start point
            # hi: intersection end point
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:  # overlap
                result.append([lo, hi])

            # remove interval with smaller end point
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result

def main():
    sol = Solution()
    assert sol.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]], 'fails'

    assert sol.intervalIntersection(firstList = [[1,7]], secondList = [[3,10]]) == [[3,7]], 'fails'


if __name__ == '__main__':
   main()