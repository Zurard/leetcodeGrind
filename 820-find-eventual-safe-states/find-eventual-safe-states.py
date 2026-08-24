class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n

        # need to calc all the 0utdegrees 
        for u in range(n):
            outdegree[u] = len(graph[u])

        from collections import deque 
        q = deque()

        for u in range(n):
            if outdegree[u] == 0 :
                q.append(u)
    

        # now we need to build reverse graph ? 
        reverse = [[] for _ in range(n)]

        for u in range(n):
            for v in graph[u]:
                reverse[v].append(u)
        
        while q : 
            u = q.popleft()
            

            for v in reverse[u]:
                outdegree[v] -= 1 

                if outdegree[v] == 0:
                    q.append(v)

        

        res = []

        for u in range(n):
            if outdegree[u] == 0 :
                res.append(u)

        
        return res 