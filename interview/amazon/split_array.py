"""
https://leetcode.com/discuss/interview-experience/1316685/amazon-oa-sde1-new-questions

Given an array of integers, determine the number of ways the entire array be split into two non-empty subarrays, left and right, such that the sum of elements in the left subarray is greater than the sum of elements in the right subarray.

Example

arr =  [10, 4, -8, 7]

There are three ways to split it into two non-empty subarrays:



[10] and [4, -8, 7], left sum = 10, right sum = 3


[10, 4] and [-8, 7], left sum = 10 + 4 = 14, right sum = -8 + 7 = -1


[10, 4, -8] and [7], left sum = 6, right sum = 7

The first two satisfy the condition that left sum > right sum, so the return value should be 2.

public List<Integer> count(List<Integer> arr) {
    if (arr.length == 0 ) return 0;
    int leftSum = 0;
    int rightSum = 0;
    int count = 0;

    for (int i : arr) {
        leftSum += i;
    }

    for (int i = arr.length - 1; i >= 0; i--) {
        rightSum += arr[i];
        leftSum -= arr[i];

        if (rightSum < leftSum && (rightSum != 0 && leftSum != 0)) {
            count++;
        }
    }
    return count;
}
"""

"""
get total sum, iterate from left to right, each left prefix sum > (total sum / 2) is one valid answer count

"""
class Solution:
    def count(self, nums):
        sums = sum(nums)

def main():
    pass

if __name__ == '__main__':
    main()
