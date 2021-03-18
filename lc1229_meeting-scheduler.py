"""
1229. Meeting Scheduler
Medium

"""
from typing import List

"""
Interval

sort both slots by start time
merge two slots into one, see if merged interval has duration >= duration
if yes, break and return
if not, move one step to right on the slots that is more to left

mistakes:
1. returned interval should be just length of expected duration, not just merged result interval
2. interval [1, 2] has duration 1
3. within inner while loop, i or j could go out of bound, needs to add check as well
4. when inner loop finishes, index i or j could also be out of bound, needs to add check
"""


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])

        slots = []
        m, n = len(slots1), len(slots2)
        i, j = 0, 0

        while i < m and j < n:
            # print('i=%s j=%s' % (i, j))
            while i < m and j < n and slots1[i][1] < slots2[j][0]:  # if slots1 is to left of slots2
                i += 1
            while i < m and j < n and slots2[j][1] < slots1[i][0]:  # if slots2 is to left of slots1
                j += 1
            # slots1 and slots2 intersect
            # print('slots1[i]=%s slots2[j]=%s' % (slots1[i], slots2[j]))
            if i < m and j < n and (
                    slots2[j][0] <= slots1[i][1] <= slots2[j][1] or slots1[i][0] <= slots2[j][1] <= slots1[i][1]):
                interval = [max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])]
                if interval[1] - interval[0] >= duration:
                    return [interval[0], interval[0] + duration]
                if slots2[j][0] <= slots1[i][1] <= slots2[j][1]:
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