# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0 
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


        # this is iterative method

        # count = 0 
        # def bfs(root): 
        #     from collections import deque
        #     q = deque()
        #     q.append(root)        

        #     nonlocal count
        #     while q:
        #         size = len(q)
        #         while size > 0  : 
        #             node = q.popleft()
        #             count += 1
        #             if node.left :
        #                 q.append(node.left)
        #             if node.right:
        #                 q.append(node.right)

        #             size -= 1

        # bfs(root)
        # return count 