# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.traverse(root, 0, result)
        return result
        
    def traverse(self, node, level, result):
        if len(result) < level + 1:
            result.append([])
        result[level].append(node.val)
        if node.left:
            self.traverse(node.left, level + 1, result)
        if node.right:
            self.traverse(node.right, level + 1, result)