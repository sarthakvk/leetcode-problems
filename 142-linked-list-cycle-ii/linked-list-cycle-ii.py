# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        f,s = head, head
        while True:
            if not (f and f.next and f.next.next):
                return

            f = f.next.next
            s = s.next

            if f is s:
                break
        
        s = head

        while f != s:
            f = f.next
            s = s.next
        
        return s

            
