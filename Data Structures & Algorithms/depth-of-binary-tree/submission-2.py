# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


            

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:     
        if not root:
            return 0
        stack = [[root, 1]]
        depth = 1
        while stack:
            node, count = stack.pop()
            if node.left:
                depth = max(depth, count + 1)
                stack.append([node.left, count + 1])
            if node.right:
                depth = max(depth, count + 1)
                stack.append([node.right, count + 1])
        
        return depth
            
