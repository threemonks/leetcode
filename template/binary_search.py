"""

"""
import logging
from queue import Queue
from typing import List

FORMAT = "%(asctime)s - {%(pathname)s : %(lineno)s : %(funcName)s} - %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

"""
Template #1 
search for exact value
Template #1 is used to search for an element or condition which can be determined by accessing a single index in the array.

Key Attributes:
* Most basic and elementary form of Binary Search
* Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
* No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

Distinguishing Syntax:

Initial Condition: left = 0, right = length-1
Termination: left > right
Searching Left: right = mid-1
Searching Right: left = mid+1

"""
def search(nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1  # [] left close, right close
    while left <= right:
        mi = (right + left) // 2
        if nums[mi] == target:
            return mi
        elif nums[mi] < target:
            left = mi + 1
        else:  # nums[i] > target
            right = mi - 1

    return -1

"""
Binary Search Template II

Template #2 is an advanced form of Binary Search. It is used to search for an element or condition which requires accessing the current index and its immediate right neighbor's index in the array.

Key Attributes:

* An advanced way to implement Binary Search.
* Search Condition needs to access the element's immediate right neighbor
* Use the element's right neighbor to determine if the condition is met and decide whether to go left or right
* Guarantees Search Space is at least 2 in size at each step
* Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

Distinguishing Syntax:

Initial Condition: left = 0, right = length
Termination: left == right
Searching Left: right = mid
Searching Right: left = mid+1
"""

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1

"""
https://daimajiaoliu.com/daima/6cc85e7a84a2803
https://daimajiaoliu.com/daima/487220eaf900404

4. 寻找左侧边界的二分搜索

public int binarySearch(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0;
    //因为要搜索左侧边界，所以索引最大位置必须大于数组长度，搜索的区间为[left, right)
    int right = nums.length;
    
    //其他代码
    while (left < right) {
        int mid = (left + right) >>> 1;
        if (nums[mid] == target) {
            right = mid;
        } else if (target > nums[mid]) {
            // 下一轮搜索区间是 [mid + 1, right]
            left = mid + 1;
        } else {
            // 下一轮搜索区间是 [left, mid)
            right = mid;
        }
    }
    return nums[left] == target ? left : -1;
}

5. 寻找右侧边界的二分查找

public int right_bound(int[] nums, int target) {
    if (nums.length == 0) return -1;
    int left = 0, right = nums.length;

    while (left < right) {
        int mid = (left + right) / 2;
        if (nums[mid] == target) {
            left = mid + 1; // 注意
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid;
        }
    }
    return left - 1; // 注意
}


"""

def left_bound(nums, target):
    """
    find left boundary, i.e., the left most position i to insert target such that all nums[:i] < target, and all nums[i:] >= target

    :param nums:
    :param target:
    :return:
    """
    n = len(nums)
    left, right = 0, n # search for boundary, could be n, so we use [0, n)
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] == target: # for left boundary, when nums[mid] == target, do not exclude mid, keep searching to left
            right = mid
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid+1

    return left if nums[left] == target else -1 # when exit while loop, nums[lo] == target

def right_bound(nums, target):
    """
    find right boundary, i.e., the right most position i to insert target such that all nums[:i] <= target, and all nums[i:]>target
    :param nums:
    :param target:
    :return:
    """
    n = len(nums)
    left, right = 0, n
    while left < right:
        mid = left + (right - left)//2
        if nums[mid] == target: # for right bound, nums[mid] == target => exclude mid, keep searching to right
            left = mid+1
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid

    return left-1

"""
Python module bisect
https://github.com/python/cpython/blob/main/Lib/bisect.py
"""

def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(i, x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def bisect_left(a, x, lo=0, hi=None, *, key=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(i, x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def lower_bound(nums, left, right, value):
    """
    this is from python standard lib bisect.bisect_left
    求非降序分为[left, right)内第一个不小于value的值的位置
    :return:
    """
    while left < right: # 搜索区间[left, right) 左闭右开 不为空
        mid = left + (right-left)//2 # 防溢出
        if nums[mid] < value: left = mid+1
        else: right = mid

    return left # right也行，因为[left, right)为空时它们重合


def binary_serach(nums, left, right, value):
    """
    this is from python standard lib bisect.bisect_left
    求非降序分为[left, right)内第一个match value的值的位置
    :return:
    """
    while left < right:  # 搜索区间[left, right) 左闭右开 不为空
        mid = left + (right - left) // 2  # 防溢出
        if nums[mid] == value:
            return mid
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid

    return -1 # 没有找到


def binary_search(nums, val):
    """
    binary search # use half close range (left close, right open) 左闭右开
    # invariant if val is in nums, it must be within [lo, hi) or val does not exist in nums
    :return:
    """
    lo = 0
    hi = len(nums)
    while lo < hi:
        mi = lo + (hi-lo)//2
        if nums[mi] == val:
            return mi
        elif nums[mi] < val:
            lo = mi + 1
        else: # nums[mi] > val:
            hi = mi

    return -1


def binary_search1(nums, val):
    """
    binary search # use close range
    # invariant if val is in nums, it must be within [lo, hi] or val does not exist in nums
    :return:
    """
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mi = lo + (hi-lo)//2
        if nums[mi] == val:
            return mi
        elif nums[mi] < val:
            lo = mi + 1
        else: # nums[mi] > val:
            hi = mi-1

    return -1

"""
https://www.topcoder.com/thrive/articles/Binary%20Search
"""
def binary_search(lo, hi, p):
    while lo < hi:
        mid = lo + (hi - lo) / 2
        if p(mid) == True:
            hi = mid
        else :
            lo = mid + 1

    if p(lo) == False:
        return -1 # p(x) is false for all x in S!

    return lo # lo is the least x for which p(x) is true

def main():
    assert binary_search1([1,3,5,6,7,8,10,15,25,32,35,45,54,67,71,87,99], 35) == 10, 'fails'

    assert binary_search1([1,3,5,6,7,8,10,15,25,32,35,45,54,67,71,87,99], 34) == -1, 'fails'

    assert binary_search1([1,3,5,6,7,8,10,15,25,32,35,45,54,67,71,87,99], 1) == 0, 'fails'

    assert binary_search1([1,3,5,6,7,8,10,15,25,32,35,45,54,67,71,87,99], 99) == 16, 'fails'

    assert binary_search1([1,3,5,6,7,8,10,15,25,32,32,35,45,54,67,71,87,99], 99) == 17, 'fails'

    assert binary_search1([1,3,5,6,7,8,10,15,25,32,32,35,45,54,67,71,87,99], 32) == 9, 'fails'

if __name__ == '__main__':
   main()