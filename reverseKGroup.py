# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def __init__(self):
            self.head1 = None
        if head is None or head.next is None or k == 1:
            return head

        copy = head
        n = 0
        while copy:
            copy = copy.next
            n += 1

        ptr1 = head
        ptr2 = head
        
        dummy =None
        x = dummy
        
        for _ in range(n//k):
            
            for _ in range(k - 1):
                ptr2 = ptr2.next
            
            temp = ptr2.next
            
            rev = None
            while ptr1 != temp:
                nexts = ptr1.next
                ptr1.next = rev
                rev = ptr1
                ptr1 = nexts
            
            if dummy is None:
                self.head1 = rev
                dummy = self.head1
            else:
                 
                c = dummy
                while c.next:
                    c = c.next
                c.next = rev
 
             
            # print(temp)   
            ptr2 = ptr1 = temp

        #print(dummy)
        
        i = dummy
        while i.next:
            i =i.next

        i.next = temp
        return dummy








