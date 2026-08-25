class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BEllman Ford Style ans 
        inf = float("inf")

        cost = [inf] * n
        cost[src] = 0

        # k stops = k + 1 flights
        for _ in range(k + 1):

            temp = cost.copy()

            for u, v, price in flights:

                if cost[u] == inf:
                    continue

                temp[v] = min(
                    temp[v],
                    cost[u] + price
                )

            cost = temp

        if cost[dst] == inf:
            return -1

        return cost[dst]

        # this soln will give me TLE (Djikstra algo modified)
        # import heapq 
        # heap =[]

        # # need to make graph 
        # graph = [[] for _ in range(n)]
        # for u , v , cost in flights : 
        #     graph[u].append((v,cost))

        # heapq.heappush(heap,(0 , src ,0))
        # # print(heap)
        # while heap : 
        #     price , city , stops = heapq.heappop(heap)
        #     # print("this is old --->",price , city)

        #     if city == dst :
        #         return price 

        #     if stops > k :
        #         continue

        #     for neighbour , cost in graph[city]:
        #         newPrice = price + cost
        #         newStops = stops + 1
        #         # print("here--->",newPrice , neighbour)
        #         if newStops <= k+ 1:
        #             heapq.heappush(heap,(newPrice , neighbour, newStops))
        #         # print(heap)
        return -1

