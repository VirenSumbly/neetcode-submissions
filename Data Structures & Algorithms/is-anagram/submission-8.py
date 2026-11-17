class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for i in s:
            if i not in h:
                h[i] = 1
            elif i in h:
                h[i] += 1
        
        for i in t:
            if i in h:
                h[i] -= 1

        for i in h.values():
            if i!=0:
                return False
        return True    
        