# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def deldup(prev, node):
            start = node.next
            is_dup = False
            while start and start.val == node.val:
                is_dup = True
                start = start.next
            
            if is_dup:
                prev.next = start
            
            return is_dup
            
        dummy = ListNode(val=-1000, next=head)
        prev = dummy
        start = head

        while start:
            is_dup = deldup(prev, start)
            if not is_dup:
                prev = start
            start = prev.next

        
        return dummy.next
        