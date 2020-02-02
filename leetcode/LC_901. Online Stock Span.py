class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        totCount = 1
        while self.stack and self.stack[-1][0] <= price:
            _, count = self.stack.pop()
            totCount += count
        self.stack.append((price, totCount))
        return totCount


'''
For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

'''
# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
prices = [100, 80, 60, 70, 60, 75, 85]
for price in prices:
    param = obj.next(price)
    print(price, param)
