class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                index=stack.pop()
                
                before=s[:index+1]
                reverse=s[index+1:i][::-1]
                after=s[i:]

                s=before+reverse+after
        result=""
        for i in s:
            if i not in {"(",")"}:
                result+=i
        return result
