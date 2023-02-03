# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        
        ptr1 = head
        ptr2 = head
        
        for i in range(n):
            ptr2 = ptr2.next
        
        
        prev = dummy_node
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            prev = prev.next
      
        prev.next = ptr1.next
        return dummy_node.next 



