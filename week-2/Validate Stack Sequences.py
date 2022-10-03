class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        push=pop=0
        while push<len(pushed):
            while stack and stack[-1]==popped[pop]:
                stack.pop()
                pop+=1
            stack.append(pushed[push]) 
            push+=1
        while stack and stack[-1]==popped[pop]:
                stack.pop()
                pop+=1
        if stack:
            return False
        return True
