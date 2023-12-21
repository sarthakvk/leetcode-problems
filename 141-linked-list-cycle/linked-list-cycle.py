# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        i, j = head.next, head.next.next

        while i is not j:
            try:
                i = i.next
                j = j.next.next
            except:
                return False
        
        return True


        