class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ans = "/"
        
        sections = path.split("/")
        
        for p in sections:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
                
        return ans + '/'.join(stack)
