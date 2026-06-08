class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(char for char in s if char.isalnum()).lower()
        
        rev = new[::-1]
        print(new, "  XXXXXX ",rev)
        return new == rev

        