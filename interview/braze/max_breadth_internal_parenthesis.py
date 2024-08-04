"""

for a string S with valid parantheses, return the max breath of the internal parantheses.

For ex :
Input - (()()) - return 2 since the inside is ()().
((()()))(()()()()) - returns 4.

Any thoughts on this problem would be most beneficial for the future.

Maximum Breadth of Parentheses。这道题我在lc上面找不到，不过和上一题差不多，不过这次要找的是maximum breadth。
花了一点时间去理解这里的breadth是什么，后面发现是同一个括号里、同样depth的括号的数量。()()()的maximum breadth是3，(()())是2，(()())(())同样是2。
这道题有些tricky，论难度应该可以到medium水平。
一开始想到了在遍历string的时候用一个int array去存储在当前的iteration里layer为i的括号有多少个 (arr[0]记载了当前depth为0的括号有多少），
最后return它的maximum就好。我一开始自己写的testcase都过了，不过最后hr给了我这个testcase：(()())(())后才发现我在出一个括号的时候没有清除array里面对应depth的数量，
导致前面大括号里面的两个小括号在我遍历到后面大括号的时候也给算进去了。脑子当时卡壳了不知道在哪清，最后在面试结束前一刹那才realize在iterate到右括号的时候清就完事，
加一行码跑过了testcase惊险做完。最后留了五分钟问question‍‌‍‌‌‌‌‌‍‌‍‌‍‌‌‌‌‌‌‍，我question问完后说等等我想到咋做了加一行码跑过以后大家都笑了哈哈，空气中充满了快活的气氛！

"""
from typing import List

class Solution:
	def max_breadth(self, s):
		"""
		n: the number of nodes in the tree
		parent[parent[0]...parent[n-1]]: integer array where parent[i]=j means the node j is a parent of node i, parent[0] is set to -1 to indacate node 0 is root
		values[values[0]...values[n-1]]: integer array where values[i] denotes the value of node i
		"""
		stack = []
		width = []

		ans = 0
		for c in s:
			if c == '(':
				level = len(stack)
				stack.append(c)
				if level >= len(width):
					width += [1]
				else:
					width[level] += 1
				ans = max(ans, width[level])
			elif c == ')':
				stack.pop()
				width = width[:len(stack)+1] # drop counts for deeper level

		return ans


def main():
	sol = Solution()
	assert sol.max_breadth('(()())') == 2, 'fails'

	assert sol.max_breadth('(()()()())((()()))') == 4, 'fails'


if __name__ == '__main__':
	main()

