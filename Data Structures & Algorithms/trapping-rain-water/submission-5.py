class Solution:
    def trap(self, height: List[int]) -> int:
        m = 0
        n = [0,]
        
        for i in range(1,len(height)):
            m = max(m,height[i-1])
            if m == height[i]:
                n.append(0)
                continue
            n.append(m)
        #print(f'n{n}')

        p = 0 
        r = [0]

        for i in range(len(height)-2,-1,-1):
            p = max(p,height[i+1])
            if p == height[i] or p <height[i]:
                r.append(0)
                continue
            r.append(p)
            
        #print(f'r{r[::-1]}')
        r = r[::-1]

        ans=0
        for i in range(len(height)):
            diff = min(r[i],n[i]) - height[i]
            if diff > 0:
                ans+=diff
        return ans

            


        