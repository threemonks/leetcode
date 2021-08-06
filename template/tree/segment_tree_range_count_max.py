import math


class Node:
    # Segment Tree for range max query
    # half-open inteval [lo, hi)
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.val = val # range max
        self.left = None
        self.right = None


class SegmentTree:
    """
    Segment Tree for range count max
    """
    def __init__(self, intervals):
        self.root = Node(0, 10**9+1) # index min and max
        for start, end in intervals:
            self.update(self.root, start, end)

    def build_tree(self, nums, start, end):
        if start > end:  # nothing to build
            return None
        node = Node(start, end)
        if start == end:
            node.sum = nums[start]
        else:  # split and call build_tree on left and right range recursively
            mid = start + (end - start) // 2
            node.left = self.build_tree(nums, start, mid)
            node.right = self.build_tree(nums, mid + 1, end)
            node.sum = node.left.sum + node.right.sum
        return node

        self.update(self.root, start, end - 1)

    def query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.val
        mid = node.start + (node.end - node.start) // 2
        res = -math.inf
        if not node.left:
            node.left = Node(node.start, mid, node.val)
        if not node.right:
            node.right = Node(mid + 1, node.end, node.val)

        if start <= mid:
            res = max(res, self.query(node.left, start, end))
        if end > mid:
            res = max(res, self.query(node.right, start, end))

        return res

    def update(self, node, start, end):
        # for each events [start, end), bookings+1
        # we should update all related nodes to maintain max bookings for [start, end)
        # time O(N*log(N))
        # spance O(N)
        if start <= node.start and node.end <= end:
            node.val += 1
            if node.left:
                self.update(node.left, start, end)
            if node.right:
                self.update(node.right, start, end)
            return

        # update left and right recursively
        mid = node.start + (node.end - node.start) // 2
        if not node.left:
            node.left = Node(node.start, mid, node.val)
        if not node.right:
            node.right = Node(mid + 1, node.end, node.val)
        if start <= mid:
            self.update(node.left, start, end)
        if end > mid:
            self.update(node.right, start, end)

        node.val = max(node.left.val, node.right.val)