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
            if dummy.next in map:
                copy.next = map[dummy.next]
            else:
                copy.next = None

            if dummy.random in map:
                copy.random = map[dummy.random]
            else:
                copy.random = None

            dummy = dummy.next
        
        return map[head]






        