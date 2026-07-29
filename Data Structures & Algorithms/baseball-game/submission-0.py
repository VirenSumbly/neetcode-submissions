class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == "+":
                el = stack[-2] + stack[-1]
                stack.append(el)
            else:
                stack.append(int(i))
        print(stack)    
        if len(stack) == 0:
            return 0
        else:
            return sum(stack)






        