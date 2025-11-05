class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []

        for candy in candies:
            res.append(candy + extraCandies >= max_candies)
        
        return res
        