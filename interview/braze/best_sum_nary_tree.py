"""

Best Sum Any Tree Path

Given a tree rooted at node 0, and a value assigned to each node, determine the maximum sum of the values along path in the tree. The path sum must not be empty, and in somecases
it might not go through the root. The following tree (labeled node number/value) is analyzed below.

    /- 1/7 - 2/-10 - 3/4
0/5
    \ 4/15

Two of the possible paths are 4 -> 0 -> 1 -> 2 ->3 which has a sum of 15+5+7+-1+4=21
and 1->2->3 with a sum of 7+-10=1, and a third possible path, the maximum sum path is 4->0->1 with a sum of
15+5+7=27

constraints
1<=n<=10^5
parent[0] = -1
0<=parent[i]<n for 1<=i<n
-1000 <= values[i]<= 1000
the parent array defines a valid tree

"""
from typing import List


class Solution:
	def bestSumAnyTreePath(self, n: int, parent: List, values:List):
		"""
		n: the number of nodes in the tree
		parent[parent[0]...parent[n-1]]: integer array where parent[i]=j means the node j is a parent of node i, parent[0] is set to -1 to indacate node 0 is root
		values[values[0]...values[n-1]]: integer array where values[i] denotes the value of node i
		"""


