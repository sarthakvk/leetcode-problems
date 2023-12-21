# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        dummy = ListNode(next=head)
        start = dummy

        while start:
            N += 1
            start = start.next

        node = dummy
        for _ in range(N-n-1):
            node = node.next

        node.next = node.next.next

        return dummy.next

        