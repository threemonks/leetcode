"""
901. Online Stock Span
Medium

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].



Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation:
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.


Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
"""
"""
Stack
observation using stack
push into (stack, spanner) if price lower than top of stack, if higher, calculate spanner by accumulating smaller numbers (associated spanners) popped out.
"""
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            p, s = self.stack.pop(-1)
            span += s
        self.stack.append((price, span))
        return span

def main():
    sol = StockSpanner()
    assert sol.next(100) == 1, 'fails'
    assert sol.next(80) == 1, 'fails'
    assert sol.next(60) == 1, 'fails'
    assert sol.next(70) == 2, 'fails'
    assert sol.next(60) == 1, 'fails'
    assert sol.next(75) == 4, 'fails'
    assert sol.next(85) == 6, 'fails'

if __name__ == '__main__':
   main()