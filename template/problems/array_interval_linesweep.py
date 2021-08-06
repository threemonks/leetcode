# interval_a, interval_b
interval_a = [2, 5]
interval_b = [4, 7]

low = max(interval_a[0], interval_b[0])
high = min(interval_a[1], interval_b[1])

if low <= high:
    overlap = [low, high]
    overlap[0] = max(interval_a[0], interval_b[0])
    overlap[1] = min(interval_a[1], interval_b[1])

    merged = [None, None]
    merged[0] = min(interval_a[0], interval_b[0])
    merged[1] = max(interval_a[1], interval_b[1])

# 问题要求只和区间本身有关的问题 - 可以仅从start_idx和end_idx就可以知晓的（区间index，或区间长度，或区间是否存在的问题）。
# 首先sort所有的interval，维护一个window变量代表当前所求的时间窗口，然后每个interval的开始和结束，要么close当前的window新建一个新window，要么是延伸当前的window或推迟将来的window。

# list of intervals merge
def merge(intervals):
    if len(intervals) == 0:
        return []

    intervals = sorted(intervals) # sort by start time

    output = []
    window = intervals[0]

    for idx in range(1, len(intervals)):
        interval = intervals[idx]
        # has no overlap
        if window[1] < interval[0]:
            output.append(window)
            window = interval

        window[1] = max(window[1], interval[1])

    # last window
    output.append(window)
    return output

# 问题要求只和区间本身有关的问题（区间index，或区间长度，或区间是否存在的问题）
# 首先sort所有的interval，将每个interval拆解成两个event，这些event会影响整个program的某些状态，比如 overlap_count，然后按照时间序遍历所有event，根据event来open和close window，然后判断window和状态变量是否满足所需的条件。


"""
minheap
"""
# 253. Meeting Rooms II
# sort all meeting by start time, use priorityqueue to keep track of rooms being used identified by ending time
# for each new meeting check any room (in priorityqueue) has ended or not, if so, replace its ending time
# if not, add a new room with this new ending time
import heapq
def minMeetingRooms(intervals):
    rooms = [] # priorityqueue stores room ending time
    heapq.heapify(rooms)

    for interval in sorted(intervals):
        if rooms and rooms[-1] < interval[0]: # can reuse room, update its ending time
            heapq.heapreplace(rooms, interval[1])
        else: # new room
            heapq.heappush(rooms, interval[1])

    return len(rooms)

"""
Interval / Line Sweep => max concurrent rooms 
"""
# 253. Meeting Rooms II
# Chronological Ordering of all events (start time, increase room count, end time, decrease room count) 
# separate each meeting's start and end to separate event, start time cause room count increase by 1
# end time cause room count decrease by 1
# for each event, increase or decrease room count accordingly
# keep track of max room count globally

def minMeetingRooms(intervals):
    ans = 0
    events = [(interval[0], 1) for interval in intervals]
    events += [(interval[1], -1) for interval in intervals]
    rooms = 0
    for event in sorted(events): # this sort result in room count decreases first if both increase and decrease happen at same time
        rooms += event[1]
        ans = max(ans, rooms)

    return ans
