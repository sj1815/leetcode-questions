class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        def min_cost(i):
            if i <= 1:
                return 0

            if i in cache:
                return cache[i]

            one_down = cost[i - 1] + min_cost(i - 1)
            two_down = cost[i - 2] + min_cost(i - 2)
            cache[i] = min(one_down, two_down)
            return cache[i]

        cache = {}
        return min_cost(len(cost))
        