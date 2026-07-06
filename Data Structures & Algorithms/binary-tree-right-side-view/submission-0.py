# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = collections.deque()
        q.append(root)

        while q:
            right = None
            qLength = len(q)

            for i in range(qLength):
                node = q.popleft()
                if node:
                    right = node.val
                    q.append(node.left)
                    q.append(node.right)

            if right:
                output.append(right)
        return output


        