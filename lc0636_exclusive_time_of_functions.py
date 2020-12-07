"""
636. Exclusive Time of Functions
Medium

On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.



Example 1:


Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
Example 2:

Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Output: [8]
Explanation:
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls itself again.
Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
Example 3:

Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
Output: [7,1]
Explanation:
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls function 1.
Function 1 starts at the beginning of time 6, executes 1 units of time, and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.
Example 4:

Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
Output: [8,1]
Example 5:

Input: n = 1, logs = ["0:start:0","0:end:0"]
Output: [1]


Constraints:

1 <= n <= 100
1 <= logs.length <= 500
0 <= function_id < n
0 <= timestamp <= 109
No two start events will happen at the same timestamp.
No two end events will happen at the same timestamp.
Each function has an "end" log for each "start" log.

"""
from typing import List

"""
use stack to track function call stack, also keep track of current function in execution, and its effective start time
when a new function starts, we push it into stack, the previous cur_fn stops, and this new function becomes cur_fn, with current ts as cur_start
when a function stops, we pop it off the stack, it must match cur_fn, and its duration is from cur_start to current ts, and next stack top becomes cur_fn, and it starts at current ts+1

time O(N)
space O(N)
 
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        fn_duration = [0] * n
        fn_actions = []
        for log in logs:
            fn, action, ts = log.split(':')
            fn_actions.append((int(fn), action, int(ts)))

        cur_fn = -1
        cur_start = 0

        # sort fn_actions by timestamp
        fn_actions = sorted(fn_actions, key=lambda x: x[2])
        for i, fa in enumerate(fn_actions):
            fn, action, ts = fa
            if action == 'start':
                if stack:
                    if cur_fn >= 0:
                        fn_duration[cur_fn] += ts - cur_start
                        # print('fn_duration=%s' % str(fn_duration))
                stack.append(fn)
                cur_fn = fn
                cur_start = ts
                # print('cur_fn=%s cur_start=%s' % (cur_fn, cur_start))
                # print('stack=%s' % str(stack))
            elif action == 'end':
                t = stack.pop(-1)
                # print('stack=%s' % str(stack))
                if t == fn:
                    assert fn == cur_fn, "fn == cur_fn fails"
                    fn_duration[cur_fn] += ts - cur_start + 1
                    # print('fn_duration=%s' % str(fn_duration))
                    if stack:
                        cur_fn = stack[-1]
                        cur_start = ts + 1  # new func starts at next timestamp
                        # print('cur_fn=%s cur_start=%s' % (cur_fn, cur_start))
                else:
                    # print('unexpcted pop function call %s' % fn)
                    pass

        # print('fn_duration=%s' % str(fn_duration))
        return fn_duration


# 0 start 0, 0 end 5, 1 start 6, 1 end 6, 2 start 7, 2 end 9, 2 start 10, 2 end 13
# 0 0-5 6
# 1 6 1
# 2 7 - 9 3
# 2 10 -13 4 => 7

def main():
    sol = Solution()
    assert sol.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]) == [3,4], 'fails'

    assert sol.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]) == [8], 'fails'

    assert sol.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]) == [7, 1], 'fails'

    assert sol.exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]) == [8, 1], 'fails'

    assert sol.exclusiveTime(1, ["0:start:0","0:end:0"]) == [1], 'fails'

    assert sol.exclusiveTime(3, ["0:start:0","0:end:5","1:start:6","1:end:6","2:start:7","2:end:9","2:start:10","2:end:13"]) == [6,1,7], 'fails'

if __name__ == '__main__':
   main()