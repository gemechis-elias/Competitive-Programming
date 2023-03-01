class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def fn( start, end, is_p1_turn):

            if start == end:
                if is_p1_turn:
                    return [nums[start], 0]
                else:
                    return [0, nums[start]]
            
            if is_p1_turn:
                left_score =  fn(start+1,end, False)
                left_score[0] += nums[start]
                right_score = fn( start,end-1,  False)
                right_score[0] += nums[end]

                if left_score[0]> right_score[0]:
                    return left_score 
                else:
                    return right_score
            else:
                left_score = fn( start+1, end,  True)
                left_score[1] += nums[start]
                right_score = fn( start,end-1,  True)
                right_score[1] += nums[end]
                
                if left_score[1]> right_score[1]:
                    return left_score
                else:
                    return right_score
        ans = fn(0, len(nums)-1, True)
        return ans[0]>= ans[1]