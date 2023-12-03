class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(root):
            if root:
                root.left, root.right = root.right, root.left
                fun(root.left)
                fun(root.right)
        
        fun(root)
        return root 