# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # Step 1: Count total nodes to determine how many groups we can reverse
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        # Step 2: Use a dummy node to handle the new head easily
        dummy = ListNode(0)
        dummy.next = head
        
        # 'group_prev' will always point to the node immediately BEFORE the group we are reversing
        group_prev = dummy
        curr = head # 'curr' will point to the first node of the group we are about to reverse

        # Step 3: Loop while there are at least k nodes left to process
        while count >= k:
            # Initialize pointers for reversal within the group
            prev = None
            ptr = curr # 'ptr' is the temporary iterator for the reversal
            
            # Reverse k nodes
            for _ in range(k):
                nxt = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = nxt
            
            # After the loop:
            # 'prev' is the new head of the reversed group (the k-th node)
            # 'curr' is the new tail of the reversed group (the 1st node)
            # 'ptr' is the start of the next remaining part of the list
            
            # Connect the previous part of the list to the new head of this group
            group_prev.next = prev
            
            # Connect the new tail of this group to the start of the next group
            curr.next = ptr
            
            # Update pointers for the next iteration
            group_prev = curr
            curr = ptr
            count -= k
            
        return dummy.next
