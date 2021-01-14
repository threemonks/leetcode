"""
1654. Minimum Jumps to Reach Home
Medium

A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.



Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
Example 2:

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1
Example 3:

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.


Constraints:

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
All the elements in forbidden are distinct.
Position x is not forbidden.
"""

import collections
import math
from typing import List

"""
BFS求最短路径问题：每到一处新的位置，我们有两种选择，向左走或者向右走。已经走过的地方就标记visited以后不再访问。直至访问到x位置。

BFS search 每次循环，我们遍历所有增加一步所能达到的状态。这样第一次到达终点状态时，必然用了最少的步数。

如果无限制使用朝右走的权利的话，永远不会停止，这样这个队列不会收敛到空。所以我们似乎应该有一个limit，往右边超越这个limit的时候就不该继续走下去。

考虑到有forbidden位置，以及可以先往右超过x或者max(forbidden)然后往左回走到x，取最大探索的右边界点为 max(x, max_forbidden) + b

这样策略是

1. 如果cur <= limit，允许往右移动(前提是不触碰forbidden)
2. 如果到达cur时是右移的，那么允许往左移动（前提是不触碰forbidden且不越过0点）

注意对于每个节点我们需要保存两种visited的状态，记录是从右边来，还是左边来，这个决定下一步可以选择的路径
"""

"""

https://blog.csdn.net/w5688414/article/details/110277961

无论是 bfs 还是 dfs，都按先右移，再左移的操作，进行递归(dfs) 或者进队(bfs)，才能保证能到达目标节点时，步数最少。
防止无限递归是关键，forbidden 中加入右移时遍历到的数据
forbidden中不能加入左移时遍历到的数据，原因是 因为左移后退回cur-b处时，无法覆盖前进到cur-b再后退到cur-2b的情况。

接下来一个比较重要的点是bfs具体处理的细节，感觉这道题目一个比较难处理的点是不能够同时往后跳两步，所以我们在将下一个平行状态加入到队列之前需要判断当前的位置是否是上一次后退得到的位置，
假如不是才能够从当前位置后退b步，这里可以将下一个位置加入到队列的时候进行状态的标记，比如使用字符串或者布尔值标记当前位置到达的下一个位置是否是后退的状态，
并且我们需要使用set集合来记录已经访问过的位置，我感觉在标记已经访问过的位置的时候存在一个很难理解的点就是当后退的时候是不能够使用set集合来标记当前访问过的位置(只能标记前进的位置)，
一开始的时候标记了后退的位置所以导致某些答案是通不过的，这个感觉比较难以理解，我的想法是有可能后退到某一个位置并且标记这个位置了，
下一次前进到这个位置的时候有可能在前进的时候就会通过这个位置在后面的时候到达目标答案，而这个时候被标记了所以下一次到达这个位置的时候就不能够使用这个位置前进到其他的位置了

"""
class Solution0:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden=set(forbidden)
        Q=deque()
        Q.append([0,0,False])
        while Q:
            cur,cnt,used=Q.popleft()
            if(cur==x):
            # 第一次到x即最小步数，因为队列后序元素cnt都是大于等于当前cnt的
                return cnt
            if(cur+a<6000 and cur+a not in forbidden):
            # 6000是往右探索的最大值，x最大为2000
                forbidden.add(cur+a)
                Q.append([cur+a,cnt+1,False])
            if(not used and cur-b>0 and cur-b not in forbidden):
            # 这里不能forbidden，因为后退回cur-b处时，无法覆盖前进到cur-b再后退到cur-2b的情况。
                Q.append([cur-b,cnt+1,True])
        return -1


"""
https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/935419/Python-deque-BFS-O(max(x-max(forbidden))%2Ba%2Bb)
"""
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:

        max_val = max([x] + forbidden) + a + b

        jumps = [0] + [math.inf] * max_val
        for pos in forbidden: jumps[pos] = -1
        queue = collections.deque([0])

        while queue:
            pos = queue.popleft()
            if pos + a <= max_val and jumps[pos + a] > jumps[pos] + 1:
                queue.append(pos + a)
                jumps[pos + a] = jumps[pos] + 1
            if pos - b > 0 and jumps[pos - b] > jumps[pos] + 1:
                jumps[pos - b] = jumps[pos] + 1
                if pos - b + a <= max_val and jumps[pos - b + a] > jumps[pos] + 2:
                    queue.append(pos - b + a)
                    jumps[pos - b + a] = jumps[pos] + 2

        return jumps[x] if jumps[x] < math.inf else -1

