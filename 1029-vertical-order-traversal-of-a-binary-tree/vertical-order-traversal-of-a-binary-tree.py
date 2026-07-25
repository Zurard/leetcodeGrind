from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cords = [] # to store conrdinates 

        # we will use dfs to assign cordinates to each nodes 
        def assignCords(node , row , col ):   
            if node is None: 
                return 
            cords.append((col , row , node.val))
            
            assignCords(node.left , row + 1 , col - 1 )
            assignCords(node.right , row + 1 , col + 1 )

        #assign cords 
        assignCords(root , 0 , 0 )
        print(cords)

        # sort the cords based on cols 
        cords.sort()
        print(cords)

        # group all the nodes based on the same cols 
        
        i = 0

        while i < len(cords):
            curr_col = cords[i][0]
            temp = []

            while i < len(cords) and cords[i][0] == curr_col:
                temp.append(cords[i][2])
                i += 1

            res.append(temp)    

        return res

        

