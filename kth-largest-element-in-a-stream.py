class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapify(nums)
        self.k = k
        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heapreplace(self.minHeap, val)
        return self.minHeap[0]
            
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)