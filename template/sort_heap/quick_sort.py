def quicksort(nums, left, right):
    # one element, no need to sort
    if left >= right:
        return

    # pick a pivot, and partition nums into left and right two points
    # all nums in left part are smaller than pivot, and all in right part are larger than pivot
    pivot_idx = partition2(nums, left, right)

    # now recursively call quicksort to sort left part, and right part
    # excluding the pivot point, which is already in its correct position
    quicksort(nums, left, pivot_idx - 1)
    quicksort(nums, pivot_idx + 1, right)
    print(nums)

def partition(nums, left, right):
    # pick right as pivot
    # pick left as wall, iterate wall from left to right-1, for any number that is smaller than wall value, swap it with wall value
    print('partition %s %s' % (left, right))
    print(nums)
    pivot_val, wall = nums[right], left

    for i in range(left, right):
        if nums[i] < pivot_val:
            nums[wall], nums[i] = nums[i], nums[wall]
            wall += 1
        print('i=%s wall=%s nums=%s' % (i, wall, nums))

    # swap pivot value into its correct position at wall
    nums[wall], nums[right] = nums[right], nums[wall]
    print(nums)
    return wall

def partition2(nums, left, right):
    # pick right as pivot, have two pointers, start from left, and right-1 (as right is pivot index), 
    # move towards middle if number pointed by left and right are in right part 
    # (means in left part and smaller than pivot val, or in right part and larger than pivot val)
    # if both left and right pointer points at number that should be on the opposite part, then swap them
    print('partition2 left=%s right=%s nums=%s' % (left, right, nums))
    pivot_val = nums[right]

    # repeatedly move all nums smaller than pivot to left, and nums larger than pivot to right
    start, end = left, right - 1  # leave pivot (nums[right]) outside of the loop, and only swap it to its position at last
    while start <= end:
        if nums[start] <= pivot_val:
            start += 1
        elif nums[end] > pivot_val:
            end -= 1
        else:
            # if both nums[start] and nums[end] are on wrong side of pivot_val, lets swap them
            nums[start], nums[end] = nums[end], nums[start]
            # and advance the pointers
            start += 1
            end -= 1
        print('partition2 while %s' % nums)
    # now put pivot to its correct position
    # when while loop finishes, start should be the first in  the right part of pivot, so it is safe to just swap pivot value with nums[start]
    nums[start], nums[right] = nums[right], nums[start]
    print('partition2 %s' % nums)
    return start

def main():
    nums = [4, 3, 9, 6, 1, 2]
    quicksort(nums, left=0, right=5)
    assert nums == [1, 2, 3, 4, 6, 9], 'fails'

if __name__ == '__main__':
   main()