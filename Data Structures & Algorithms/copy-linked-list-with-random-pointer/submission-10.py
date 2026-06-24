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

        pointer = head

        while pointer:
            copy = Node(pointer.val)
            map[pointer] = copy
            
            pointer = pointer.next

        pointer = head
        while pointer:
            copy = map[pointer]
            copy.next = map[pointer.next]
            copy.random = map[pointer.random]

            pointer = pointer.next

        return map[head]







        