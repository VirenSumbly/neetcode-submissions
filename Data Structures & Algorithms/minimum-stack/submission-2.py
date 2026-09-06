class MinStack:

    def __init__(self):
        self.s = []
        self.ms =[]
        #self.l = len(self.s)
        #t = s[-1]
        #self.m = float('+inf')
        

    def push(self, value: int) -> None:
        self.s.append(value)
        if len(self.ms) == 0:
            self.ms.append(value)
        else:
            el = min(self.ms[-1], value)
            self.ms.append(el)
         
        #self.l = len(self.s)
        #self.t = self.s[-1]
        #self.m = min(self.m, value)

        

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()

        

    def top(self) -> int:
        #print(self.t)
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
        
