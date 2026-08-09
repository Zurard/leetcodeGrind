class Solution(object):
    def totalCost(self, costs, k, candidates):
        import heapq

        n = len(costs)

        left = []
        right = []

        # If candidate groups overlap
        if 2 * candidates >= n:
            heap = []

            for i in range(n):
                heapq.heappush(heap, (costs[i], i))

            total_cost = 0

            for _ in range(k):
                cost, index = heapq.heappop(heap)
                total_cost += cost

            return total_cost

        # Initial left candidates
        for i in range(candidates):
            heapq.heappush(left, (costs[i], i))

        # Initial right candidates
        for i in range(n - candidates, n):
            heapq.heappush(right, (costs[i], i))

        left_ptr = candidates
        right_ptr = n - candidates - 1

        total_cost = 0

        while k > 0:

            # Left heap is empty
            if not left:
                cost, index = heapq.heappop(right)

                if left_ptr <= right_ptr:
                    heapq.heappush(
                        right,
                        (costs[right_ptr], right_ptr)
                    )
                    right_ptr -= 1

            # Right heap is empty
            elif not right:
                cost, index = heapq.heappop(left)

                if left_ptr <= right_ptr:
                    heapq.heappush(
                        left,
                        (costs[left_ptr], left_ptr)
                    )
                    left_ptr += 1

            # Both heaps have workers
            elif left[0] <= right[0]:
                cost, index = heapq.heappop(left)

                if left_ptr <= right_ptr:
                    heapq.heappush(
                        left,
                        (costs[left_ptr], left_ptr)
                    )
                    left_ptr += 1

            else:
                cost, index = heapq.heappop(right)

                if left_ptr <= right_ptr:
                    heapq.heappush(
                        right,
                        (costs[right_ptr], right_ptr)
                    )
                    right_ptr -= 1

            total_cost += cost
            k -= 1

        return total_cost