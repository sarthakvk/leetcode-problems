"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from queue import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        nmap = {}
        q = deque()
        q.append(node)
        visited = {}

        while len(q) > 0:
            print([i.val for i in q])
            n = q.popleft()
            if n.val in visited:
                continue

            if n.val not in nmap:
                nd = Node(val=n.val)
                nmap[n.val] = nd
            else:
                nd = nmap[n.val]
            visited[n.val] = True
            for nei in n.neighbors:
                if nei.val not in visited:
                    q.append(nei)

                if nei.val in nmap:
                    nd.neighbors.append(nmap[nei.val])
                else:
                    t = Node(nei.val)
                    nd.neighbors.append(t)
                    nmap[t.val] = t
            
        return nmap[node.val]
