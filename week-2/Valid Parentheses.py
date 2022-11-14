class Solution:
    def isValid(self, s: str) -> bool:
        clodeToOpen={")" : "(" ,  "}" : "{","]" :"["}
        stack=[]
        for i in s:
            if i in clodeToOpen:
                if stack and stack[-1]==clodeToOpen[i]:
                    stack.pop()
                    continue
                return False
            stack.append(i)
        return not stack
