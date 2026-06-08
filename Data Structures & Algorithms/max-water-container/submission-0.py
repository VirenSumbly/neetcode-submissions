class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxarea =0 
        while l<r:
            area = (r-l)* min(heights[r],heights[l])
            maxarea = max(maxarea, area)
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
            
        return maxarea

         