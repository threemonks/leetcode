"""
1562. Find Latest Group of Size M
Medium

278

63

Add to List

Share
Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.

At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.



Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
Example 3:

Input: arr = [1], m = 1
Output: 1
Example 4:

Input: arr = [2,1], m = 2
Output: 2


Constraints:

n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
All integers in arr are distinct.
1 <= m <= arr.length
"""
import math
from typing import List

"""
brutal force 
loop through array, keep adding (|) new integer to get new result integer (bit string), and check each bit string if it matches exactly m ones in a group or not.

TLE

"""
from functools import lru_cache


class Solution0:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        mones = '1' * m

        @lru_cache(None)
        def check_mones(s):
            nonlocal mones, m
            if len(s) == len(mones) and s == mones:
                return True
            elif len(s) > len(mones) and (
                    s.startswith(mones + '0') or s.endswith('0' + mones) or '0' + mones + '0' in s):
                return True
            else:
                return False

        latest_step = -1
        bs = 0
        for i, a in enumerate(arr):
            bs = bs | (1 << (n - a))
            s = bin(bs)[2:]
            # print('i=%s s=%s' % (i, s))
            if check_mones(s):
                latest_step = i + 1

        return latest_step


"""
observation:
arr[3] = 4 # at step 3, we set digit 4 to one
<=> steps[4] = 3 # digit 4 is set to one at step 3

For a group of bits [i, i+m-1] to be a valid group, all bits in this group must be turned into '1', and the group is valid at step 1 if and only if bit [i-1] and [i+m] is still '0' at step t, i.e., '0[1111]0'

once a group becomes valid, it will remains valid until one of [i-1] or [i+m] turns '1'. so the last step it will remain valid would be min(steps[i-1], steps[i+m]) - 1.

The step t is basically the largest value within steps[i:i+m], this is a sliding window maximum problem 
Sliding Window Maximum (https://leetcode.com/problems/sliding-window-maximum/)

    res = max(res, min(steps[i-1], steps[i+m])-1)

"""
import collections


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:  # if arr has size m
            return n

        # add sentinel value to arr
        arr = [0] + arr

        steps = [-1] * (n + 1)

        for i in range(1, n + 1):
            steps[arr[i]] = i

        # print('steps=%s' % steps)

        # deque stores index of steps that are still possible candidate for later
        q = collections.deque()
        q.append(0)

        res = -1

        for i in range(1, n + 1):
            # print('i=%s q=%s steps=%s' % (i, q, steps))
            # at each iterate, the new value would bump off any previous value from end of deque that is less attractive (smaller value, older steps, as we are looking for latest step)
            while q and steps[q[-1]] <= steps[i]:  # same value, newer ones pops old ones
                q.pop()
            # and we drop any items from front of deque that are now outside the sliding window
            while q and q[0] + m <= i:
                q.popleft()
            # now add new item
            q.append(i)
            # print('i=%s q=%s' % (i, q))
            # check if there's a good result
            # check to make sure the bit to left and right of sliding window are not set yet (exactly m ones)
            if i >= m:  # we need at least m bits set
                t = steps[q[0]]
                left = steps[
                    i - m] if i - m >= 1 else math.inf  # virtual left boundary is at q[0]-1==0, and the sentinel value should be math.inf since we are taking min(left, right) later
                right = steps[i + 1] if i + 1 <= n else math.inf
                if left > t and right > t:
                    res = max(res, min(left, right) - 1)

        return res


def main():
    sol = Solution()
    assert sol.findLatestStep([3,5,1,2,4], 1) == 47, 'fails'

    assert sol.findLatestStep([3,1,5,4,2], 2) == -1, 'fails'

    assert sol.findLatestStep([1], 1) == 1, 'fails'

    assert sol.findLatestStep([2,1], 2) == 2, 'fails'



if __name__ == '__main__':
   main()