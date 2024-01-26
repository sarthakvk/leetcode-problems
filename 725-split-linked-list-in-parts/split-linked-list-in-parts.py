# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        t = head
        ans = []
        while t:
            n += 1
            t = t.next
        
        if n <= k:
            while head:
                ans.append(head)
                prev = head
                head = head.next
                prev.next = None
            if n < k:
                for i in range(n, k):
                    ans.append(None)
        else:
            min_nodes = n // k
            extra = n % k
            
            for i in range(k):
                ans.append(head)
                count = 0
                prev = None
                while count != min_nodes:
                    prev = head
                    head = head.next
                    count += 1
                
                if extra > 0:
                    prev = head
                    head = head.next
                    extra -= 1
                
                prev.next = None
        
        return ans

        

        