##  Sorting Algorithm

### Counting Sort
* Advantage: complexity – O(n+k), n size of sorted array and k is the size of the helper array (range of distinct values)
* Disadvantage: only to sort discrete values (for example integers), because otherwise the array of frequencies cannot be constructed
* it is linear O(n+k) when elements are in the range from 1 to k

## Bucket Sort
* Limitation: mainly useful when input is uniformly distributed over a range

## Radix Sort
* For each digit where varies from the least significant digit to the most significant digit of a number
* Sort input array using counting sort algorithm according to ith digit.

## Pancake Sort
* Start from current size equal to n and reduce current size by one while it’s greater than 1. Let the current size be curr_size. Do following for every curr_size
* Find index of the maximum element in arr [ 0..curr_szie-1 ]. Let the index be ‘mi’
* Call flip(arr, mi)
* Call flip(arr, curr_size-1)

