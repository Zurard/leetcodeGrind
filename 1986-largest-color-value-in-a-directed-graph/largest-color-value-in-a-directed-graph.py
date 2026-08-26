class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        visited = set()
        n = len(colors)

        # i need to make graph 
        graph = [[] for _ in range(n)]
        for u , v in edges:
            graph[u].append(v)
        
        indegree = [0] * n 
        for u in range(n):
            for v in graph[u]:
                indegree[v] += 1

        from collections import deque
        q = deque()

        for u in range(n): 
            if indegree[u] == 0 :
                q.append(u) 
        

        dp = [[0]*26 for _ in range(n) ]

        ans = 0 
        processed = 0 

        while q : 
            u = q.popleft()     
            processed += 1

            color = ord(colors[u]) - ord('a')

            dp[u][color] += 1 
            ans = max(ans, max(dp[u]))

            for v in graph[u]:
                for c in range(26):
                    dp[v][c] = max(dp[u][c] , dp[v][c])
                
                indegree[v] -= 1

                if indegree[v] == 0 :
                    q.append(v)

            
        if processed !=  n:
            return -1 

        return ans 