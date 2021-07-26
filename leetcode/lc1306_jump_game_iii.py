"""
1306. Jump Game III
Medium

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true
Explanation:
One possible way to reach at index 3 with value 0 is:
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.


Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length

"""
import collections
from typing import List

"""
BFS

time O(N)
space O(N)
"""


class Solution0:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        q = collections.deque()
        q.append(start)
        visited = [0] * n
        visited[start] = 1

        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            if cur + arr[cur] >= 0 and cur + arr[cur] < n and visited[cur + arr[cur]] == 0:
                if arr[cur + arr[cur]] == 0:
                    return True
                visited[cur + arr[cur]] = 1
                q.append(cur + arr[cur])
            if cur - arr[cur] >= 0 and cur - arr[cur] < n and visited[cur - arr[cur]] == 0:
                if arr[cur - arr[cur]] == 0:
                    return True
                visited[cur - arr[cur]] = 1
                q.append(cur - arr[cur])

        return False


"""
DFS recursion without visited, and modifying input arr
"""


class Solution1:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start >= 0 and start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]
            return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False


"""
DFS using stack and visited
"""


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = collections.defaultdict(int)
        stack = []
        stack.append(start)
        while stack:
            cur = stack.pop()
            if arr[cur] == 0:
                return True
            visited[cur] = 1
            if cur + arr[cur] >= 0 and cur + arr[cur] < len(arr) and visited[cur + arr[cur]] == 0:
                stack.append(cur + arr[cur])
            if cur - arr[cur] >= 0 and cur - arr[cur] < len(arr) and visited[cur - arr[cur]] == 0:
                stack.append(cur - arr[cur])

        return False


def main():
    sol = Solution()
    assert sol.canReach(arr = [4,2,3,0,3,1,2], start = 5) is True, 'fails'

    assert sol.canReach(arr = [4,2,3,0,3,1,2], start = 0) is True, 'fails'

    assert sol.canReach(arr = [3,0,2,1,2], start = 2) is False, 'fails'

if __name__ == '__main__':
   main()