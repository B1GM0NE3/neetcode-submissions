# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(node, max_val):
            nonlocal cnt
            if not node:
                return None

            if node.val >= max_val:
                max_val = node.val
                cnt += 1

            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, root.val)
        return cnt