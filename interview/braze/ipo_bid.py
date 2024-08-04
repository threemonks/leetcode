"""

A company IPO
bids arrive from users in the form of <userid, number of shares, bidding price, timestamp> until the bidding window is closed
the auction logic assigns shares to biders as follows
1. the ibdder with the highest price gets the number of shares they bid for
2. if multiple bidders have bid a the same price, the bidders are assigned shares in the order in which they placed their bids earliest bids first

list the user ids' of all users who did not get even one share after the shares have been allocated
eg.
bids = [1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]]
total shares = 10 to allocate, the highest price bid is for user id 2 for 7 shares at a price of 8, so that user gets 7 shares, leaving 11 to allocate to lower prices.
Users with ids 1 and 3 each bid 5 for 5 and 7 shares, with bidder 1 having the earlier timestamp. Bidder 1 has the full allotment. Bidder 3 has
2 more shares to buy. And there is 1 share left to allocate. It goes to bidder 3 and all shares have been allocated. Bidder 4 is the only bidder who gets no shares.

"""
from typing import List

"""
Greedy

sort by price, than timestamp, store into heap

while remainshares > 0:
    pop one bid

"""


class Solution:
	def getUnallottedUsers(self, bids: List[List[int]], totalShares:int) -> List[List[int]]:
        pass

def main():
    sol = Solution()
    assert sol.groupStrings(strings = ["abc","bcd","acef","xyz","az","ba","a","z"]) == [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']], 'fails'

    assert sol.groupStrings(strings = ["a"]) == [["a"]], 'fails'


if __name__ == '__main__':
   main()
