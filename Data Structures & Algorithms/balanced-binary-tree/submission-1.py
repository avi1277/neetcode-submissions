# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(curr):
            if not curr:
                return 0
            
            return 1 + max(dfs(curr.left), dfs(curr.right))

        if (abs(dfs(root.left) - dfs(root.right))) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)                
        