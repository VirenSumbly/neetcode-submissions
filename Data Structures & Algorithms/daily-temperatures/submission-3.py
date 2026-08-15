class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        result = []

        for i in range(len(temperatures)-1,-1,-1):
            if len(stack) == 0:
                result.append(0)
            elif len(stack) > 0 and stack[-1][0] > temperatures[i]:
                result.append(stack[-1][1] - i)

            elif len(stack)>0 and stack[-1][0] <= temperatures[i]:
                while len(stack) > 0 and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if len(stack) == 0:
                    result.append(0)
                else:
                    result.append(stack[-1][1] - i)
            stack.append([temperatures[i],i])
        return result[::-1]
         