# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        prev = None
        n = 1
        l = None
        lp = None

        while node:
            t = node.next
            if left < n <= right:
                node.next = prev
            if n == left:
                l = node
                lp = prev
            prev = node
            node = t

            if n == right:
                break

            n += 1
        
        l.next = node
        if lp:
            lp.next = prev
        else:
            head = prev
        
        return head
