"""
https://www.tutorialspoint.com/program-to-find-how-many-swaps-needed-to-sort-an-array-in-python

Suppose, we have an array called nums and we have to find the number of swaps needed to make nums sorted in any order, either ascending or descending.

So, if the input is like nums = [2, 5, 6, 3, 4], then the output will be 2 because initially nums has [2, 5, 6, 3, 4]. If we swap numbers 6 and 4, the array will be [2,5,4,3,6]. Then, if we swap the numbers 5 and 3, the array will be [2,3,4,5,6]. So 2 swaps are needed to make the array sorted in ascending order.

"""

"""
Ideas:

1. sort array val with index => pos
   pos := new list containing tuples (item_postion, item) for each item in input_arr
2. cnt := 0
    loop through all index from 0 to n (array size)
    for index in range 0 to size of input_arr, do
        while True, do
            if pos[index, 0] is same as index, then
                exit from the loop
            otherwise,
                cnt := swap_count + 1
                swap_index := pos[index, 0]
                swap the values of (pos[index], pos[swap_index])    
"""
def swap_count(input_arr):
   pos = sorted(list(enumerate(input_arr)), key=lambda x: x[1])
   cnt = 0

   for index in range(len(input_arr)):
      while True:
         if (pos[index][0] == index):
            break
         else:
            cnt += 1
            swap_index = pos[index][0]
            pos[index], pos[swap_index] = pos[swap_index], pos[index]

   return cnt

def solve(input_arr):
   return min(swap_count(input_arr), swap_count(input_arr[::-1]))

nums = [2, 5, 6, 3, 4]
print(solve(nums))
