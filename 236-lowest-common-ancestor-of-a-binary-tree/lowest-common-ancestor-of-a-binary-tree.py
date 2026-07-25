# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dict td store all teh parents 
        parent = {}

        def bfs(root):
            from collections import deque
            Q = deque()
            Q.append(root)
            
            parent[root] = None
            
            while Q:
                Q_len = len(Q)
                while Q_len > 0 : 
                    node = Q.popleft()
                    if node.left : 
                        parent[node.left] = node
                        Q.append(node.left)
                    if node.right:
                        parent[node.right] = node
                        Q.append(node.right)
                    Q_len -= 1
        
        # build the dicr to get parent child  relationship 
        bfs(root)
        # print(parent)

        def findLCA(x, y):
            visited = set()

            # Store all ancestors of x
            while x:
                visited.add(x)
                x = parent[x]

            # Move up from y until a common ancestor is found
            while y not in visited:
                y = parent[y]

            return y

        return findLCA(p,q)

