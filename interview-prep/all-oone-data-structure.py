class AllOne:

    def __init__(self):
        self.mem = dict()
        self.prev_max = None
        self.prev_min = None
        
    def inc(self, key: str) -> None:
        self.prev_max, self.prev_min = None, None

        if key not in self.mem:
            self.mem[key] = 1
        else:
            self.mem[key] += 1

    def dec(self, key: str) -> None:
        self.prev_max, self.prev_min = None, None

        if self.mem[key] == 1:
            self.mem.pop(key)
        else:
            self.mem[key] -= 1
        
    def getMaxKey(self) -> str:
        if len(self.mem) == 0:
            return ""
        else:
            if self.prev_max != None:
                return self.prev_max
            
            output = sorted(self.mem.items(), key=lambda x:x[1])[-1][0]
            self.prev_max = output

            return output
        
    def getMinKey(self) -> str:
        if len(self.mem) == 0:
            return ""
        else:
            if self.prev_min != None:
                return self.prev_min
            output = sorted(self.mem.items(), key=lambda x:x[1])[0][0]
            self.prev_min = output
            return output