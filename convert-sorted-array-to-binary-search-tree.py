# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#   [0,-10,5,-10,-3,5,9]
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(right, left):

            if right-left <= 1 :
                if right-left == 0:
                    Node = TreeNode(nums[right])
                    return Node
                Node1 = TreeNode(nums[right])
                Node2 = TreeNode(nums[left])
                Node2.right = Node1 
                return Node2
                
            mid = (right+left)//2 
            left_node = helper(max(mid-1, left), left)
            right_node = helper(right, mid+1)

            Node = TreeNode(nums[mid], left_node, right_node)

            return Node
        return helper(len(nums)-1, 0)