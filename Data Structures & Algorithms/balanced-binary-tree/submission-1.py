# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = False
        def dfs(root):
            nonlocal flag
            if not root:
                return 0
            lheight, rheight = dfs(root.left), dfs(root.right)

            if lheight == -1 or rheight == -1:
                return -1 

            if abs(lheight - rheight) > 1:
                return -1

            return 1 + max(lheight, rheight)
        
        return dfs(root) != -1
            

