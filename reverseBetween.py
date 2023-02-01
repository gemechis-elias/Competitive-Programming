2# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp1, temp2 = head, head

        c =1
        while c < left:
            temp2 = temp2.next
            c+=1
        while c < right+1:
            temp1 = temp2.next
            count2 = c + 1
            while count2 != right + 1:
                value = temp2.val 
                temp2.val = temp1.val
                temp1.val = value
                temp1 = temp1.next
                count2 += 1
            
            temp2 = temp2.next
            c += 1

        return head

        

        # return head
