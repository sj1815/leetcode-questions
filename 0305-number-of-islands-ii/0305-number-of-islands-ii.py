class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [-1] * (m * n)
        rank = [0] * (m * n)
        count = 0
        res = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                if rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                count -= 1  # merge two islands

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i, j in positions:
            idx = i * n + j
            if parent[idx] != -1:
                res.append(count)  # already land
                continue

            parent[idx] = idx
            count += 1

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    nei_idx = x * n + y
                    if parent[nei_idx] != -1:
                        union(idx, nei_idx)

            res.append(count)

        return res

        