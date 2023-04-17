class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        ans = []
        for i in range(len(candies)):
            if candies[i] + extraCandies>= max_:
                ans.append(True)
            else:
                ans.append(False)

        return ans