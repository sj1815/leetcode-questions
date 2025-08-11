class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if c_bit == 1:
                if a_bit == 0 and b_bit == 0:
                    flips += 1
            else:  # c_bit == 0
                flips += a_bit + b_bit  # each 1 needs a flip

            a >>= 1
            b >>= 1
            c >>= 1

        return flips