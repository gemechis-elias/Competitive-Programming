# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimum(self,node):
        cur_node = node
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node 
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = self.minimum(root.right)
                root.val = temp.val 
                root.right = self.deleteNode(root.right,temp.val)
        return root