class Solution:
    def isValid(self, s: str) -> bool:
        valid_parenthesis = ["()","{}","[]"]
        opener = ["(","{","["]
        closer = [")","}","]"]
        stack =[]
       
        for i in s:
            if i in opener:
                stack.append(i)
            elif i in closer:
                if len(stack) ==0:
                    return False
                if stack[-1] + i in valid_parenthesis:
                    stack.pop()
                else:
                    return False
    
        if len(stack) == 0:
            return True
        else:
            return False
    
        