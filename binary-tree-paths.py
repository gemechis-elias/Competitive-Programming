# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if not root:
            return paths

        def traverse(node, path):
            if not node.left and not node.right:
                paths.append(path + str(node.val))
                return
            if node.left:
                traverse(node.left, path + str(node.val) + "->")
            if node.right:
                traverse(node.right, path + str(node.val) + "->")

        traverse(root, "")

        return paths