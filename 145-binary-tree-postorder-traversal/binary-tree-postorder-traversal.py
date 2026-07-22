# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # this is the recursive soln 
        # res = []

        # def traverse(node, res):
        #     if not node :
        #         return 
        #     traverse(node.left , res)
        #     traverse(node.right , res)
        #     res.append(node.val)
        
        # traverse(root , res )
        # return res

        # ---------------------------- >>this is the iterative soln where we use stack 
        # ----------------->>>this soln uses 2 stack 
        # s1= [root]
#         s2 = []
        # res = []
        # if not root : 
            # return res 
        # 
        # while s1 :
            # node = s1.pop()
            # s2.append(node)
# 
            # if node.left : 
                # s1.append(node.left)
            # if node.right : 
                # s1.append(node.right)
# 
        # while s2 : 
            # node = s2.pop()
            # res.append(node.val)
# 
        # return res 
        
        #this soln uses only one stack 

        res = []
        if not root : 
            return res 
        
        stack = [] 
        curr = root
        lastVisited= None 
        while stack or curr : 
            while curr : 
                stack.append(curr)
                curr = curr.left
            
            node = stack[-1]
            
            if node.right and lastVisited != node.right :
                curr = node.right 
            else : 
                node = stack.pop()
                res.append(node.val)
                lastVisited = node

        return res