class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i in s:
            if i not in h:
                h[i] = 1
            elif i in h:
                h[i] += 1 
        minindex=float('inf')
        
        if 1 not in h.values():
            return -1
        
        print(h)
        print(h.items())

        for i,j in h.items():
            print(f"j:{j}")
            if j == 1:
                minindex = min(minindex,s.find(i))
        return minindex