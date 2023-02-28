# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1: Optional[ListNode], list2: Optional[ListNode], tmp:Optional[ListNode])-> Optional[ListNode]:
            if list1 and list2:
                if list1.val < list2.val:
                    tmp.next =  list1
                    list1 = list1.next
                else:
                    tmp.next =  list2
                    list2 = list2.next
                tmp = tmp.next
            else:
                if list1:
                    tmp.next = list1
                if list2:
                    tmp.next = list2

                return
            return merge(list1, list2, tmp)

        node = ListNode()    
        merge(list1, list2, node)
        return node.next
        
