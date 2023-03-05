class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                j = stack.pop()
                right[j] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
            
        while stack:
            j = stack.pop()
            right[j] = n
        ans = 0
        MOD = 10**9 + 7
        for i in range(n):
            contribution = (i - left[i]) * (right[i] - i) * arr[i]
            ans = (ans + contribution) % MOD
        return ans