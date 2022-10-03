class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        
        ele= min(val,self.minStack[-1]) if self.minStack else val
        
        self.stack.append(val)
        
        self.minStack.append(ele)
    def pop(self) -> None:
        self.stack.pop() if self.stack else None
        self.minStack.pop() if self.minStack else None
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        
    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
