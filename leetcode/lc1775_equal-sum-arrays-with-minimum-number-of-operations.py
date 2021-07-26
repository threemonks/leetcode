"""
1775. Equal Sum Arrays With Minimum Number of Operations
Medium

You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.



Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].


Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6

https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
"""
import collections
import heapq
from typing import List

"""
Greedy

observation:
Assuming sum(nums1) > sum(nums2), then we want to change to reduce sum(nums1), or change to increase sum(nums2). In order to minimize number of ops to achieve equal sum, we want to maximize the change obtained in each op. So we start from changing max value (6, then 5, then 4, ...) to 1 in nums1, or change small value (1, 2, ...) to 6 in nums2.

We repeat this until sum(nums1) <= sum(nums2) (we could always make a smaller change to make diff to 0, if it is less than 0), and count the number of ops along, to get minimum number of ops.

time: O(N)
space: O(N)

mistakes:
1. diff is actually max change, can go negative, as we can always choose a different number to get a smaller change
2. value range is [1,2,3,4,5,6], so we should check for i in range(6, 0, -1), not for i in range(7, 1, -1)
3. if sum(nums1) > sum(nums2), then decreasing large values in nums1 reduce diff, similarly, increasing smaller values in nums2 also reduce diff
4. we need to exit the while loop as soon as diff <= 0
5. to swap values of two variables:
    sums1, sums2 = sums2, sums1
6. in one operation, we want to try reduce diff by maximum possible change achievable by either change nums1, or nums2, but not both at the same time, so we should only try changing one array at a time, changing two in one step could result in unnecessarily do two ops, while only one op is enough.
"""


class Solution0:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 > 6 * n2 or n2 > 6 * n1:
            return -1

        sums1 = sum(nums1)
        sums2 = sum(nums2)
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)

        if sums2 > sums1:
            sums1, sums2 = sums2, sums1
            counter1, counter2 = counter2, counter1

        diff = sums1 - sums2

        op = 0

        for i in range(6, 0, -1):
            # turn 6 to 1 in counter1
            count1 = counter1[i]
            j = 7 - i
            # turn 1 to 6 in counter2
            count2 = counter2[j]
            while diff > 0 and (count1 or count2):
                if count1:
                    diff -= i - 1
                    count1 -= 1
                    op += 1
                elif count2:
                    diff -= 6 - j
                    count2 -= 1
                    op += 1

        if diff <= 0:
            return op
        else:
            return -1


"""
Greedy with heap

observation:
Assuming sum(nums1) > sum(nums2). In order to minimize number of operations, we want to maximize the change we get towards equal sum in each step, so we want to sort nums1/nums2, this leads to idea of using heap to store nums1 and nums2, so that at each step we only retrieve the smallest of num1, and largest of nums2 (assuming sum(nums1) > sums(nums2), if not, we can swap nums1 and nums2)

time O(N)
space O(N)
"""


class Solution1:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums1) < sum(nums2):
            return self.minOperations(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        if n1 > 6 * n2 or n2 > 6 * n1:
            return -1

        diff = sum(nums1) - sum(nums2)

        # heapq is min heap, we want large number first in nums1
        nums1 = [(-1) * num for num in nums1]
        heapq.heapify(nums1)
        heapq.heapify(nums2)

        op = 0
        while diff > 0 and nums1 and nums2:
            # print('diff=%s nums1=%s nums2=%s' % (diff, nums1, nums2))
            if -nums1[0] - 1 > 6 - nums2[0]:  # changing first number in nums1 would result in bigger change than nums2
                diff -= -nums1[0] - 1
                op += 1
                heapq.heappop(nums1)
            else:
                diff -= 6 - nums2[0]
                op += 1
                heapq.heappop(nums2)

        # if one nums1 or nums2 runs out, but another still has number remains
        while diff > 0 and nums1:
            # print('diff=%s nums1=%s' % (diff, nums1))
            diff -= -nums1[0] - 1
            op += 1
            heapq.heappop(nums1)

        while diff > 0 and nums2:
            # print('diff=%s nums2=%s' % (diff, nums2))
            diff -= 6 - nums2[0]
            op += 1
            heapq.heappop(nums2)

        # now diff should be <=0 if possible, otherwise cannot achieve equal sum
        return op if diff <= 0 else -1


"""
Heap

assume sum(nums1) > sum(nums2), so the op is to reduce numbers in nums1, or increase numbers in nums2, and try to use minimum number of ops to make the sum equal

we can use heap to store the num1-1, and 6-num2, and always pick the max value of the top of heap, until either we reach equal sum (diff=0), or both queue are empty

time: (N1log(N1)+N2log(N2))
mistakes:
1. while loop termate condition is target <= 0 or q1=q2=[]
"""
import heapq


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        if n1 * 6 < n2 or n2 * 6 < n1:
            return -1

        sums1 = sum(nums1)
        sums2 = sum(nums2)

        if sums2 > sums1:
            return self.minOperations(nums2, nums1)

        q1 = []  # store diff in nums1 that needs to decrease, use negative since its minheap, but we need to get biggest value first

        for num in nums1:
            if num - 1 > 0:
                heapq.heappush(q1, -(num - 1))

        q2 = []
        for num in nums2:
            if 6 - num > 0:
                heapq.heappush(q2, -(6 - num))

        target = sums1 - sums2
        ans = 0
        while target > 0 and (q1 or q2):
            if q1 and q2:
                if q1[0] < q2[0]:
                    v = heapq.heappop(q1)
                    target += v  # v<0
                    ans += 1
                else:
                    v = heapq.heappop(q2)
                    target += v  # v<0
                    ans += 1
            elif q1:
                v = heapq.heappop(q1)
                target += v  # v<0
                ans += 1
            elif q2:  # q2
                v = heapq.heappop(q2)
                target += v  # v<0
                ans += 1

        return ans

def main():
    sol = Solution()
    assert sol.minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]) == 3, 'fails'

    assert sol.minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]) == -1, 'fails'

    assert sol.minOperations(nums1 = [6,6], nums2 = [1]) == 3, 'fails'


if __name__ == '__main__':
   main()