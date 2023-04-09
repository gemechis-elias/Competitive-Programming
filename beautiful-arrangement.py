class Solution:
    def countArrangement(self, n: int) -> int:
        nums = (1 << n) - 1  
        memo = {}
        print(nums)
        
        def countArrangementHelper(used: int, pos: int) -> int:
            if used == nums:   
                return 1
            if (used, pos) in memo:
                return memo[(used, pos)]
            
            count = 0
            for i in range(1, n+1):
                if not used & (1 << (i-1)) and (i % pos == 0 or pos % i == 0):
                    count += countArrangementHelper(used | (1 << (i-1)), pos+1)
            
            memo[(used, pos)] = count
            return count
        
        return countArrangementHelper(0, 1)