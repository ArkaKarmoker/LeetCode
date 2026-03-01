# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node points to head to handle cases where the head itself is duplicated
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr:
            # Check if the current node is the start of duplicates
            if curr.next and curr.val == curr.next.val:
                # Move curr to the very last node of this duplicate group
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip the entire duplicate group by linking prev to the next distinct node
                prev.next = curr.next
            else:
                # Node is distinct, advance the prev pointer
                prev = prev.next
            
            # Move curr forward to continue evaluation
            curr = curr.next
            
        return dummy.next
