# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def traverse(root):
            nodes = []
            if root:
                nodes = traverse(root.left)
                nodes.append(root.val)
                nodes += traverse(root.right)
            return nodes
       
        def helper(root):
            nonlocal count 
            nodes=  traverse(root)
            if not root:
                return count 
            if sum(nodes)//len(nodes) == root.val:
                count += 1
            helper(root.left)
            helper(root.right)

            return count
        
        return helper(root)