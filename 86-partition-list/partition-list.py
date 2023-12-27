# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        valid = dummy
        prev = dummy
        cur = head

        while cur:
            if cur.val < x:
                if valid.next is not cur:
                    prev.next = cur.next
                    cur.next = valid.next
                    valid.next = cur
                    valid = cur

                    cur = prev.next
                else:
                    valid = cur
                    prev = cur
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next

        return dummy.next

        