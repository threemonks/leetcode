"""
470. Implement Rand10() Using Rand7()
Medium

734

246

Add to List

Share
Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?


Example 1:

Input: n = 1
Output: [2]
Example 2:

Input: n = 2
Output: [2,8]
Example 3:

Input: n = 3
Output: [3,8,10]


Constraints:

1 <= n <= 10^5
"""
# The rand7() API is already defined for you.
def rand7():
    """

    @return a random integer in the range 1 to 7
    """
    pass

"""
Rejection Sampling

use rand7() to implement rand10
steps:
1. run rand7() twice, it will generate 49 outcomes grid[i][j] for i=1...7, j=1...7, we take the value of index vals[i][j]%10

[[1, 2, 3, 4, 5, 6, 7],
[8, 9,10, 1, 2, 3, 4],
[5, 6, 7, 8, 9,10, 1],
[2, 3, 4, 5, 6, 7, 8],
[9,10, 1, 2, 3, 4, 5],
[6, 7, 8, 9,10, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
]

use unfair coins to simulate fair coin game:
given an unfair coin, say 60% probability head, 40% probabiliy tail, how to simulate a fair game?
throw coin twice, if both times same (both head, or both tail), ignore the result
                  if first head, second tail, consider head, if first tail second head, consider tail, then this is equal probability head/tail
"""


class Solution0:
    def rand10(self):
        """
        :rtype: int
        """
        matrix = [[1, 2, 3, 4, 5, 6, 7],
                  [8, 9, 10, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9, 10, 1],
                  [2, 3, 4, 5, 6, 7, 8],
                  [9, 10, 1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  ]

        ans = 0
        while ans == 0:
            i = rand7()
            j = rand7()
            ans = matrix[i - 1][j - 1]

        return ans


"""
Rejection sampling

Note we cannot simplify 7*(rand7()-1)+(rand7()-1) to 8 * (rand7() - 1) because:

7 * (rand7() - 1) + (rand7() - 1) calls rand7() twice, it generates a uniform random integer in range of [0, 48], which is rand49() - 1.

8 * (rand7() - 1) calls rand7() only once, actually it's still rand7(), just multiplied by 8. The value of 8 * (rand7() - 1) is a uniform random integer taken from the set {0, 8, 16, 24, 32, 40, 48}. Obviously it's not rand49().

"""


class Solution:
    def rand10(self):
        result = 40
        while result >= 40:
            result = 7 * (rand7() - 1) + (rand7() - 1)

        return (result % 10) + 1
