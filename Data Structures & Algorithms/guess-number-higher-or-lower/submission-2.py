# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        a = 1
        b = n 
        while a <= b:
            mid = (a + b)//2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                a = mid + 1
            elif guess(mid) == -1:
                b = mid - 1
        

        