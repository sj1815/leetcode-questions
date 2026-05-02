class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_same = {0, 1, 8}
        valid_diff = {2, 5, 6, 9}
        
        def is_good(num):
            has_diff = False
            
            while num > 0:
                digit = num % 10
                
                if digit in valid_diff:
                    has_diff = True
                elif digit not in valid_same:
                    return False
                
                num //= 10
            
            return has_diff
        
        count = 0
        for i in range(1, n + 1):
            if is_good(i):
                count += 1
        
        return count