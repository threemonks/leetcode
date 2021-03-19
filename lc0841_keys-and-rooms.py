"""
841. Keys and Rooms
Medium

"""
from collections import deque
from typing import List

"""
Graph / BFS

start with all rooms whose key are in room 0, put all these key's corresponding room to queue as start source
start from any of these source, mark node as visited as we traverse

When done, compare # of visited nodes vs total number of rooms

"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = set([0])
        for key in list(rooms[0]):
            visited.add(key)

        q = deque(list(rooms[0]))

        while q:
            cur = q.popleft()
            for key in rooms[cur]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)
                    # print(key)

        # print(visited)
        if len(visited) == len(rooms):
            return True
        else:
            return False

def main():
    sol = Solution()
    assert sol.canVisitAllRooms([[1],[2],[3],[]]) is True, 'fails'

    assert sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) is False, 'fails'

if __name__ == '__main__':
   main()