"""
582. Kill Process
Medium

702

14

Add to List

Share
You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.



Example 1:


Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that should be killed.
Example 2:

Input: pid = [1], ppid = [0], kill = 1
Output: [1]


Constraints:

n == pid.length
n == ppid.length
1 <= n <= 5 * 10^4
1 <= pid[i] <= 5 * 10^4
0 <= ppid[i] <= 5 * 10^4
Only one process has no parent.
All the values of pid are unique.
kill is guaranteed to be in pid.
"""
from typing import List
from collections import defaultdict
"""
DFS tree traverse

time O(N) all node are processed once and only once
space O(N) map and stack
"""

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)

        parent = dict(zip(pid, ppid))

        for pid, ppid in parent.items():
            children[ppid].append(pid)

        stack = [kill]
        ans = []

        while stack:
            cur = stack.pop()
            if cur in children:
                for child in children[cur]:
                    stack.append(child)
            ans.append(cur)

        return ans


def main():
    sol = Solution()
    assert sol.killProcess(pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5) == [5, 10], 'fails'

    assert sol.killProcess(pid = [1], ppid = [0], kill = 1) == [1], 'fails'


if __name__ == '__main__':
   main()