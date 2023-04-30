class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums
        c = collections.Counter(nums)
        d = [(c[key], key) for key in c]
        d.sort(reverse=True)
        return [p[1] for p in d[:k]]