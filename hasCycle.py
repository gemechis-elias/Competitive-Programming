class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head,head
        while slow != None and fast != None and fast.next  != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
