class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path):
            if len(path) > 1:
                res.append(path)
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    dfs(i + 1, path + [nums[i]])
        
        res = []
        dfs(0, [])
        return res