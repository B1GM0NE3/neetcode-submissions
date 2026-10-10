# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root: Optional[TreeNode], count) -> int:
            if not root:
                return count
            count += 1

            count = max(dfs(root.left, count), dfs(root.right, count))
            
            return count

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:     
        return dfs(root, 0)

            
