class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        resultA=[]
        #nearest smallest left dir-> 
        for i in range(len(heights)):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                resultA.append(stack[-1][1])
            else:
                resultA.append(-1)
            stack.append([heights[i],i])
        #print(f'NSL{resultA}')

        stack2=[]
        resultB=[]
        for i in range(len(heights)-1,-1,-1):
            while stack2 and stack2[-1][0] >= heights[i]:
                stack2.pop()
            if stack2:
                resultB.append(stack2[-1][1])
            else:
                resultB.append(len(heights))
            stack2.append([heights[i],i])
        #print(f'NSR{resultB[::-1]}')
        resultB=resultB[::-1]

        area_arr = []
        for i in range(len(heights)):
            diff = abs(- resultA[i] + resultB[i] - 1)
            area=diff*heights[i]
            area_arr.append(area)
        #print(f'area array: {area_arr}')
        return max(area_arr)





        

