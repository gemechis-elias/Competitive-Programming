# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        ptr1 = copy = head
        ptr2 = ptr1.next
        n = 0
        while copy:
            copy = copy.next
            n+=1
        dummy = None
        k = k%n
        if k == 0:
            return head
        for _ in range(k):

            c = 0
            temp =start = None

            while c < n-2:
                ptr2 = ptr2.next
                ptr1 = ptr1.next
                c +=1
            ptr1.next = None
            if dummy is None:
                dummy = ListNode(ptr2.val)
            else:
                temp = dummy
                start = ListNode(ptr2.val)
                start.next = temp
                dummy = start

            if dummy.next is None:
                dummy.next = head 
            ptr1 = dummy
            ptr2 = ptr1.next 

            
        return dummy
        

        



