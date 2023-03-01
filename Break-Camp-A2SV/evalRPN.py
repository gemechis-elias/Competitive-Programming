class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i =0
        while i  < len(tokens):
            ans = 0
            if tokens[i].lstrip('-+').isdigit():
                stack.append(int(tokens[i]))
            else:
                print(tokens[i])

                top1 = int(stack[len(stack)-1])
                top2 = int(stack[len(stack)-2])
                
                if tokens[i] == "/" :
                    if top2 !=0:
                        ans = int(top2 / top1)
                    else:
                        ans = 0
                if tokens[i] == "-":
                    ans = int(top2-top1)
                if tokens[i] == "*":
                    ans = int(top2*top1)
                if tokens[i] == "+":
                    ans = int(top2+top1)

                if len(stack)>1:
                    stack.pop()
                stack.pop()
                stack.append(int(ans))
            i +=1
        return sum(stack)
