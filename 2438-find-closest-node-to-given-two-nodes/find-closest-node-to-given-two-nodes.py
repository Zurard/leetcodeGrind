class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1] * n 
        dist2 = [-1] * n

        dist1[node1] = 0  
        dist2[node2] = 0 
        
        def dfs(u , currDistance ,arrDistance ):
            v = edges[u]
            if v == -1 or arrDistance[v] != -1 :
                return
            currDistance += 1
            arrDistance[v]= currDistance
            dfs(v, currDistance , arrDistance)

        
        dfs(node1, 0 , dist1)
        dfs(node2, 0 , dist2)
        
        ans = - 1 
        best= float("inf") 

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1 :
                curr = max(dist1[i] , dist2[i])

                if curr < best :
                    best = curr
                    ans = i 

        return ans  
           
