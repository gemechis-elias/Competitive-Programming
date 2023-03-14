# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.total_sum = 0
        
        def dfs(node, num):
            if not node.left and not node.right:
                self.total_sum += num * 10 + node.val
            if node.left:
                dfs(node.left, num * 10 + node.val)
            if node.right:
                dfs(node.right, num * 10 + node.val)
        
        dfs(root, 0)
        
        return self.total_sum