"""
Interval scheduling maximization

- sort interval by end time, greedily take next interval with smallest ending, if its start does not overlap with previous end
https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
"""

def interval_schedule(intervals):
    intervals.sort(key=lambda x: (x[1], x[0]))  # sort by end first, then start

    # maximum interval scheduling, greedily take the next one with smallest ending time,
    # if its start does not overlap with previous ending
    res, prev_end = [], -1
    for start, end in intervals:
        if start > prev_end:  # next smallest ending interval's start does not overlap with previous ending
            res.append((start, end))  # add to result
            prev_end = end  # update previous ending

    return res

