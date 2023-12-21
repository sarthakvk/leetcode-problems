# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        current = head
        
        left = 1
        right = k
        knode = True

        while knode:
            tmp = current
            for _ in range(right-left):
                if not tmp:
                    knode = False
                    break
                tmp = tmp.next
            if not tmp:
                knode = False
                break
            
            if knode:
                for _ in range(right-left):
                    nxt = current.next
                    prev.next, current.next, nxt.next = nxt, nxt.next, prev.next
                
                for _ in range(k):
                    if not prev.next:
                        return dummy.next
                    prev = prev.next
                current = prev.next
                left = right + 1
                right = left + k - 1
        
        return dummy.next


        