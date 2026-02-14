import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to store (value, index, node)
        min_heap = []
        
        # 1. Push the head of each list into the heap
        for i, l in enumerate(lists):
            if l:
                # We use 'i' as a tie-breaker so Python doesn't try to compare 
                # ListNode objects if two values are equal.
                heapq.heappush(min_heap, (l.val, i, l))
        
        # Dummy head to simplify result list construction
        dummy = ListNode(0)
        current = dummy
        
        # 2. Process the heap
        while min_heap:
            # Pop the smallest node
            val, i, node = heapq.heappop(min_heap)
            
            # Add to our result list
            current.next = node
            current = current.next
            
            # 3. If there is a next node in that specific list, push it to heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
