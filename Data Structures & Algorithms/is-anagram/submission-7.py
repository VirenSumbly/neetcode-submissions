class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dict = {}
        # l_s = list(s)
        # l_t = list(t)
        for char in s:
            dict[char]=dict.get(char,0)+1

        for char in t: 
            dict[char] = dict.get(char,0)-1

        return not any(dict.values())

       