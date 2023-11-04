# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        queue = collections.deque([(root, False)])
        res = []
        deleteSet = set(to_delete)
        
        while queue:
            node, hasParent = queue.popleft()
            # new Root found
            if not hasParent and node.val not in to_delete:
                res.append(node)
                
            hasParent = not node.val in to_delete

            if node.left: 
                queue.append((node.left, hasParent))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                queue.append((node.right, hasParent))
                if node.right.val in to_delete:
                    node.right = None
            
        return res