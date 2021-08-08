"""
1151. Minimum Swaps to Group All 1's Together
Medium

485

4

Add to List

Share
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.



Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation:
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation:
Since there is only one 1 in the array, no swaps needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation:
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
Example 4:

Input: data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
Output: 8


Constraints:

1 <= data.length <= 10^5
data[i] is 0 or 1.

"""
from typing import List

"""
Sliding Window

sliding window with minimum number of zeros, and window size = total # of ones

note:
1. window boundary [left, right+1] => size right-left+1
2. special case ones = 1 => no swaps required # with correct window size, no need special handling

time O(N)
"""
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        winsize = sum([d for d in data if d])
        ans = n
        zeros = 0 # count of zeros within the window
        left, right = 0, 0
        for right in range(n):
            zeros += 1-data[right]
            while right-left+1 > winsize:
                zeros -= 1-data[left]
                left += 1
            if right-left+1 == winsize:
                ans = min(ans, zeros)

        return ans


def main():
    sol = Solution()

    assert sol.minSwaps(data = [1,0,1,0,1]) == 1, 'fails'

    assert sol.minSwaps(data = [0,0,0,1,0]) == 0, 'fails'

    assert sol.minSwaps(data = [1,0,1,0,1,0,0,1,1,0,1]) == 3, 'fails'

    assert sol.minSwaps(data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]) == 8, 'fails'

if __name__ == '__main__':
   main()