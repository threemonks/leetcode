"""
975. Odd Even Jump
Hard

950

292

Add to List

Share
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.



Example 1:

Input: arr = [10,13,12,14,15]
Output: 2
Explanation:
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.
Example 2:

Input: arr = [2,3,1,1,4]
Output: 3
Explanation:
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
number of jumps.
Example 3:

Input: arr = [5,1,3,4,2]
Output: 3
Explanation: We can reach the end from starting indices 1, 2, and 4.


Constraints:

1 <= arr.length <= 2 * 10^4
0 <= arr[i] < 10^5

"""
from typing import List

"""
DP + MonoStack

observation:
last one always true
We have to jump higher (odd step) and lower (even) alternately to the end.

so if we use two array, higher, lower to represent if we can jump same or higher or same or lower to certain index i, we can work backwards, from right to left

next_min_ge[i] holds the next minimum greater or equal to number's index j where j satisfies i < j and A[i] <= A[j]
next_max_le[i] holds the next maximum less or equal to number's index j where j satisfies i < j and A[i] >= A[j]

the transition would be:
higher[i] = lower[j] where j is maximum value to right of i s.t. nums[j]<=nums[i]
lower[i] = higher[j] where j is minimum value to right of i s.t. nums[j]>=nums[i]

Note that we can pre-process arr using monotonic increasing stack to find minimum value larger than nums[i] to the right of i

thoughts:
maybe we can use DP with SortedDict to store the smallest larger number (or largest smaller number) on right

time O(Nlog(N)) - sort
"""


class Solution0:
    def oddEvenJumps(self, nums: List[int]) -> int:
        n = len(nums)

        # find index that an odd jump from i can land on
        # i.e., smallest number that's larger than nums[i] on right, if multiple, take smallest such index
        # 0 if not found
        next_min_ge = [0] * n
        st = []
        for a, i in sorted([a, i] for i, a in enumerate(nums)):
            # mono stack (from sorted array) guarantees nums[st[-1]]<nums[i] and nums[i] is smallest such number,
            # and we check st[-1]<i to ensure i is on right
            while st and st[-1] < i:
                next_min_ge[st.pop()] = i
            st.append(i)

        # find index that an even jump from i can land on
        # i.e., largest number that's smaller than nums[i] on right, if multiple, take smallest index
        next_max_le = [0] * n
        st = []
        for a, i in sorted([-a, i] for i, a in enumerate(nums)):
            while st and st[-1] < i:
                next_max_le[st.pop()] = i
            st.append(i)

        # now try to fill odd and even from right to left
        odd = [0] * n  # odd jump #, must go same or higher (but as small as possible)
        even = [0] * n  # even jump # must go same or lower (but as larger as possible)
        odd[-1], even[-1] = 1, 1  # last index is always true (No need to jump)
        for i in range(n - 2, -1, -1):
            odd[i] = even[next_min_ge[i]]
            even[i] = odd[next_max_le[i]]

        # we always start with odd jump (1st)
        # so odd contains the valid number of jumps to reach end
        return sum(odd)


"""
DP + SortedDict

traverse from right to left, end index is True, and if early odd jump odd[i-1] can get to index i, and even[i] is True, then odd[i-1] is also True

we iterate the array from right to left, retrieve the smallest larger number (or largest smaller number) and store it as next_min_higher or next_max_lower number for nums[i]. use SortedDict to store values and their index found so far, so that we can use SortedDict.bisect_left to find largest smaller or smallest larger number in O(logN) time

SortedDict保存的是从右往左到当前位置看到的每个value的最近的，也是最小的index，所以对于nums[i]，用sd.bisect_left(nums[i])找到的idx就是最小的大于nums[i]的index， idx-1就是

if nextJump is the valid jump from A[i] if such exists, then odd[nextJump]=True => even[i] = odd[nextJump] = True

time O(Nlog(N))
"""
from sortedcontainers import SortedDict


class Solution:
    def oddEvenJumps(self, nums: List[int]) -> int:
        n = len(nums)

        sd = SortedDict()  # {num: index}, we iterate nums from right to left, so if there's duplicate value, sd always have latest (smallest) index at given time

        oddjump = [False] * n  # oddjump[i]: can we do a odd jump at index i to reach end
        evenjump = [False] * n
        oddjump[n - 1] = True  # last index is always True
        evenjump[n - 1] = True

        for i in range(n - 1, -1, -1):
            # if there are duplicate numbers, that's always the first choice
            # since it is smallest larger or equal number, or largest smaller or equal number
            if nums[i] in sd:
                oddjump[i] = evenjump[sd[nums[i]]]
                evenjump[i] = oddjump[sd[nums[i]]]
            else:
                # smallest larger or equal number to right
                idx = sd.bisect_left(nums[i])
                if idx != len(sd):
                    oddjump[i] = evenjump[sd.peekitem(idx)[1]]

                # largest smaller or equal number to right
                idx = sd.bisect_left(nums[i]) - 1
                if idx != -1:
                    evenjump[i] = oddjump[sd.peekitem(idx)[1]]

            # update sd
            sd[nums[i]] = i

        return oddjump.count(True)


def main():
    sol = Solution()
    assert sol.oddEvenJumps([10,13,12,14,15]) == 2, 'fails'

    assert sol.oddEvenJumps([2,3,1,1,4]) == 3, 'fails'

    assert sol.oddEvenJumps([5,1,3,4,2]) == 3, 'fails'

if __name__ == '__main__':
   main()