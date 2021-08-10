"""
1539. Kth Missing Positive Number
Easy

1288

85

Add to List

Share
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

"""
from typing import List

"""
Brutal force
[2,3,4,7,11]

time O(N)
"""


class Solution0:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        i, j = 1, 0

        while i <= max(arr):
            while i < arr[j]:
                k -= 1
                if k == 0:
                    return i
                i += 1
            i += 1
            j += 1

        i -= 1  # cancel the last i += 1 after i == max(arr)

        while k:
            i += 1
            k -= 1

        return i


"""
Brutal force

scan through array, count number of missing numbers between elements

O(N)
"""


class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # if kth missing is less than arr[0]
        if k <= arr[0] - 1:
            return k

        k -= arr[0] - 1

        # search for kth missing between array alements
        for i in range(1, len(arr)):
            curr_missing = arr[i] - arr[i - 1] - 1  # numbers missing between two adjacent elements
            # if the kth missing is between arr[i-1] and arr[i] => return it
            if k <= curr_missing:
                return arr[i - 1] + k
            k -= curr_missing

        # if the missing number is greater than arr[-1]
        return arr[-1] + k


"""
Binary Search

             [ 2, 3, 4, 7, 11]
sequential #   1  2  3  4  5 
# of missing:  1  1  1  3  6 <= # of positive integers missing before arr[i] = arr[i]-i-1

the # of missing is a increasing sequence, thus we can use binary search to find k-th missing

time O(logN)
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            elif arr[mid] - mid - 1 >= k:
                right = mid - 1

        # when loop exits, left = right+1
        # kth missing is between arr[right] and arr[left]
        # number of integers missing before arr[right] is arr[right]-right-1
        # so kth missing is arr[right] + k - (arr[right]-right-1) = left+k
        return left + k

def main():
    sol = Solution()
    assert sol.findKthPositive(arr = [2,3,4,7,11], k = 5) == 9, 'fails'

    assert sol.findKthPositive(arr = [1,2,3,4], k = 2) == 9, 'fails'


if __name__ == '__main__':
   main()