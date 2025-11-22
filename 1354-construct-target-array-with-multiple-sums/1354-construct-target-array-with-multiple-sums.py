class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)

        while True:
            largest = -heapq.heappop(target)
            rest = total - largest

            if largest == 1 or rest == 1:
                return True

            if rest == 0 or largest < rest:
                return False

            new_val = largest % rest
            if new_val == 0:
                return False

            total = rest + new_val
            heapq.heappush(target, -new_val) 