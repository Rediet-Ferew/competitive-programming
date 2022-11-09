class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        span = 1
        while self.stock and self.stock[-1][0] <= price:
            p, s = self.stock.pop()
            span += s
        self.stock.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)