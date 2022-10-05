class MyCircularDeque:

    def __init__(self, k: int):
        self.size=0
        self.front=0
        self.rear=0
        self.maxsize=k
        self.queue=[None]*k
    def insertFront(self, value: int) -> bool:
        
        if self.isFull(): return False
        if self.isEmpty():
            self.queue[self.front]=value
            self.size+=1
            return True
        self.front=(self.front-1)%self.maxsize
        self.queue[self.front]=value
        self.size+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty() :
            self.queue[self.rear]=value
            self.size+=1
            return True
        self.rear=(self.rear+1)%self.maxsize
        self.queue[self.rear]=value
        self.size+=1
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        if self.size!=1: 
            self.front=(self.front+1)%self.maxsize
        self.size-=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        if self.size!=1: 
            self.rear=(self.rear-1)%self.maxsize
        self.size-=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.maxsize==self.size
