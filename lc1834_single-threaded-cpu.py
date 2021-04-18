"""
1834. Single-Threaded CPU
Medium

36

37

Add to List

Share
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.



Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows:
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.


Constraints:

tasks.length == n
1 <= n <= 10^5
1 <= enqueueTimei, processingTimei <= 10^9

"""
from typing import List
import heapq

"""
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
time 1 available {0}
       start {0}
time 2 available {1}
time 3 available {1, 2} <= heap [(processing time, index)]
       finish {0}
       start 

"""
"""
Heap

sort tasks (along with original index) by enque time because tasks can be put into available queue only when its enque time passed current time

at each timestamp, enque all tasks whose enque task <= current time, store (processtime, index) into heap, so that we process task with shorter processtime first (if same process time, small index first)

with each task starts, jump timestamp to when the task will finish, as cpu will be busy and won't process anything until it is done, so there's no need to enque any task before cpu is done and can check available task from heap again

if no task available, then jump timestamp to the enque time of next task that will be enqued

"""
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = sorted(
            [task[0], task[1], idx] for idx, task in enumerate(tasks))  # task with index, and sorted by enque time
        # print('tasks sorted=%s' % tasks)
        available = []
        ans = []
        idx = 0  # index of current task checked
        i = tasks[0][0]  # time start at first task enque time
        while available or idx < n:
            # print('i=%s' % i)
            while idx < n and tasks[idx][0] <= i:
                # print('idx=%s task=%s' % (idx, tasks[idx]))
                heapq.heappush(available, [tasks[idx][1], tasks[idx][2]])  # (processing time, index)
                idx += 1
            if available:
                processtime, index = heapq.heappop(available)
                ans.append(index)
                i += processtime  # next time cpu finishes task and will check new task
            else:  # no available task, jump to next none queued task
                if idx < n:
                    i = tasks[idx][0]
                else:
                    i += 1

        return ans

def main():
    sol = Solution()

    assert sol.getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]) == [0,2,3,1], 'fails'

    assert sol.getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]) == [4,3,2,0,1], 'fails'


if __name__ == '__main__':
   main()