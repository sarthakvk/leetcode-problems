# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(next=head)
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        current = prev.next

        for _ in range(right-left):
            nxt = current.next
            prev.next, current.next, nxt.next = nxt, nxt.next, prev.next
        
        return dummy.next
