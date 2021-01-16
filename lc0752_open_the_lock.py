"""
752. Open the Lock
Medium

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.



Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1


Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.

"""
import collections
from typing import List

"""
standard BFS traverse graph with no weight for single source shortest path 

Note: 1. convert deadends to set
      2. might merge deadends and seen set (need to take care starting point '0000')
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1  # start point in deadends
        elif target == '0000':
            return 0
        dead = set()

        for s in deadends:
            dead.add(tuple([int(c) for c in list(s)]))

        # print('dead=%s' % str(dead))

        target = tuple([int(c) for c in list(target)])
        # print('target=%s' % str(target))

        q = collections.deque()  # node arrived with less steps are added first, so first result found is shortest path
        q.append(((0, 0, 0, 0), 0))  # store coord (4 numbers) and steps to get to this node
        seen = {(0, 0, 0, 0)}

        while q:
            cur, steps = q.popleft()
            # print('cur=%s steps=%s q=%s' % (cur, steps, q))
            if cur in dead: continue
            if cur == target: return steps
            c1, c2, c3, c4 = cur
            neighbors = [
                ((c1 + 1) % 10, c2, c3, c4),
                ((c1 - 1) % 10, c2, c3, c4),
                (c1, (c2 + 1) % 10, c3, c4),
                (c1, (c2 - 1) % 10, c3, c4),
                (c1, c2, (c3 + 1) % 10, c4),
                (c1, c2, (c3 - 1) % 10, c4),
                (c1, c2, c3, (c4 + 1) % 10),
                (c1, c2, c3, (c4 - 1) % 10),
            ]
            for nei in neighbors:
                if nei not in seen:
                    q.append((nei, steps + 1))
                    seen.add(nei)

        return -1


def main():
    sol = Solution()
    assert sol.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202") == 6, 'fails'

    assert sol.openLock(deadends = ["8888"], target = "0009") == 1, 'fails'

    assert sol.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888") == -1, 'fails'

    assert sol.openLock(deadends = ["0000"], target = "8888") == -1, 'fails'


if __name__ == '__main__':
   main()