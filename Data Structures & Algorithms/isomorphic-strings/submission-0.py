class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hs = {}
        ht = {} 
        for i in range(len(s)):
            c1,c2 = s[i],t[i]
            if (c1 in hs and hs[c1] != c2) or (c2 in ht and ht[c2] != c1):
                return False
            hs[c1] = c2
            ht[c2] = c1
        return True
        