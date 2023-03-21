# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)

        def check(root, level, column):
            if not root:
                return root
            
            dic[level].append(column)
            check(root.left, level + 1, column * 2)
            check(root.right, level + 1, (column * 2) + 1)
                
        check(root, 0 , 0)
        
        return max([max(dic[level]) - min(dic[level]) + 1 for level in dic])