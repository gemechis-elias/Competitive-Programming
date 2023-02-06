# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode(None)
        distnict = newhead
        right = head
        Found = False
        while right:
            while right.next and right.val==right.next.val:
                right=right.next
                Found=True
                
            if Found :
                right = right.next 
                if not right or not right.next or right.val!=right.next.val:
                    distnict.next=right
                    distnict = distnict.next
                    Found = False
            else: 
                if distnict != right:
                    distnict.next = right
                    distnict = distnict.next
                right = right.next

        return newhead.next

