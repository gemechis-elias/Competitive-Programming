class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0} 
        arr2.sort()

        for num1 in arr1:
            new_dp = {}
            for key in dp:
                if num1 > key:
                    new_dp[num1] = min(new_dp.get(num1, float('inf')), dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    new_dp[arr2[loc]] = min(new_dp.get(arr2[loc], float('inf')), dp[key] + 1)
            dp = new_dp
            print(dp)

        if dp:
            return min(dp.values())
        return -1