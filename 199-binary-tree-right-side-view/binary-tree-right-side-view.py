# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        res = []
        if not root : 
            return res 

        q = deque()

        def bfs(root):
            q.append(root)
            while q: 
                q_len = len(q)
                temp = []
                while q_len > 0 : 
                    node = q.popleft()
                    temp.append(node)
                    if node.left : 
                        # print("left")
                        q.append(node.left)
                    if node.right : 
                        # print("right")
                        q.append(node.right)
                    q_len -= 1  
                res.append(temp[-1].val)

        bfs(root)
        return res        

    