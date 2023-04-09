# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0
        self.helper(root, targetSum, [])
        return self.count
    
    def helper(self, root, targetSum, path):
        if not root:
            return
        
        path.append(root.val)
        curr_sum = 0
        for i in range(len(path)-1, -1, -1):
            curr_sum += path[i]
            if curr_sum == targetSum:
                self.count += 1
        
        self.helper(root.left, targetSum, path)
        self.helper(root.right, targetSum, path)
        path.pop()