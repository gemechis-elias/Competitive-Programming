class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        size = len(nums)
        nums_costs = sorted([(nums[i], cost[i]) for i in range(size)], key=itemgetter(0))
        #nums_costs.item = (num, cost) sorted by num low to high
        
        left_index = 0
        left_cost_accrued = 0
        left_per_unit_cost = nums_costs[left_index][1]
        right_index = size - 1
        right_cost_accrued = 0
        right_per_unit_cost = nums_costs[right_index][1]

        while right_index - left_index > 0:
            if left_per_unit_cost < right_per_unit_cost:
                low_value = nums_costs[left_index][0]
                next_lowest_value = nums_costs[left_index + 1][0]
                left_cost_accrued += (next_lowest_value - low_value) * left_per_unit_cost
                left_per_unit_cost += nums_costs[left_index + 1][1]
                left_index += 1
            else:
                high_value = nums_costs[right_index][0]
                next_highest_value = nums_costs[right_index - 1][0]
                right_cost_accrued += (high_value - next_highest_value) * right_per_unit_cost
                right_per_unit_cost += nums_costs[right_index - 1][1]
                right_index -= 1
        
        total_cost = left_cost_accrued + right_cost_accrued
        return total_cost