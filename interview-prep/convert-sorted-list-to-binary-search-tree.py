# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def toBST(self, left: int, right: int) -> Optional[TreeNode]:
        if left >= right: return
        mid = (left + right) // 2
        leftTree = self.toBST(left, mid)
        val = self.current.val
        self.current = self.current.next

        rightTree = self.toBST(mid+1, right)
        return TreeNode(val, leftTree, rightTree)

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node = head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        self.current = head
        
        return self.toBST(0, count)