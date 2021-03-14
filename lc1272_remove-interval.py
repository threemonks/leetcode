"""
1272. Remove Interval
Medium

"""
from typing import List

"""
Sweepline

A[i][0] or b[1] might open a new interval
A[i][1] or b[0] might close a new interval

mistakes:
1. four cases, A[i] covers b, or b covers A[i], or b[0] within A[i], or b[1] within A[i]
"""


class Solution:
    def removeInterval(self, A: List[List[int]], b: List[int]) -> List[List[int]]:
        n = len(A)

        curr_start = None

        result = []

        for i in range(n):
            if A[i][0] < b[0] <= A[i][1] and A[i][0] <= b[1] < A[i][1]:  # b covered by A[i]
                result.append([A[i][0], b[0]])
                result.append([b[1], A[i][1]])
                # done with b, can early terminate
                break
                i += 1
            elif A[i][0] < b[0] <= A[i][1]:  # b[0] falls within interval
                result.append([A[i][0], min(A[i][1], b[0])])
                i += 1
            elif A[i][0] <= b[1] < A[i][1]:  # b[1] falls within interval
                result.append([max(b[1], A[i][0]), A[i][1]])
                # done with b, can early terminate
                break
                i += 1
            elif b[0] <= A[i][0] and A[i][1] <= b[1]:  # A[i] coverd by b
                i += 1
            else:
                result.append(A[i])

        if i < n:  # append rest of A if early terminates
            result += A[i + 1:]

        return result

def main():
    sol = Solution()
    assert sol.removeInterval([[0,2],[3,4],[5,7]], [1,6]) == [[0,1],[6,7]], 'fails'

    assert sol.removeInterval([[0,5]], [2,3]) == [[0,2],[3,5]], 'fails'

    assert sol.removeInterval([[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], [-1,4]) == [[-5,-4],[-3,-2],[4,5],[8,9]], 'fails'

if __name__ == '__main__':
   main()