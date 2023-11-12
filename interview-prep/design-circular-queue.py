class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k  # initialize the queue with k zeros
        self.size = 0  # current size of the queue
        self.capacity = k  # maximum capacity of the queue
        self.head = 0  # index of the front element
        self.tail = -1  # index of the last element

    def enQueue(self, value: int) -> bool:
        if self.isFull():  # if the queue is already full, cannot insert any more
            return False
        self.tail = (self.tail + 1) % self.capacity  # increment the index of the last element
        self.queue[self.tail] = value  # set the value of the last element
        self.size += 1  # increase the size of the queue
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():  # if the queue is already empty, cannot delete any more
            return False
        self.head = (self.head + 1) % self.capacity  # increment the index of the front element
        self.size -= 1  # decrease the size of the queue
        return True

    def Front(self) -> int:
        if self.isEmpty():  # if the queue is empty, return -1
            return -1
        return self.queue[self.head]  # return the value of the front element

    def Rear(self) -> int:
        if self.isEmpty():  # if the queue is empty, return -1
            return -1
        return self.queue[self.tail]  # return the value of the last element

    def isEmpty(self) -> bool:
        return self.size == 0  # if the size of the queue is 0, it's empty

    def isFull(self) -> bool:
        return self.size == self.capacity  # if the size of the queue is equal to the capacity, it's full
