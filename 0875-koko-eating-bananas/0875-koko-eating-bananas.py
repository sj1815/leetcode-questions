class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            hrs = 0

            for pile in piles:
                hrs += (pile + mid - 1) // mid
                
            if hrs <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
    
        return ans

        