class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isValid(s):
            return len(s) == len(set(s))

        def backtrack(idx, curr):
            if idx == len(arr):
                return len(curr) if isValid(curr) else 0
            
            ans = backtrack(idx+1, curr)
            if isValid(curr + arr[idx]):
                ans = max(ans, backtrack(idx+1, curr+arr[idx]))
            return ans
        
        return backtrack(0, "")