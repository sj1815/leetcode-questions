class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        r_no = 0
        while x > r_no:
            r_no = r_no * 10 + x % 10
            x //= 10

        return x == r_no or x == r_no // 10
        