"""
Stock Market Prediction
first player gives the second player some stock market data for some consecutive days. The data contains a company's stock price on each day. The rule for the game is:
* player 1 will tell player 2 a day number and player 2 has to find the nearest day on which a stock price is smaller than the given day.
* if there are two results, then player 2 has to find the day number which is smaller and if no such day exists, then return -1

constraints:
1<=n<=10^5
1<=stockData[i]<=10^9
1<=q<=10^5
1<=queries[i]<=10^9

sample input
10, 5, 6, 8, 4, 9, 10, 8, 3, 6, 4, 3

3, 1, 8

output

2, 4, -1



Same as find next smaller element in array
Given an array, find out the next smaller element for each element

Given an array find the next smaller element in array for each element without changing the original order of the elements.

For example, suppose the given array is 4,2,1,5,3.

The resultant array would be 2,1,-1,3,-1.

https://stackoverflow.com/questions/9493853/given-an-array-find-out-the-next-smaller-element-for-each-element


"""
from typing import List

"""
MonoStack
idea is to use Monotonic stack to find next smaller on left, and next smaller on right for each element
then pick the one that is closer to the element in another run.
 
"""

class Solution:
	def predictAnswer(self, stockData: List, queries: List):
		"""
		stockData: array of n integers, where stockData[i] is stock price on i-th day (0 based)
		queries: array of q integers, value being day number given in the query 0<=i<q
		"""
		pass

