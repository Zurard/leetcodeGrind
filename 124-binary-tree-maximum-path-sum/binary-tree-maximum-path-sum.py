# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def findSum(node): 
            nonlocal ans 
            if not node :
                return 0 
            
            left= 0
            right = 0

            if node.left : 
                left = findSum(node.left)
            if node.right:
                right = findSum(node.right)

            left = max(0,left)
            right = max(0,right)
            
            ans = max(ans , node.val + left + right)

            return node.val + max(left , right) 
        
        if not root:
            return 0

        findSum(root)
        return ans