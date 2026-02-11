# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify the head of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Iterate while there are nodes in l1, l2, or there is a carry left
        while l1 is not None or l2 is not None or carry != 0:
            # Get values from the lists, if the node is None, use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for this digit position
            total_sum = val1 + val2 + carry
            
            # Update carry for the next position (integer division)
            carry = total_sum // 10
            
            # Create a new node with the digit value (remainder)
            new_digit = total_sum % 10
            current.next = ListNode(new_digit)
            
            # Move pointers forward
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the next node of dummy head which is the actual start of result
        return dummy_head.next
