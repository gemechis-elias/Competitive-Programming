# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def grand(self,root):
        summ = 0
        if not root:
            return 0
        if (root.left):
            if (root.left.left):
                summ += root.left.left.val
            if (root.left.right):
                summ += root.left.right.val
        if (root.right):
            if (root.right.left):
                summ += root.right.left.val
            if (root.right.right):
                summ += root.right.right.val
        return summ
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.sumEvenGrandparent(root.left)
        right = self.sumEvenGrandparent(root.right)
        if root.val % 2 == 0:
            res = self.grand(root) + left + right
            return res
        return left + right
