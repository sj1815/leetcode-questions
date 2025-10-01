class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        used_bottles = 0

        while numBottles >= numExchange:
            used_bottles += numExchange
            numBottles -= numExchange

            numBottles += 1
        
        return used_bottles + numBottles

        
        