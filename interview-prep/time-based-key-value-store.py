class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        N = len(self.store[key])
        arr = self.store[key]
        if arr and arr[0][0] > timestamp:
            return ''
        
        if arr and arr[-1][0] <= timestamp:
            return arr[-1][1]
        left = 0
        right = N - 1
        while right > left + 1:
            mid = left + (right - left)//2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                right = mid
            else:
                left = mid
        return arr[left][1] if arr and left <= timestamp else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)