class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n:
            tmp = n // 5
            cnt += tmp
            n = tmp
        return cnt
        