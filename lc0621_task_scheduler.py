"""
621. Task Scheduler
Medium

https://leetcode.com/problems/task-scheduler/
"""
from typing import List
from collections import Counter
import heapq

"""
Priority Queue

basic idea:
1 use priority queue to store -count, task
2. for n times (cooling period), take most freq task from queue, schedule it, put into tempq if there's remaining count
3. at end of n time or until queue is empty, put all items in tempq back into queue
4. repeat from 2 until queue is empty

since we always wait for cooling down period, before we put items from tempq back into queue, so we know all items in tempq have experienced enough cooling down period before they will be at the head of q for scheduling again, thus we don't need to keep track of last run time of given task in queue

Mistakes:

1, heapq stores (-count, task, lasttime), note it is -count, as heapq is minheap
2. cpu idle (res += 1) even when all tasks in heapq are checked but none can be scheduled due to cool down restriction
3. we don't need to scan entire queue to check each task, if valid, schedule and put into tempq if there's count left, and merge tempq back into queue after we finish scan entire queue
    instead, one could just process task from head of queue for n times, store ones with remaining count into tempq, then at end of n times (cooling down period), we put all tasks from tempq back into queue, this guarantees any tasks we put back into queue would have waited at least n time when they are next scheduled from queue - the first one (with most count) would have waited n times when put back into queue, and the next most freq one would also have waited n times when it is scheduled after the first one

Note: task name is not necessary in Queue

"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        # print(task_count)

        q = []
        heapq.heapify(q)

        for task, count in task_count.items():
            heapq.heappush(q, (-count, task))  # -count, taskname

        res = 0
        while q:
            i, tempq = 0, []
            while i <= n:  # if still within cooling down period, we try to execute more items from pq
                res += 1
                if q:
                    count, task = heapq.heappop(q)

                    # if this task has not cooled enough, put it into a tempq
                    # which will be put back into heapq after this cooling down period ends
                    if count != -1:
                        tempq.append((count + 1, task))

                if not q and not tempq:  # if both q and tempq are empty, we are done
                    break
                else:
                    i += 1

            # at end of this cooling down period
            # if there's any task in tempq that we could not run, we need to put back into queue
            for t in tempq:
                heapq.heappush(q, t)

        return res

def main():
    sol = Solution()
    assert sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2) == 8, 'fails'

    assert sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0) == 6, 'fails'

    assert sol.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2) == 16, 'fails'

if __name__ == '__main__':
   main()