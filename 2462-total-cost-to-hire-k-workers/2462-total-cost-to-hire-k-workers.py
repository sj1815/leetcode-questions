class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left_can, right_can = [], []
        left, right = 0, n - 1
        total = 0


        while left <= right and len(left_can) < candidates:
            heapq.heappush(left_can, costs[left])
            left += 1
        while left <= right and len(right_can) < candidates:
            heapq.heappush(right_can, costs[right])
            right -= 1

        for _ in range(k):
            if right_can and (not left_can or right_can[0] < left_can[0]):
                total += heapq.heappop(right_can)
                if left <= right:
                    heapq.heappush(right_can, costs[right])
                    right -= 1
            else:
                total += heapq.heappop(left_can)
                if left <= right:
                    heapq.heappush(left_can, costs[left])
                    left += 1

        return total
