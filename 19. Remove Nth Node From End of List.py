# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head.
        # This helps handle the edge case where the head itself needs to be removed.
        dummy = ListNode(0, head)
        
        # Initialize two pointers at the dummy node
        left = dummy
        right = dummy
        
        # Move the right pointer n steps ahead
        for _ in range(n):
            right = right.next
            
        # Move both pointers until right reaches the end of the list
        while right.next:
            left = left.next
            right = right.next
            
        # left is now just before the node to be removed.
        # Skip the node by pointing left.next to the node after it.
        left.next = left.next.next
        
        # Return the new head (which is dummy.next)
        return dummy.next
