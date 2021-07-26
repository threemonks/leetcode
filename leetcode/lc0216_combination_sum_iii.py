"""
216. Combination Sum III
Medium

1645

63

Add to List

Share
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.


Constraints:

2 <= k <= 9
1 <= n <= 60

"""
from typing import List
"""
backtrack / recursive
"""
class Solution0:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.backtrack(1, [], k, n)

        return self.result

    def backtrack(self, idx, path, k, target):
        if len(path) == k and target == 0:
            self.result.append(path)
            return
        if idx > 9 or target < 0 or len(path) >= k or idx > target:
            return

        for i in range(idx, 10): # number 1 to 9
            if i > target:
                continue
            self.backtrack(i+1, path+[i], k, target-i)


"""
iterative (similar to recursive, but using stack directly)
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        total, start, path = 0, 1, []
        stack = [(total, start, path)]
        result = []
        while stack:
            total, start, path = stack.pop()
            if total == n and len(path) == k:
                result.append(path)
                continue
            for i in range(start, 10):
                if total + i > n:
                    break
                stack.append((total+i, i+1, path+[i]))

        return result


def main():
    sol = Solution()
    assert sol.combinationSum3(k = 3, n = 7) == [[1,2,4]], 'fails'

    assert sorted(sol.combinationSum3(k = 3, n = 9)) == sorted([[1,2,6],[1,3,5],[2,3,4]]), 'fails'

    assert sol.combinationSum3(k = 3, n = 2) == [], 'fails'

    assert sol.combinationSum3(k = 9, n = 45) == [[1,2,3,4,5,6,7,8,9]], 'fails'



if __name__ == '__main__':
   main()