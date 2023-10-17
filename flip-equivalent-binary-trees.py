# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def checkEqual(root1, root2):
            # check both the roots are not available
            if not root1 and not root2:
                return True

            # check both the roots are values with each other
            if not root1 or not root2 or root1.val != root2.val:
                return False

            #  
            case1 = (checkEqual(root1.left,root2.left) and checkEqual(root1.right , root2.right) )

            case2 = (checkEqual(root1.left,root2.right) and checkEqual(root1.right , root2.left) )
            
            return case1 or case2
        
        return checkEqual(root1,root2)