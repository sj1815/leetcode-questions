class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_check = (i == 0) or (flowerbed[i - 1] == 0)
                right_check = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left_check and right_check:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        
        return n <= 0
        