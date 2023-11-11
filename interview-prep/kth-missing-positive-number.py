class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missed = [x for x in range(1, 10000)]
        for n in arr:
            if n in missed:
                missed.remove(n)
        return missed[k-1]