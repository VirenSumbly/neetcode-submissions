class Solution:
    def trap(self, height: List[int]) -> int:
        l,r, water  = 0, len(height) - 1, 0
        left_max, right_max = height[l],height[r]
        while l < r:
            if height[l] < height[r]:
                #process left
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l+=1
            else: 
                #prcoess right
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r-=1
        return water

        