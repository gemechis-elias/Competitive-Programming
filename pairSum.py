# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        max_sum = 0
        i, j = 0, len(values) - 1
        while i < j:
            twin_sum = values[i] + values[j]
            if twin_sum > max_sum:
                max_sum = twin_sum
            i += 1
            j -= 1
        
        return max_sum
