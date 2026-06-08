class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a,b = 0,0
        count = 0
        if len(s) == 1: 
            return 1
        while b<len(s):
            if len(set(s[a:b+1]))==len(s[a:b+1]):
                count=max(count,len(s[a:b+1]))
                b+=1
            else:
                a +=1
              
        return count
             
