from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        if not root :
            return 0 
        
        q.append(root)
        while q : 
            q_len = len(q)
            depth += 1 
            while q_len > 0: 
                node = q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
                q_len -= 1
        return depth 
