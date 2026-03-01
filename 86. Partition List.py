# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes to anchor the start of both partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Pointers to build the new lists
        less = less_dummy
        greater = greater_dummy
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            
            current = current.next
            
        # Terminate the greater list to avoid cycles in the linked list
        greater.next = None
        
        # Connect the end of the less list to the start of the greater list
        less.next = greater_dummy.next
        
        return less_dummy.next
