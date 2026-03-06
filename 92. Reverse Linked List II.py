# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # If the list is empty or no reversal is needed
        if not head or left == right:
            return head
        
        # Dummy node simplifies operations when the head itself needs to change
        dummy = ListNode(0, head)
        prev = dummy
        
        # Advance prev to the node just before the sublist starting position
        for _ in range(left - 1):
            prev = prev.next
            
        # curr points to the first node of the sublist to be reversed
        curr = prev.next
        
        # Iteratively move the node right after curr to the front of the sublist
        for _ in range(right - left):
            temp = curr.next
            
            # Detach temp and connect curr to the rest of the unreversed list
            curr.next = temp.next
            
            # Insert temp exactly after the prev node
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
