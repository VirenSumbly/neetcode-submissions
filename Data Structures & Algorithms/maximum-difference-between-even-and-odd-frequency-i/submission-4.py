class Solution:
    def maxDifference(self, s: str) -> int:
        h = {}
        for i in s:
            if i not in h:
                h[i] = 1
            elif i in h:
                h[i] +=1
        diff = float('-inf')
        yo = sorted(list(h.values()))
        f = 0
        for i in range(len(yo)-1,-1,-1):
            if yo[i]%2!=0:
                f = yo[i]
                break 
        s = 0
        for j in range(len(yo)):
            if yo[j] %2 == 0:
                s = yo[j]
                break
        return f-s




        
