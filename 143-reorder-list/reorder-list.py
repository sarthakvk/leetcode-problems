# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_map = {}
        start = head
        n = 0
        while start:
            node_map[n] = start
            n += 1
            start = start.next
        
        s = node_map[0]
        h = None
        l = None
        
        for i in range((n+1)//2):
            j = (n-1) - i
            if i != j:
                s.next = node_map[i]
                s = s.next
                s.next = node_map[j]
                s = s.next

                del node_map[i]
                del node_map[j]

            elif i == j:
                s.next = node_map[i]
                s = s.next

                del node_map[i]

            if i == 0:
                h = s

        s.next = None

        
        return h