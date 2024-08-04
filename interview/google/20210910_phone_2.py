"""
N rooms id 0 to N-1, paitents appointments with start and end, sorted
always assign paient to smallest rooom that is available
find rooms that have maximum appointements (usage count)

thoughts:
use two prioirity queue

empty_room: empty room ids
used_room: used room with ending time, sorting by ending time

for each appointment,
check head of used_room, if the head room's ending time is <= current appointment start, remove this room from used room,
and add it to empty room
then if there's room in empty room, use the smallest room id for this appointment, also record one usages for this room

when done iterating all appointments, check all counts, return room ids with highest counts


time O(M*log(N))

"""
import heapq
from collections import defaultdict
def find_rooms(n, times):
    usage = defaultdict(int)
    empty_room = list(range(n))
    used_room = [] # (ending time, room #)

    for start, end in times:
        while used_room and used_room[0][0] <= start:
            ending, room_id = heapq.heappop(used_room)
            heapq.heappush(empty_room, room_id)

        if empty_room:
            room_id = heapq.heappop(empty_room)
            heapq.heappush(used_room, (end, room_id))
            usage[room_id] += 1
        else:
            return [] # appointment cannot be scheduled

    # get rooms with max usage count
    max_use = 0
    ans = []
    for room_id, count in usage.items():
        if count > max_use:
            max_use = count
            ans = [room_id]
        elif count == max_use:
            ans.append(room_id)

    return ans