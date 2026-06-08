class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(ch.lower() for ch in s if ch.isalnum())
        i = 0
        j = len(new)-1
        while(i<j):
            if(new[i]!=new[j]):
                return False
            i +=1
            j -=1 
        return True
        