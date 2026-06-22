"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {None : None}
        dummy = head
        while dummy:
            copy = Node(dummy.val)
            map[dummy] = copy
            dummy = dummy.next
        
        dummy = head


        while dummy:
            copy = map[dummy]
            copy.next = map[dummy.next]
            copy.random = map[dummy.random]

            dummy = dummy.next
        
        return map[head]






        