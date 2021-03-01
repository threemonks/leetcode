"""
164. Maximum Gap
Hard

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

"""
import collections
import math
from typing import List

"""
Radix sort idea

sort numbers using smallest digit, then more/most important digit
within each digit, use counting sort

mistakes:
1. count needs to be int array of 10 for radix sort of 10 base
2. index needs to be int ((nums[i]//exp)%10), not (nums[i]/exp)%10
3. when filling nums[i] into aux array based on counting index, must start from end, i.e., nums[-1]
"""


class Solution0:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        maxval = max(nums)
        aux = [0 for _ in range(n)]
        R = 10
        exp = 1
        while maxval // exp > 0:
            # print('exp=%s' % exp)
            count = [0 for _ in range(R)]

            # counting sort
            for i in range(n):
                count[(nums[i] // exp) % 10] += 1
            # print('count=%s' % count)

            # calculate presum, which is the number of occurances of each key in count
            for i in range(1, len(count)):
                count[i] += count[i - 1]
            # print('presum=%s' % count)

            # fill aux array with each nums[i] for count[(nums[i]/exp)%10] times, starting from end of nums
            # Note, must start from nums[-1]
            for i in range(n - 1, -1, -1):
                count[(nums[i] // exp) % 10] -= 1
                aux[count[(nums[i] // exp) % 10]] = nums[i]

            # print('aux=%s' % aux)
            # now copy aux back into nums
            for i in range(n):
                nums[i] = aux[i]

            exp *= 10

        # print(nums)

        # now find max gap
        maxgap = 0
        for i in range(0, n - 1):
            maxgap = max(maxgap, nums[i + 1] - nums[i])

        return maxgap


"""
Radix sort idea

sort numbers using smallest digit, then more/most important digit, store
within each significant digit, use bucket sort

time O(N)
"""


class Solution1:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        maxval = max(nums)
        R = 10  # maximum 10 digits

        exp = 1
        while maxval / exp > 0:
            # print('exp=%s nums=%s' % (exp, nums))

            aux = [[] for _ in range(R)]

            # bucket sort?
            # store num into aux's bucket corresponding to i-th digit value
            for num in nums:
                # print('num//exp=%s (num//exp) 10=%s' % (num//exp, (num//exp)%10))
                aux[(num // exp) % 10].append(num)
                # print('aux=%s' % aux)

            # flat aux (sorted) back to nums
            # print('aux=%s' % aux)
            nums = [a for sublist in aux for a in sublist]

            # print('exp=%s nums=%s' % (exp, nums))

            exp *= 10

        # print(nums)

        # now find max gap
        maxgap = 0
        for i in range(0, n - 1):
            maxgap = max(maxgap, nums[i + 1] - nums[i])

        return maxgap


"""
Buckets and Pigeonhle principal

Pigeonhole principal: if n items are put into m containers, with n > m, then at least one container must contain more than one item.

minval, maxval = max(nums), min(nums)
n = len(nums)

if we use n bucket, and divide (maxval-minval) by n-1, then each bucket can potentially have number range (maxval-minval)/(n-1), with at least distance 1 between each adjacent bucket.

We can then fill nums[i] according to their corresponding value range and decide which bucket it falls into, along this process, we can also find out the actual gap (and therefore maxgap) between any bucket, i.e., for bucket[i] and bucket[i+1], the actual gap would be min(bucket[i+1]) - max(bucket[i])

Note that instead of storing entire buckets, we just need to store min and max value within each bucket, and using nums[i] value and bucketsize, we can directly calculate the bucket index it should fall into

time O(N)
mistakes:
1. n<2 => 0
2. some buckets might be empty
3. we should calculate max gap only after we filled all nums into buckets
4. some buckets might have default value (no nums filled in it)
5. we should not store entire bucket, we just need to store min and max value within each bucket
6. for each num, instead of loop all buckets, we can calculate its bucket index, and fill into that bucket (update its min/max) directly
"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        minval, maxval = min(nums), max(nums)

        # with this bucket size, we know we can put one number into each bucket
        # and guarantee at least distance 1 between each adjacent bucket's capacity/range
        bucket_size = max(1, (maxval - minval) // (n - 1))
        # number of buckets
        bucket_num = (maxval - minval) // bucket_size + 1
        buckets = [[math.inf, 0] for _ in range(bucket_num)]  # a tuple of min and max value

        for i in range(n):
            bucket_idx = (nums[i] - minval) // bucket_size
            buckets[bucket_idx][0] = min(buckets[bucket_idx][0], nums[i])
            buckets[bucket_idx][1] = max(buckets[bucket_idx][1], nums[i])

        maxgap = 0
        # skip empty buckets
        buckets = [bucket for bucket in buckets if (0 < bucket[0] < math.inf and 0 < bucket[1] < math.inf)]
        # print('buckets=%s' % buckets)
        for i in range(len(buckets) - 1):
            if i > 0:
                maxgap = max(maxgap, buckets[i][0] - buckets[i - 1][1])
            maxgap = max(maxgap, buckets[i + 1][0] - buckets[i][1])
            # print('i=%s maxgap=%s' % (i, maxgap))

        return maxgap

def main():

    sol = Solution()

    assert sol.maximumGap([3,6,9,1]) == 3, 'fails'

    assert sol.maximumGap([10]) == 0, 'fails'


if __name__ == '__main__':
   main()