"""
BFS search for single source shortest path Shortest path faster algorithm

https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/935419/Python-deque-BFS-O(max(x-max(forbidden))%2Ba%2Bb)

This method does not always push nodes with shorter path into the queue first, so the final output is jumps[x] (which gets updated only if a smaller value is obtained). But it seems we can also  return jumps[x] the first time x is encountered, and it still pass all test cases.

"""
from collections import deque

class Solution2:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0: return 0
        max_val = max([x] + forbidden) + a + b

        jumps = [0] + [math.inf] * max_val
        for pos in forbidden: jumps[pos] = -1
        queue = deque()  # store node, steps, direction
        queue.append(0)

        while queue:
            pos = queue.popleft()
            if pos + a <= max_val and jumps[pos + a] > jumps[pos] + 1:
                # print('pos=%s+a' % pos)
                if pos + a == x: return jumps[pos] + 1
                queue.append(pos + a)
                jumps[pos + a] = jumps[pos] + 1
            if pos - b > 0 and jumps[pos - b] > jumps[pos] + 1:
                # print('pos=%s-b' % pos)
                if pos - b == x: return jumps[pos] + 1
                jumps[pos - b] = jumps[pos] + 1
                if pos - b + a <= max_val and jumps[pos - b + a] > jumps[
                    pos] + 2:  # after jump backward, we can only jump forward, so we just do it instead of adding the previous node to the queue
                    # print('pos=%s-b+a' % pos)
                    if pos - b + a == x: return jumps[pos] + 2
                    queue.append(pos - b + a)
                    jumps[pos - b + a] = jumps[pos] + 2

        # print('get here')
        # print(jumps[x])
        return jumps[x] if jumps[x] < math.inf else -1

"""
BFS search for single source shortest path in unweighted graph

process queue to search one level, add all children to queue, then search next level (all newly added nodes in queue)

with this approach, the first result found is the shortest path because it is unweighted, so path length is the same for all nodes in one level, and we only finish one level completely before proceeding to next level 

consider each jump is going from a graph node to its adjacent node, the jump distance is the weight
terminal condition is node < 0, and we cannot jump to forbidden node, or node value is x
the right side might be going on infinitely, so we need a upper boundary, max(x, max(forbidden))+b, the last '+b' is so that we may need to pass forbidden and come back to go to x

Note we need to have two different visited states for each node, as we cannot go left twice, so the status of a node visited from right is different from the node being visited from left.

https://github.com/wisdompeak/LeetCode/tree/master/BFS/1654.Minimum-Jumps-to-Reach-Home

"""


class Solution3:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0: return 0

        max_right = max(x, max(forbidden)) + b  # maximum right position to check, beyond this the frog cannot come back
        visited = [[0, 0] for _ in range(
            8001)]  # for each node, there's two visited state, one comes from left to right, one comes from right to left

        for f in forbidden:
            visited[f][0] = -1  # to right
            visited[f][1] = -1  # to left

        visited[0][0] = 1

        q = collections.deque()

        q.append((0, 0))  # (node value, previous jump is to left)

        steps = 0
        while q:
            # print('q=%s steps=%s' % (q, steps))
            l = len(q)
            steps += 1
            while l: # finish processing one level before proceeding to next level
                cur, prev_left = q.popleft()
                # print('cur=%s x=%x' % (cur, x))
                if cur == x:
                    return steps
                if cur <= max_right and visited[cur + a][0] == 0:
                    visited[cur + a][0] = 1
                    q.append((cur + a, False))
                    if cur + a == x: return steps
                if prev_left is False:
                    if cur - b >= 0 and visited[cur - b][1] == 0:
                        visited[cur - b][1] = 1
                        q.append((cur - b, True))
                        if cur - b == x: return steps
                l -= 1

        # print('steps=%s' % steps)
        return -1

def main():
    sol = Solution()
    assert sol.minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9) == 3, 'fails'

    assert sol.minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11) == -1, 'fails'

    assert sol.minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7) == 2, 'fails'

    assert sol.minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29, 98, 80) == 121, 'fails'



if __name__ == '__main__':
   main()