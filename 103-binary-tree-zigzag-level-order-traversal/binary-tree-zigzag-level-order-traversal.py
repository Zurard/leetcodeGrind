# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if level is odd add it otherwise reverse the level and add it 
        level = 0
        res = []
        if not root :
            return res

        from collections import deque
        q = deque()

        q.append(root)

        while q : 
            q_len =len(q)
            temp = []
            while q_len > 0 : 
                node = q.popleft()
                temp.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                q_len -=1 
            if level % 2 == 0 : 
                res.append(temp)
            else : 
                temp.reverse()
                res.append(temp)
            level += 1
        return res 