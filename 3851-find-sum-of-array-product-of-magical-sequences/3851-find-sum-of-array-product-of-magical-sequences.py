MOD = 10**9 + 7
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        # Precompute factorials and inv factorials for combinations up to m
        fact = [1] * (m+1)
        for i in range(1, m+1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (m+1)
        invfact[m] = pow(fact[m], MOD-2, MOD)
        for i in range(m-1, -1, -1):
            invfact[i] = invfact[i+1] * (i+1) % MOD
        def comb(a,b):
            if b < 0 or b > a: return 0
            return fact[a] * invfact[b] % MOD * invfact[a-b] % MOD

        # Precompute pow(nums[i], c) for c = 0..m
        pownums = [[1]*(m+1) for _ in range(n)]
        for i in range(n):
            for c in range(1, m+1):
                pownums[i][c] = (pownums[i][c-1] * nums[i]) % MOD

        # DP: dp[used][carry][ones] = total contribution (sum of products * ways)
        # We'll keep 3D arrays but rolled over indices (process nums[i] sequentially)
        # carry can be at most m (if all m placed in low bits)
        max_carry = m
        # initialize dp: used=0, carry=0, ones=0 -> contribution = 1 (empty product, 1 way)
        dp = [ [ [0]*(k+1) for _ in range(max_carry+1) ] for __ in range(m+1) ]
        dp[0][0][0] = 1

        for i in range(n):
            new_dp = [ [ [0]*(k+1) for _ in range(max_carry+1) ] for __ in range(m+1) ]
            for used in range(0, m+1):
                rem = m - used
                for carry in range(0, max_carry+1):
                    for ones in range(0, k+1):
                        base = dp[used][carry][ones]
                        if base == 0:
                            continue
                        # try placing c occurrences of index i (0..rem)
                        # ways to choose which positions: C(rem, c)
                        # product multiplier: nums[i]^c (precomputed)
                        for c in range(0, rem+1):
                            new_used = used + c
                            total = carry + c
                            bit = total & 1
                            new_ones = ones + bit
                            if new_ones > k:
                                # pruning
                                continue
                            new_carry = total >> 1
                            if new_carry > max_carry:
                                # shouldn't happen if max_carry=m, but safe check
                                continue
                            ways = comb(rem, c)
                            mul = pownums[i][c]
                            add = base * ways % MOD * mul % MOD
                            new_dp[new_used][new_carry][new_ones] = (new_dp[new_used][new_carry][new_ones] + add) % MOD
            dp = new_dp

        # Sum final dp states with used == m and ones + popcount(carry) == k
        ans = 0
        for carry in range(0, max_carry+1):
            carry_bits = carry.bit_count()  # python 3.8+: popcount
            for ones in range(0, k+1):
                if ones + carry_bits == k:
                    ans = (ans + dp[m][carry][ones]) % MOD

        return ans