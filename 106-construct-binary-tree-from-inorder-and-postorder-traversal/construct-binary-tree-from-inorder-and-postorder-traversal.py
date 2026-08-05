class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(inorder,postorder):
            if not inorder:
                return None 

            root_val = postorder[-1]
            root = TreeNode(root_val)
            root_index  = inorder.index(root_val)

            left_inorder = inorder[:root_index]
            left_postorder = postorder[:root_index]

            right_inorder = inorder[root_index+1 : ]
            right_postorder = postorder[root_index: -1 ]

            root.left = build(left_inorder, left_postorder)
            root.right = build(right_inorder, right_postorder)

            return root 


        return build(inorder,postorder)