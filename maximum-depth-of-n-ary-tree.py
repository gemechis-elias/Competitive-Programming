"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        depth = 0
        
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        
        #print ('root ' + str(root.val) + ' depth ' + str(depth + 1))
        return depth + 1