class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        price_span = [price, 1]
        if not self.stock:
            self.stock.append(price_span)
        elif self.stock[-1][0] > price:
            self.stock.append(price_span)
        else:
            while self.stock and self.stock[-1][0] <= price:
                p, s = self.stock.pop()
                price_span[1] += s
            self.stock.append(price_span)
        return price_span[1]
    

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)