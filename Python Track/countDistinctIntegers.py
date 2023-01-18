class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            res.append(str(nums[i]))
            temp = str(nums[i])
            is_last_zero = True
            while is_last_zero:
                if temp[-1]== "0":
                    temp = temp[:-1]
                else:
                    is_last_zero = False
            
            temp = temp[::-1]
            res.append(temp)
        return len(set(res))
        
