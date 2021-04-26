"""
327. Count of Range Sum
Hard

1034

120

Add to List

Share
Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.



Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1


Constraints:

1 <= nums.length <= 10^4
-231 <= nums[i] <= 2^31 - 1
-3 * 104 <= lower <= upper <= 3 * 10^4


Follow up: A naive algorithm of O(n2) is trivial, Could you do better than that?
"""
from typing import List
from collections import defaultdict
import bisect

"""
HashMap + Prefix sum

calculate all prefix sum as presum, for each such prefix sum psum, for each number between lower and upper, check if psum-target exists in dict counts{psum: count of psum}, if it does, adds counts[target-psum] into result

time O(n*(upper-lower)) => 6*10^8

mistakes:
1. needs to add dummy 0 in front of prefix sum, to make calculating range sum include first value, since single element is also a valid count
"""
class Solution0:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        presum = [0]*(n+1) # add dummy [0]
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        counts = defaultdict(int)

        ans = 0
        for psum in presum:
            for target in range(lower, upper+1):
                if psum - target in counts:
                    # print('psum=%s target=%s counts=%s' % (psum, target, counts))
                    ans += counts[psum - target]
            counts[psum] += 1

        return ans

"""
Merge Sort + Counting

during merge sorting of prefix sum, after sorted left and right, during merging stage, for each presum in left presm[i], count how many presum[j] on right part satisfying  the following condition

a <= presum[j] - presum[i] <= b with j > i

i.e.
count[i] = count of a <= presum[j] - presum[i] <= b with j > i
ans = sum(count[:])


"""
class Solution1:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        presum = [0]*(n+1) # add dummy [0]
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        # l and r both inclusrive
        def mergesort(l, r):
            # count how many
            if l == r:
                return 0
            mid = l+(r-l)//2
            count = mergesort(l, mid) + mergesort(mid+1, r)

            i = j = mid+1

            for left in presum[l:mid+1]:#对于左半部分每一个
                while i <= r and presum[i] - left < lower:#找到到右边最小的满足presum[i]-left>=lower的index i
                    i += 1
                while j <= r and presum[j] - left <= upper:#找到右边最大的满足presum[j]-left<=upper的index j(找到的j是第一个不满足此条件的index，所以满足条件的最大index是j-1)
                    j += 1
                count += j-i #所以有j-i个满足条件的presum

            presum[l:r+1] = sorted(presum[l:r+1]) #需要把已经排好序的部分放入排序合并结果
            return count

        return mergesort(0, len(presum)-1)


"""
Fenwick Tree + Prefix Sum

Sum[k] is the sum of first k numbers. O(N^2) solution is

for j in range(n + 1):
    for i in range(j):
        if lower <= Sum[j] - Sum[i] <= upper: res += 1
This is equal to:

collection = empty
for sum_j in Sum:
    sum_i_count = how many sum_i in this collection that sum_j - upper <= sum_i <= sum_j - lower
    res += sum_i_count
    put sum_j into this collection

so for each sum[j], we count how many sum[i] falls within [sum[j]-upper, sum[j]-lower]

mistakes:
1. needs to add dummy 0 in front of prefix sum
2. segment tree should only hold count, no actual value at leaf node, but we update parent nodes with a new value inserting at leaf node, note we are building tree once via inserting, no more updating later
3. segment tree range is 0 to len(presum)-1

time O(N*log(N))
"""

class FenwickTree:
    def __init__(self, n):
        self.sums = [0]*(n+1)

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)
        return s

    def _lowbit(self, i):
        return i & (-i)

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        presum = [0]*(n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        sorted_presum = sorted(presum)
        l = len(presum)
        # also need to sort presum and remove duplicates
        self.fwt = FenwickTree(l)

        ans = 0
        for psum in presum:
            """
            ind = bisect.bisect_right(sorted_presum, psum - lower) will get the smallest ind that sorted_presum[ind] > psum - lower. So all sums from index 0 to ind-1 inclusive will be <= psum - lower. The count for those sums would be search(ind - 1 + 1). The +1 here is because the index of BIT starts from 1.

Same for bisect.bisect_left(sortSum, sum_j - upper).
            """
            ans += self.fwt.query(bisect.bisect_right(sorted_presum, psum - lower)) - self.fwt.query(bisect.bisect_left(sorted_presum, psum - upper))
            self.fwt.update(bisect.bisect_left(sorted_presum, psum) + 1, 1)
        return ans

def main():
    sol = Solution()
    assert sol.countRangeSum(nums = [-2,5,-1], lower = -2, upper = 2) == 3, 'fails'

    assert sol.countRangeSum(nums = [0], lower = 0, upper = 0) == 1, 'fails'



if __name__ == '__main__':
   main()