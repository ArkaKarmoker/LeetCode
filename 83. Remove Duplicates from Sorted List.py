# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        # Traverse the list until the end is reached
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Duplicate found, bypass the next node
                curr.next = curr.next.next
            else:
                # Distinct value, move forward
                curr = curr.next
                
        return head
