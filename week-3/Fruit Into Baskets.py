class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        Mydict = {}
        left = 0
        result = 0
        for right in range(len(fruits)):
            if fruits[right] in Mydict:
                Mydict[fruits[right]]+= 1
            else:
                Mydict[fruits[right]] = 1
            while len(Mydict) > 2:
                Mydict[fruits[left]] -= 1
                if Mydict[fruits[left]] == 0:
                    del Mydict[fruits[left]]
                left += 1
            result = max(result,right-left+1)
        return result
