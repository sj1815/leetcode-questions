class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 1

        while n > 0:
            for day in range(7):
                if n == 0:
                    break
                total += monday + day
                n -= 1
            monday += 1
        
        return total
