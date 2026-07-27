# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        levels = []

        def bfs(root):
            q = deque()
            index = 0 
            q.append((0 , root))

            while q:
                q_len = len(q)
                level = []
                while q_len > 0 : 
                    i , node = q.popleft()
                    level.append((i , node))
                    
                    if node.left : 
                        q.append(( 2*i , node.left))
                    
                    if node.right:
                        q.append( ((2*i) + 1 , node.right))
                    q_len -= 1

                levels.append(level)
        
        # travesre the BT and give each node its index  
        bfs(root)
        max_len= 0

        for level in levels:
            width = level[-1][0] - level[0][0]
            if width > max_len: 
                max_len = width

        return max_len + 1
