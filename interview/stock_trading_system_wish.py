import unittest
import heapq

"""
use minheap to keep track of remaining open selling orders
use maxheap to keep track of remaining open buy orders

when a buy request come in, try to match it with lowest sell order, either partial or complete fulfill
if there's partial order remaining, add it into buy order heap

when sell request come in, try to match it with highest buy order, either partial or complete fulfill
if there's partial order remaining, add it into sell order heap 
"""
class StockTradingSystem:
    def __init__(self):
        self.buys = []
        self.sells = []

    def buy(self, quantity, price):
        if not self.sells or price < self.sells[0][1]: # no open sell order or no open sell order with same or lower price
            heapq.heappush(self.buys, (quantity, price))
        else:
            while self.sells and price >= self.sells[0][1]:



class StockTradingSystemTest(unittest.TestCase):

    def test_run(self):
        system = StockTradingSystem()
        assert system.sell(50, 1.5) == 0, 'fails'

        assert system.sell(20, 1.4) == 0, 'fails'

        assert system.buy(60, 1.51) == 60, 'fails'

        assert system.buy(20, 1.5) == 10, 'fails'

        assert system.sell(20, 0.7) == 10, 'fails'

        assert system.buy(100, 0.6) == 0, 'fails'

        system = StockTradingSystem()

        assert system.sell(50, 1.5) == 0, 'fails'

        assert system.sell(20, 1.4) == 0, 'fails'

        assert system.buy(60, 1.45) == 20, 'fails' # partial fulfill

        assert system.buy(20, 1.5) == 20, 'fails'


if __name__ == '__main__':
    unittest.main()

