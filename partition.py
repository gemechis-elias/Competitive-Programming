# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
            self.head1 = None
            self.head2 = None
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        dummy = head
        curr = None
        curr2 = None
        while dummy:
            if dummy.val < x:
                if curr is None:
                    self.head1 = ListNode(dummy.val)
                    curr = self.head1
                else:
                    curr.next = ListNode(dummy.val)
                    curr = curr.next
            else:
                if curr2 is None:
                    self.head2 = ListNode(dummy.val)
                    curr2 = self.head2
                else:
                    curr2.next = ListNode(dummy.val)
                    curr2 = curr2.next

            dummy = dummy.next
        if curr is not None:
            curr.next = self.head2
        else:
            return self.head2

        return self.head1
