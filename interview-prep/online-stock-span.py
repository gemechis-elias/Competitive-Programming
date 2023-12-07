class StockSpanner:

    def __init__(self):
        self.stack = []
        self.d = defaultdict(int)
        self.l = 0

    def next(self, price: int) -> int:
        if not self.stack:
            self.l += 1
            self.stack.append([price,self.l])
            self.d[self.l] += 1
        else:
            self.l += 1
            while self.stack and self.stack[-1][0] <= price:
                p,l = self.stack.pop()
                self.d[self.l] += self.d[l]
            self.stack.append([price,self.l])
            self.d[self.l] += 1
        return self.d[self.l]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)