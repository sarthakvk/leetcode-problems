class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        no_incoming = set(range(n))

        for frm, to in edges:
            if to in no_incoming:
                no_incoming.remove(to)
        
        return list(no_incoming)