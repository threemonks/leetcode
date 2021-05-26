"""
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Medium

566

30

Add to List

Share
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.



Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
Example 3:

Input: arr = [2,3]
Output: 0
Example 4:

Input: arr = [1,3,5,7,9]
Output: 3
Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8


Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8

"""
from collections import defaultdict
from typing import List

"""
Brutal force

subarray 
a (arr[i]^arr[i+1]^...^arr[j-1]) == b (arr[j]^arr[j+1]^...^arr[k])
a==b
<=> a^b == 0
<=> arr[i]^arr[i+1]^...^arr[j-1]^arr[j]^...^arr[k] == 0
<==>pre_xor[i] == pre_xor[j] => adds i-j-1 triplets to answer

and each such subarray of xor equals 0, adds k-i triplets into ans

two pointers iterate and check all possible subarrays, if subarray xors is zero, add length-1 to ans

time O(N^2)
"""


class Solution0:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        ans = 0

        for i in range(n):
            xors = arr[i]
            for j in range(i + 1, n):
                xors ^= arr[j]
                # print('i=%s j=%s xors=%s' % (i, j, xors))
                if xors == 0:
                    ans += j - i

        return ans


"""
Hash Map

subarray a (arr[i]^arr[i+1]^...^arr[j-1]) == b (arr[j]^arr[j+1]^...^arr[k]) <=> a^b == 0
<=> arr[i]^arr[i+1]^...^arr[j-1]^arr[j]^...^arr[k] == 0
and each such subarray of xor equals 0, adds k-i triplets into ans

if we calculate prefix xor, then we are basically looking for all pairs of repeating prefix-xor value, and sum these pair index distance.

        [2,   3,   1,   6,   7]
bin     10   11   01  110   111 
pre_xor 10   01    0  110    01
pair j             i            => add i-j-1=2 triplets
pair          j               i => add i-j-1=2 triplets

time O(N)
space O(N)
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        cur_xor = 0
        indices = defaultdict(list)  # hold list of index where pre_xor value is the value of the key
        indices[0] = [-1]  # add dummy index -1, so that we can calculate for pre_xor value 0
        ans = 0

        for i in range(n):
            cur_xor ^= arr[i]
            if cur_xor in indices:
                for j in indices[cur_xor]:
                    ans += i - j - 1  # subarray arr[j...i] adds i-j-1 valid triplets
            indices[cur_xor].append(i)

        return ans


def main():
    sol = Solution()
    assert sol.countTriplets(arr = [2,3,1,6,7]) == 4, 'fails'

    assert sol.countTriplets(arr = [1,1,1,1,1]) == 10, 'fails'

    assert sol.countTriplets(arr = [2,3]) == 0, 'fails'

    assert sol.countTriplets(arr = [1,3,5,7,9]) == 3, 'fails'

    assert sol.countTriplets(arr = [7,11,12,9,5,2,7,17,22]) == 8, 'fails'

if __name__ == '__main__':
   main()