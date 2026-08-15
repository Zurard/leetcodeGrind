class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = [False] * n
    
        def dfs(city):
            nonlocal n 
            visited[city] = True 

            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)


        count = 0 
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)

        return count 