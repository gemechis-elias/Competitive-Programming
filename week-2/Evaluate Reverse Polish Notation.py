class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        hashset={"+","-","*","/"}
        for i in tokens:
            if i in hashset:
                top=stack.pop()
                second=stack.pop()
                result=str(int(eval(second+i+top)))
                stack.append(result)
                continue
            stack.append(i)
        return stack.pop()
