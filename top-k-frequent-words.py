class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, (-freq, word))
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result