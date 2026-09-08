class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append([price,1])
            return 1
        elif len(self.stack)!=0 and self.stack[-1][0] > price:
            self.stack.append([price,1])
            return 1
        elif len(self.stack)!=0 and self.stack[-1][0] <= price:
            count = 1
            while self.stack and self.stack[-1][0] <= price:
                a=self.stack.pop()
                count+=a[1]
            if len(self.stack) == 0:
                self.stack.append([price,count])
            else:
                self.stack.append([price,count])
            return self.stack[-1][1]
        


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)