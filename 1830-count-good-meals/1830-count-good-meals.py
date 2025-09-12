class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        freq = {}

        max_val = max(deliciousness)
        max_sum = max_val * 2
        powers = []
        p = 1
        while p <= max_sum:
            powers.append(p)
            p <<= 1

        for x in deliciousness:
            for target in powers:
                need = target - x
                if need in freq:
                    ans = (ans + freq[need]) % MOD
            freq[x] = freq.get(x, 0) + 1

        return ans
        