
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, d):
            length = r - l + 1
            old_sum = sum1[node]

            sum2[node] = (
                sum2[node] + 2 * d * old_sum
                + d * d * length
            ) % MOD

            sum1[node] = (
                old_sum + d * length
            ) % MOD

            lazy[node] = (lazy[node] + d) % MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            d = lazy[node]

            apply(node * 2, l, mid, d)
            apply(node * 2 + 1, mid + 1, r, d)

            lazy[node] = 0

        def update(node, l, r, ql, qr, d):
            if ql <= l and r <= qr:
                apply(node, l, r, d)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, d)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, d)

            sum1[node] = (
                sum1[node * 2] + sum1[node * 2 + 1]
            ) % MOD

            sum2[node] = (
                sum2[node * 2] + sum2[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            # Increment distinct counts for valid start positions.
            update(1, 0, n - 1, prev + 1, i, 1)

            # Sum of squared distinct counts for subarrays ending at i.
            ans = (ans + sum2[1]) % MOD

            last[x] = i

        return ans
