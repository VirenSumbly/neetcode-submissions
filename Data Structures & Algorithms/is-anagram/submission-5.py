class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dict = {}
        l_s = list(s)
        l_t = list(t)
        for char in l_s:
            dict[char]=dict.get(char,0)+1

        for char in l_t: 
            if char in dict:
                dict[char] -= 1
            else: 
                continue

        if (any(dict.values())):
            return False
        else:
            return True

       