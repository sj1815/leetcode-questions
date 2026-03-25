class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        nums = [x for row in grid for x in row]  # flatten grid
        size = len(nums)

        l_mult = 1
        r_mult = 1
        l_arr = [0] * size
        r_arr = [0] * size

        # Prefix products (left to right)
        for i in range(size):
            l_arr[i] = l_mult % MOD
            l_mult = (l_mult * nums[i]) % MOD

        # Suffix products (right to left)
        for i in range(size - 1, -1, -1):
            r_arr[i] = r_mult % MOD
            r_mult = (r_mult * nums[i]) % MOD

        # Combine left and right multipliers
        res = [(l_arr[i] * r_arr[i]) % MOD for i in range(size)]

        # Convert back to 2D
        ans = []
        for i in range(m):
            ans.append(res[i * n:(i + 1) * n])

        return ans