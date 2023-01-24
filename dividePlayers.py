class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n =len(skill)
        start = 0
        sum_ = 0
        end = n-1
        ans = 0
        # Group
        c_s = skill[0] + skill[-1]
        while start < end:
            if skill[start] + skill[end] != c_s:
                return -1
            ans += skill[start] * skill[end]
            start += 1
            end -= 1
        return ans

            
        
