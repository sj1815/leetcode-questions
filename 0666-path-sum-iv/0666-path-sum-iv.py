from typing import List

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}

        for num in nums:
            depth = num // 100
            pos = (num // 10) % 10
            val = num % 10
            tree[(depth, pos)] = val

        def dfs(depth: int, pos: int, path_sum: int) -> int:
            if (depth, pos) not in tree:
                return 0

            path_sum += tree[(depth, pos)]

            left = (depth + 1, 2 * pos - 1)
            right = (depth + 1, 2 * pos)

            has_left = left in tree
            has_right = right in tree

            if not has_left and not has_right:
                return path_sum

            total = 0

            if has_left:
                total += dfs(depth + 1, 2 * pos - 1, path_sum)

            if has_right:
                total += dfs(depth + 1, 2 * pos, path_sum)

            return total

        return dfs(1, 1, 0)