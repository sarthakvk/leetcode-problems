# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        N = 0

        start = head
        last = None
        while start:
            N += 1
            last = start
            start = start.next
        k = k%N

        if k == 0:
            return head
        
        tail = head
        for _ in range(N-k-1):
            tail = tail.next
        
        last.next = head
        head = tail.next
        tail.next = None

        return head

        