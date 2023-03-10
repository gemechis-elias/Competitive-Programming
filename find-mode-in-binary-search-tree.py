# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        def helper(root):
            nonlocal result
            if root:
                result = helper(root.left)
                result.append(root.val)
                result =  helper(root.right)
            return result

      
        ans = helper(root)
        if len(ans)==1:
            return ans

        c = Counter(ans)
        mod = []
        max_ = max(c.values())
        for key, value in c.items():
            if value == max_:
                mod.append(key)

        return mod