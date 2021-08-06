"""
Fenwick / Binary Index Tree (BIT) 树状数组

https://leetcode.com/discuss/general-discussion/1093346/introduction-to-fenwick-treebinary-indexed-treebit

A BIT essentially works with cumulative quantities.
Each node of the Binary Indexed Tree stores the sum of some elements of the input array.

If there are multiple single value update, and multiple range sum queries, Fenwick trees (BIT) solve this problem as it takes O(logn) time for both updates and finding range sum

http://www.phillypham.com/Fenwick%20Trees%20and%20Two%27s%20Complement

              0
	/		  |                \
0001(1) 0010(2) 0100(4)         1000(8)
[1,1]   [1,2]   [1,4]           [1,8]
            |     |    \           |             \
        0011(3) 0101(5) 0110(6) 1001(9) 1010(10) 1100(12)
        [3,3]   [5,5]   [5,6]   [9,9]   [9,10]   [9,12]
		                 |               |        |       \
						0111(7)         1011(11) 1101(13) 1110(14)
						[7,7]           [11,11]  [13,13]  [13,14]
						                                   |
														  1111(15)
														  [15,15]

update:
	i += lowbit(i), i<=n
query => presum(0, i):
	i -= lowbit(i), i>0

"""
class FenWickTree:
    def __init__(self, n):
        self._sums = [0] * (n+1) # note index i is 1-based

    def prefix_sum(self, i): # this sums from elements from 1, 2, ..., i # could also implement i+1 here, so that calling this function can still be 0-based, so it is consistent with input array size n
        i += 1
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= self._lowbit(i) # remove lowbit, 1011 (13) => 1010 (10) => 1000 (8), from 13 to 10 to 8, go to parent node
        return s

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left-1)

    def add(self, i, delta): # note index i is 1-based
        """
        add delta onto index i
        :param i:
        :param delta:
        :return:
        """
        i += 1
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i) # add lowbit, 1001 (9) => 1010 (10) => 1100 (12), from 9 to 10 to 12 (right sibling)

    def _lowbit(self, x):
        return x & (-x)

"""
initialize with array
"""
class FenWickTree1:
    def __init__(self, nums):
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.update(i, num) # initially, num == delta