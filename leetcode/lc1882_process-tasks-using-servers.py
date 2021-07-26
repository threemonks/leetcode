"""
1882. Process Tasks Using Servers
Medium

8

7

Add to List

Share
You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

You are running a simulation system that will shut down after all tasks are processed. Each server can only process one task at a time. You will be able to process the jth task starting from the jth second beginning with the 0th task at second 0. To process task j, you assign it to the server with the smallest weight that is free, and in case of a tie, choose the server with the smallest index. If a free server gets assigned task j at second t,​​​​​​ it will be free again at the second t + tasks[j].

If there are no free servers, you must wait until one is free and execute the free tasks as soon as possible. If multiple tasks need to be assigned, assign them in order of increasing index.

You may assign multiple tasks at the same second if there are multiple free servers.

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

Return the array ans​​​​.



Example 1:

Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
Example 2:

Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4.
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9.
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.


Constraints:

servers.length == n
tasks.length == m
1 <= n, m <= 2 * 10^5
1 <= servers[i], tasks[j] <= 2 * 10^5
"""
import heapq
from typing import List

"""
Heap

two pq, one for free servers, one for running servers

steps:

for each tasks (in ascending order of start time):
    if this task is not ready to run (curtime < task start time):
        increase curtime to task start time
    if no available server:
        increase curtime to time of first finish time of all running ones
    while running and finish time of running < curtime:
        pop one running server, push it into available server
    remove one available server
    start this task on this server
    push this sever onto running queue

time O(m+nlog(m)) - m is # of servers, n is # of tasks
"""


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        m, n = len(servers), len(tasks)

        idle_servers = []  # free server q (weight, server index)
        for i, w in enumerate(servers):
            heapq.heappush(idle_servers, (w, i))

        running = []  # running server q (endtime, index)

        ans = []
        curtime = 0
        for j, task in enumerate(tasks):
            # if curtime is behind task index j, we have no task to schedule, move time forward
            curtime = max(j, curtime)

            # if no idle server available, jump time to next job end time
            if not idle_servers:
                curtime = running[0][0]

            # free servers where job has ended by now
            while running and running[0][0] <= curtime:
                endtime, si = heapq.heappop(running)
                heapq.heappush(idle_servers, (servers[si], si))

            # print('j=%s task=%s curtime=%s idle_servers=%s running=%s ans=%s' % (j, task, curtime, idle_servers, running, ans))
            # add this task to idle server
            sw, si = heapq.heappop(idle_servers)
            ans.append(si)
            heapq.heappush(running, (curtime + tasks[j], si))

        return ans

def main():
    sol = Solution()
    assert sol.assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]) == [2,2,0,2,1,2], 'fails'

    assert sol.assignTasks(servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]) == [1,4,1,4,1,3,2], 'fails'

if __name__ == '__main__':
   main()