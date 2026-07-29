class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                if type(eval(i)) == int:
                    stack.append(int(i))
            except:
                if i == '/':
                    result = eval(f'{stack[-2]} / {stack[-1]}')
                    result = int(result)
                    
                else:
                    result=eval(f'{stack[-2]} {i} {stack[-1]}')
                
                stack.pop(-2)
                stack.pop(-1)
                print(f'result: {result}')
                stack.append(result)
        print(stack)
        return stack[-1]


        