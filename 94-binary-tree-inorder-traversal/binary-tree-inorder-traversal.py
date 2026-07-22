# Definition for a binary tre node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # RECURSIVE SOLN --------------->>>
        # res = []

        # def traverse(node, res ): 
        #     if not node : 
        #         return 
        #     traverse(node.left , res)
        #     res.append(node.val)
        #     traverse(node.right, res)  

        # traverse(root , res )

        # return res 

        # ITERATIVE SOLN ----------------->>
        # for this method we need to use stack to act as recursion call 
        res = []
        stack = []
        curr = root 

        if not root :
            return res 

        while curr or stack: 
            while curr : 
                stack.append(curr)
                curr = curr.left 
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res 