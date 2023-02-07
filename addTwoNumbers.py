# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        upper = l1
        lower = l2
        ans = []
        dummy = left = None

        n = 0
        while upper and lower:
            if upper is not None and lower is not None: 
                sum_ = upper.val + lower.val
                upper = upper.next
                lower = lower.next
            else:
                if upper is not None and lower is None:
                    sum_ = upper.val
                    upper = upper.next
                elif lower is not None and upper.next is None:
                    sum_ = lower.val
                    lower = lower.next

            if sum_+n < 10:
                ans.append(sum_ + n)
                n = 0
            else:
                if n!=0:
                    sum_ +=n
                r = sum_ - 10
                n = 1
                ans.append(r)
        print(ans)
         # checking non-empty lists
        if upper is not None:
            left = upper
        if lower is not None:
            left = lower
        # adding to ans array
        while left:
            if left.val + n<10:
                ans.append(left.val+n)
                n = 0
            else:
                ans.append(0)

            left = left.next

        if n != 0:
            ans.append(n)
      
        #changing arr to linked list    
        for i in range(len(ans)):
            if dummy is None:
                dummy = ListNode(ans[i])
            else:
                temp = dummy
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(ans[i])

        
        return dummy

