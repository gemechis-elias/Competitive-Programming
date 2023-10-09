# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def helper(node,s, path):
            nonlocal ans
            if node:
                s-=node.val   
                if not node.left and not node.right and s==0:
                    ans.append(path)
                    return               
                helper(node.left,s, path+([node.left.val] if node.left else []))
                helper(node.right,s,path+([node.right.val] if node.right else []))
        helper(root,targetSum, [root.val] if root else [])
        return ans
