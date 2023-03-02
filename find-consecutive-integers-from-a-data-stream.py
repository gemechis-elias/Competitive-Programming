class DataStream:

    def __init__(self, value: int, k: int):
        self.queue=[]
        self.value=value
        self.k=k   

    def consec(self, num: int) -> bool:
        if num==self.value:
            self.queue.append(num)
        else:
            self.queue.clear()
        if len(self.queue)>=self.k:
            return True
        else:
            return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

        
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)