# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([[root, 0]])
        while queue:
            node, i = queue.popleft()
            if node.left:
                queue.append([node.left, i+1])
            if node.right:
                queue.append([node.right, i+1])
            if len(res) - 1 >= i:
                res[i].append(node.val)
            else:
                res.append([node.val])
        
        return res

        