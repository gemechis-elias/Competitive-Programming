class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.extend([float("inf"), float("-inf")])
        heaters.sort()
        houses.sort()
        radius = 0

        i = 1

        for house in houses:
            while i < len(heaters) and heaters[i] <= house:
                i += 1
            if i < len(heaters) and heaters[i] > house:
                radius = max(radius, min(abs(house - heaters[i-1]), abs(house - heaters[i])))
            
        return radius