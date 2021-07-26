"""
1311. Get Watched Videos by Your Friends
Medium

There are n people, each person has a unique id between 0 and n-1. Given the arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list of friends respectively for the person with id = i.

Level 1 of videos are all watched videos by your friends, level 2 of videos are all watched videos by the friends of your friends and so on. In general, the level k of videos are all watched videos by people with the shortest path exactly equal to k with you. Given your id and the level of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest.



Example 1:



Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
Output: ["B","C"]
Explanation:
You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with id = 1 -> watchedVideos = ["C"]
Person with id = 2 -> watchedVideos = ["B","C"]
The frequencies of watchedVideos by your friends are:
B -> 1
C -> 2
Example 2:



Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
Output: ["D"]
Explanation:
You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).


Constraints:

n == watchedVideos.length == friends.length
2 <= n <= 100
1 <= watchedVideos[i].length <= 100
1 <= watchedVideos[i][j].length <= 8
0 <= friends[i].length < n
0 <= friends[i][j] < n
0 <= id < n
1 <= level < n
if friends[i] contains j, then friends[j] contains i

"""
import collections
from typing import List

"""
use BFS to get only friends on level level, and get list of videos from them, and frequency the video shows up
Note: a person cannot be revisited unless we are on a shorter path to this person.
"""


class Solution0:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], pid: int, level: int) -> \
    List[str]:

        q = collections.deque()
        q.append((pid, 0))
        visited = collections.defaultdict(int)
        visited[pid] += 0

        wvs = collections.defaultdict(int)

        while q:
            cur, curlevel = q.popleft()
            if curlevel == level:
                # collect videos
                for wv in watchedVideos[cur]:
                    wvs[wv] += 1
            for f in friends[cur]:
                if f not in visited or curlevel + 1 < visited[f]:
                    q.append((f, curlevel + 1))
                    visited[f] = curlevel + 1

        wvs_sorted = sorted(wvs.items(), key=lambda x: (x[1], x[0]))

        return [v[0] for v in wvs_sorted]


"""
use BFS to get only friends on level level, and get list of videos from them, and frequency the video shows up
process one level at a time 
"""


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], pid: int, level: int) -> \
    List[str]:

        q = collections.deque()
        q.append(pid)
        visited = set()
        visited.add(pid)

        wvs = collections.defaultdict(int)

        lvl = 0
        while q:
            l = len(q)
            while l:
                cur = q.popleft()
                if lvl == level:
                    # collect videos
                    for wv in watchedVideos[cur]:
                        wvs[wv] += 1
                for f in friends[cur]:
                    if f not in visited:
                        q.append(f)
                        visited.add(f)
                l -= 1
            lvl += 1

        wvs_sorted = sorted(wvs.items(), key=lambda x: (x[1], x[0]))

        return [v[0] for v in wvs_sorted]

def main():
    sol = Solution()
    assert sol.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1) == ["B","C"], 'fails'

    assert sol.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2) == ["D"], 'fails'


if __name__ == '__main__':
   main()