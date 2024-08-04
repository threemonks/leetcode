"""
We have an NxN matrix of numbers and we want to compute the min of each WxW window. The return value is also a matrix, containing for each window the min value computed for it.


Input Matrix:
[ 1  6     3    8]
[ 5  2     7    4]
[ 9  10   15   12]
[13  14   16   11]

[1 2  3   4]
[5 2  7   4]
[9 10 15 11]

Input Matrix: NxN
Window: WxW

W=2

Output Matrix:
[1  2    3]
[2  2    4]
[9 10   11]

n = 4
w = 2
n-w+1

"""
import math
import heapq
"""
using minheap to hold all values of the sub-matrix elements (with index), when checking/retrieving min value of the given sub-matrix, drop values that is out of bound of the sub-matrix (by checking its index), time complexity `O(n*n*log(k))`
"""

def matrix_min_size_k(inputs, k):
    n = len(inputs)
    m = n - k + 1

    ans = [[math.inf for _ in range(m)] for _ in range(m)]

    hq = []

    # insert the first k*k values into hq
    heapq.heapify(hq)
    for i in range(k):
        for j in range(k):
            heapq.heappush(hq, (inputs[i][j], i, j))

    print(f"{hq = }")
    ans[0][0] = hq[0][0]

    for i in range(m):
        # insert first w elements of i-th row
        for j in range(k):
            heapq.heappush(hq, (inputs[i][j], i, j))
        for j in range(m):
            # i,j is upper left corner, and x,y is bottom right corner of the sub-matrix
            x = i + k - 1
            y = j + k - 1
            # range covered is (i, j) ... (x, y)
            for l in range(i, x+1):
                print(f"{i = } {j = } {x = } {y = } {l = }")
                heapq.heappush(hq, (inputs[l][y], l, y))
            while (hq[0][1] < i or hq[0][1] > x or hq[0][2] < j or hq[0][2] > y):
                print(f"remove outof bound nodes {i = } {j = } {x = } {y = } {hq[0] = }")
                heapq.heappop(hq) # remove min value with index out of range
            # now hq[0] is a valid min value
            print(f"{i = } {j = } {x = } {y = } {hq = }")
            ans[i][j] = hq[0][0]
            print(f"{i = } {j = } {x = } {y = } {ans = }")

    print(ans)
    return ans


inputs = [[ 1, 6, 3, 8], [5, 2, 7, 4], [9, 10, 15, 12], [13, 14, 16, 11]]

output = [[1, 2, 3],
[2,  2,  4],
[9, 10, 11]
]

assert matrix_min_size_k(inputs, 2) == output, 'fails'

