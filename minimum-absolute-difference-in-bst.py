class Solution:
    def getMinimumDifference(self, root):
        self.min_diff = float('inf')
        self.prev_val = None
        
        def inorder_traversal(node):
            if node is None:
                return
            
            inorder_traversal(node.left)
            
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
                
            self.prev_val = node.val
            
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        
        return self.min_diff