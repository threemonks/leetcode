"""
Do following for each digit i where i varies from least significant digit to the most significant digit.
Sort input array using counting sort (or any stable sort) according to the i’th digit.

"""
# A function to do counting sort of arr[] according to
# the digit represented by exp
def counting_sort(nums, exp):
    pass

def radix_sort(nums):
    # Find the maximum number to know number of digits
    maxnum = max(nums)
    exp = 0

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    while exp < maxnum:
        counting_sort(nums, exp)
        exp *= 10