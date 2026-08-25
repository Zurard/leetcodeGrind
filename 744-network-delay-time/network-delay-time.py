class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = [[] for _ in range(n+1)]
        for to , where , delay in times:
            graph[to].append((where, delay)) 

        import heapq 
        heap = []
        heapq.heappush(heap , (0, k))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        while heap : 
            time , u = heapq.heappop(heap)

            if time > dist[u]: 
                continue

            for neighbour , delay in graph[u]:
                newTime = time + delay

                if newTime < dist[neighbour]:
                    dist[neighbour] = newTime

                    heapq.heappush(heap , (newTime , neighbour))

        if float("inf") in dist[1:]: 
            return -1 

        return max(dist[1:])