# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helperFunc(root):
            result=[]

            if root:
                result.extend(helperFunc(root.left))
                result.append(root.val)
                result.extend(helperFunc(root.right))
            
            return result
        
        result=helperFunc(root)

        if result==sorted(set(result)):
            return True
        else:
            return False