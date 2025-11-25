class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        length = 1
        remainder = 1 % k
        
        while remainder != 0:
            remainder = (remainder * 10 + 1) % k
            length += 1
        
        return length