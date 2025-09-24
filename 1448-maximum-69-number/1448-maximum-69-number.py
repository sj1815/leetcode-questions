class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        
        for i, ch in enumerate(digits):
            if ch == '6':       
                digits[i] = '9'
                break            
        
        return int("".join(digits))
        