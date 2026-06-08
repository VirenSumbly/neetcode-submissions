class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        a= 0
        ans=0

        for b in range(len(s)):
            while s[b] in my_set:
                my_set.remove(s[a])
                a+=1
            my_set.add(s[b])
            ans = max(ans,b-a+1)
        return ans 
             
