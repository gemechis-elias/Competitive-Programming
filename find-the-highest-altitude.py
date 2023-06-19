class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        currentAltitude = 0
        
        for g in gain:
            currentAltitude += g
            maxAltitude = max(maxAltitude, currentAltitude)
        
        return maxAltitude