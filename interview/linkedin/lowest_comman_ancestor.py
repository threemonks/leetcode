2
"""
The lowest common ancestor is defined between two nodes v and w as the lowest node in a tree that has both v and w as descendants (where we allow a node to be a descendant of itself).
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.


Given the following Binary Search Tree:
                10
               /  \
              5    20
             /\    /\
            1  6  15 30
                \
                 7
The lowest common ancestor of node 1 and 7 is 5.
The lowest common ancestor of node 1 and 5 is 5.

time O(V) V- # of nodes
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # TreeNode
        self.right = None  # TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    path1 = []
    path2 = []

    def dfs(node, path):
        nonlocal path1, path2
        if node.val == p.val:
            path1 = path[:]
            return
        elif node.val == q.val:
            path2 = path[:]

        if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
            return

        if node.left and not (p.val > node.val and q.val > node.val):
            dfs(node.left, path + [node.left])
        if node.right and not (p.val < node.val and q.val < node.val):
            dfs(node.right, path + [node.right])

    dfs(root)

    m, n = len(path1), len(path2)
    ans = root
    for i in range(min(m, n)):
        if path1[i].val == path2[i].val:
            ans = path1[i]
        else:
            break

    return ans


"""
public interface Intervals {

    /**
     * Adds an interval [from, to) into an internal structure.
     */
    void addInterval(int from, int to);

    /**
     * Returns a total length covered by the added intervals.
     * If several intervals intersect, the intersection should be counted only once.
     * Example:
     *
     * addInterval(3, 6)
     * addInterval(8, 9)
     * addInterval(1, 5)
     *
     * getTotalCoveredLength() -> 6
     *
     * i.e. [1,5) and [3,6) intersect and give a total covered interval [1,6) with a length of 5.
     *      [1,6) and [8,9) don't intersect, so the total covered length is a sum of both intervals, that is 5+1=6.
     *
     *          |__|__|__|                  (3,6)
     *                         |__|         (8,9)
     *    |__|__|__|__|                     (1,5)
     *
     * 0  1  2  3  4  5  6  7  8  9  10
     *
     */
    int getTotalCoveredLength();

}

time O(NlogN)
 get O(N)
"""


class Intervals:
    def __init__(self):
        self.intervals = []  # sorted, no overlap

    def addIntervals0(self, a, b):
        if not self.intervals:
            self.intervals.append([a, b])
        else:
            new_intervals = self.intervals + [[a, b]]
            sorted_intervals = []
            for interval in sorted(new_intervals):
                if interval[0] <= sorted_intervals[-1][1]:
                    sorted_intervals[-1][1] = max(sorted_intervals[-1][1], interval[1])
                else:
                    sorted_intervals.append(interval)

            self.intervals = sorted_intervals[:]

    def addIntervals(self, a, b):
        if not self.intervals:
            self.intervals.append([a, b])
        else:
            cur_interval = [a, b]
            new_intervals = []
            for interval in self.intervals:
                if cur_interval[0] > interval[1]:
                    new_intervals.append(interval)
                elif cur_interval[1] < interval[0]:
                    if cur_interval[0] > new_intervals[-1][1]:
                        new_intervals.append(cur_interval)
                    else:
                        new_intervals[-1][1] = max(new_intervals[-1][1], cur_interval[1])
                    cur_interval = interval[:]
                else:
                    cur_interval[1] = max(cur_interval[1], interval[1])

            if cur_interval[0] > new_intervals[-1][1]:
                new_intervals.append(cur_interval)
            else:
                new_intervals[-1][1] = max(new_intervals[-1][1], cur_interval[1])

            self.intervals = new_intervals[:]

    def getTotalCoveredLength(self):
        ans = 0
        for interval in self.intervals:
            ans += interval[1] - interval[0]

        return ans

