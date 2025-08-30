class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        x_even = n // 2
        x_odd = (n + 1) // 2
        y_even = m // 2
        y_odd = (m + 1) // 2
        return x_even * y_odd + y_even * x_odd
        