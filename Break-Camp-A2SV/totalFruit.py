class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = right = 0
        window = {}
        ans = 0
        while right < n:
            window[fruits[right]] = window.get(fruits[right], 0)+1
            while len(window)>2:
                window[fruits[left]] -=1
                if window[fruits[left]] ==0:
                    del window[fruits[left]]
                left +=1
            ans = max(ans, right-left+1)
            
            right+=1
            print(window, ans)
        return ans
