+class Solution:
+    def minCost(self, nums: List[int], cost: List[int]) -> int:
+        size = len(nums)
+        nums_costs = sorted([(nums[i], cost[i]) for i in range(size)], key=itemgetter(0))
+        #nums_costs.item = (num, cost) sorted by num low to high
+        
+        left_index = 0
+        left_cost_accrued = 0
+        right_index = size - 1
+        right_cost_accrued = 0
+
+        # TODO: Gather left and right costs
+
+        total_cost = left_cost_accrued + right_cost_accrued
+        return total_cost