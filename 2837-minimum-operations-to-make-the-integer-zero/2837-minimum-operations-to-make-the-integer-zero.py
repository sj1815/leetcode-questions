class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 61):  
            target = num1 - i * num2
            if target < 0:
                continue
            if target >= i and target.bit_count() <= i:
                return i
        return -1
        