# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases: empty list or list with only one node
        if not head or not head.next:
            return head
        
        # Create a dummy node that points to the head
        # This helps strictly handle the head swap logic generically
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' sits immediately before the pair we are about to swap
        prev = dummy
        
        # We continue as long as there is a pair to swap (head and head.next)
        while head and head.next:
            # 1. Identify the two nodes to be swapped
            first = head
            second = head.next
            
            # 2. Perform the swap
            # Connect the previous node to the second node (which moves to front)
            prev.next = second
            # Connect the first node to the node coming after the second node
            first.next = second.next
            # Connect the second node back to the first node
            second.next = first
            
            # 3. Re-position pointers for the next iteration
            # 'prev' moves to 'first', which is now the tail of this swapped pair
            prev = first
            # 'head' moves to the start of the next pair
            head = first.next
            
        # Return the new head (node after dummy)
        return dummy.next
