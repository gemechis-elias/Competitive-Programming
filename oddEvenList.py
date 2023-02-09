# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        ptr2_head = head.next
        ptr1 = head
        ptr2 = head.next
        
        while ptr1.next and ptr1.next.next:
            ptr1.next = ptr1.next.next
            ptr2.next = ptr2.next.next
            ptr1, ptr2 = ptr1.next, ptr2.next

        ptr1.next = ptr2_head
        
        return head
