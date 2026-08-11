class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        dummy = TreeNode(val)

        parent = None

        def findInsert(node):
            nonlocal parent

            if val < node.val:
                if node.left is None:
                    parent = node
                    return

                findInsert(node.left)

            else:
                if node.right is None:
                    parent = node
                    return

                findInsert(node.right)

        findInsert(root)

        if val < parent.val:
            parent.left = dummy
        else:
            parent.right = dummy

        return root