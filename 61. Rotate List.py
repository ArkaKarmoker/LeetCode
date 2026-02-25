# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Determine the length of the linked list and locate the current tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Calculate the effective number of rotations
        k %= length
        if k == 0:
            return head

        # Connect the tail to the head to form a circular linked list
        tail.next = head

        # Find the new tail, which is (length - k - 1) steps from the head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # The new head is the node immediately following the new tail
        new_head = new_tail.next
        
        # Break the cycle to form the new un-linked list
        new_tail.next = None

        return new_head
