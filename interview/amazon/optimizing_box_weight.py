"""
https://leetcode.com/discuss/interview-question/1143541/amazon-oa-march-2021-sdeii
Optimizing box weight: you have 2 boxes A and B return subset A in increasing order where sum of A' weight > sum of B' weight. if More than one subset A exist, return the one with the maximal weight.
Conditions:

A & B intersection is null
Union is equevilant to original array
number of elements in A is minimal
sum of A weights > sum of B weights

Example:

n = 5

arr = [3, 7, 5, 6, 2]

The 2 subsets in arr that satisfy the conditions for A are (5, 7] and [6, 7]:

A is minimal (size 2)
Sum(A) = (5 + 7) = 12 > Sum(B) = (2+ 3+ 6) = 11
Sum(A) = (6 + 7) = 13 > Sum(B) = (2+ 3+ 5) = 10
The intersection of A and B is null and their union is equal to arr.
The subset A where the sum of its weight is maximal is [6, 7].

"""

def main():
    pass

if __name__ == '__main__':
    main()
