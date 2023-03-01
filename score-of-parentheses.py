class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        s = s.replace('()','1')
        for i in s:
            if i == ')':
                total = 0
                while stack[-1] != '(':
                    total += int(stack.pop())
                stack.pop()
                stack.append(total*2)
            elif i == '(':
                stack.append(i)
            else:
                stack.append(int(i))
                
        return stack[-1] if len(stack) == 1 else sum(stack)