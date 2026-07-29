class MinStack:

    def __init__(self):
        self.s = []
        self.l = len(self.s)
        #t = s[-1]
        

    def push(self, value: int) -> None:
        self.s.append(value)
        self.l = len(self.s)
        self.t = self.s[-1]

        

    def pop(self) -> None:
        self.s.pop()
        self.l = len(self.s)
        if len(self.s) != 0:
            self.t = self.s[-1]
        

    def top(self) -> int:
        print(self.t)
        return self.t 
        

    def getMin(self) -> int:
        return min(self.s)
        
