typedef struct ListNode NODE;
struct ListNode* middleNode(struct ListNode* head)
{
    NODE *slow = head;
    NODE *fast = head;
    
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
        
    return slow;
}
