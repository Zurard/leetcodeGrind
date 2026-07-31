# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       

        def build (preorder , inorder ):  # shoud return the root node of the subtree
            
            if not preorder :
                return None

            root_val = preorder[0]
            root = TreeNode(root_val)            
            split = inorder.index(root_val)
            
            # now we need to find inorder and preorder for left and right subtree

            left_inorder = inorder[:split] 
            right_inorder = inorder[split+1 :]

            left_preorder = preorder[1 : 1+len(left_inorder)]
            right_preorder = preorder[1+len(left_inorder) : ]

            root.left = build(left_preorder, left_inorder)
            root.right = build(right_preorder , right_inorder)

            return root 


        return  build(preorder, inorder)
