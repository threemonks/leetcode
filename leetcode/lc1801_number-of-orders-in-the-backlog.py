"""
1801. Number of Orders in the Backlog
Medium
"""
import heapq
from typing import List

"""
Greedy / Heap

buy backlog heap sort by price (-price because we only have minheap)
sell backlog heap sort by price

mistakes:
1. after partial fulfill on multiple sell orders, we might still have buy order left, so need to use while loop buy_amount > 0
"""


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        buylog = []  # use negative price in buylog since python has only minheap, and for buyoffer, we match buyer with higher price first
        selllog = []

        for i, (price, amount, order_type) in enumerate(orders):
            # print('i=%s price=%s amount=%s order_type=%s' % (i, price, amount, order_type))
            if order_type == 0:  # buy
                while amount > 0:
                    if not selllog:
                        break
                    # execute some orders
                    sellprice, sellamount = heapq.heappop(selllog)
                    if sellprice > price:
                        heapq.heappush(selllog, (sellprice, sellamount))
                        break
                    if sellamount > amount:  # fully match, with some sell order amount remains
                        heapq.heappush(selllog, (sellprice, sellamount - amount))
                    amount = amount - sellamount
                # if any amount remains, add to buy log
                if amount > 0:
                    heapq.heappush(buylog, (-price, amount))
            elif order_type == 1:  # sell
                while amount > 0:
                    if not buylog:
                        break
                    buyprice, buyamount = heapq.heappop(buylog)
                    buyprice *= -1
                    if buyprice < price:
                        heapq.heappush(buylog, (-buyprice, buyamount))
                        break
                    # execute some orders
                    if buyamount > amount:  # fully match, with some buy order amount remains
                        heapq.heappush(buylog, (-buyprice, buyamount - amount))
                    amount = amount - buyamount
                if amount > 0:  # any amount remains, add to sell log
                    heapq.heappush(selllog, (price, amount))
            # print('i=%s backlog orders=%s' % (i, sum([bl[1] for bl in buylog]) + sum([sl[1] for sl in selllog])))

        # once done, check total remaining orders
        return (sum([bl[1] for bl in buylog]) + sum([sl[1] for sl in selllog])) % MOD


def main():
    sol = Solution()
    assert sol.getNumberOfBacklogOrders(orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]) == 6, 'fails'

    assert sol.getNumberOfBacklogOrders(orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]) == 999999984, 'fails'



if __name__ == '__main__':
   main()