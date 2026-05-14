class StockSpanner:

    def __init__(self):
        self.day = -1
        self.stack = [(-1, 10**8)]        

    def next(self, price: int) -> int:
        self.day += 1
        while self.stack[-1][1] <= price:
            self.stack.pop()
        val = self.day - self.stack[-1][0]
        self.stack.append((self.day, price))
        return val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)