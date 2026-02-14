# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the start of the result list.
        # This simplifies handling the edge case where the head changes.
        dummy = ListNode()
        tail = dummy
        
        # 2. Iterate while both lists have nodes remaining
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1    # Append list1 node
                list1 = list1.next   # Move list1 pointer forward
            else:
                tail.next = list2    # Append list2 node
                list2 = list2.next   # Move list2 pointer forward
            
            tail = tail.next         # Move the tail pointer forward
        
        # 3. If one list is not empty, append the rest of it to the result.
        # Since the lists are sorted, the remainder is already in order.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # 4. Return the next node of dummy, which is the actual head of the merged list.
        return dummy.next
