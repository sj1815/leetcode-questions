class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)

        for candy in candies:
            res.append(candy + extraCandies >= max_candies) 

        return res