class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        up = [0] * n
        down = [0] * n
        
        teams = 0
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    up[i] += 1
                    teams += up[j]
                else:
                    down[i] += 1
                    teams += down[j]
        
        return teams