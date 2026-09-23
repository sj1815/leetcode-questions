class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        parts = list(map(int, ip.split(".")))
        start = (
            (parts[0] << 24)
            | (parts[1] << 16)
            | (parts[2] << 8)
            | parts[3]
        )

        ans = []

        while n > 0:
            # Largest aligned block
            if start == 0:
                block = 1 << 32
            else:
                block = start & -start

            # Block cannot contain more than n addresses
            while block > n:
                block >>= 1

            prefix = 32 - (block.bit_length() - 1)

            a = (start >> 24) & 255
            b = (start >> 16) & 255
            c = (start >> 8) & 255
            d = start & 255

            ans.append(f"{a}.{b}.{c}.{d}/{prefix}")

            start += block
            n -= block

        return ans