class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str,
                       queries: list[str]) -> list[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        # Iterative DFS: Euler tour, depths, parents and prefix masks.
        stack = [(0, -1, 0, 0)]

        while stack:
            u, p, state, mask = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1

                parent[0][u] = u if p == -1 else p
                prefix[u] = mask ^ (1 << (ord(s[u]) - ord('a')))

                stack.append((u, p, 1, 0))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0, prefix[u]))

            else:
                tout[u] = timer - 1

        # Binary lifting table.
        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        # Fenwick tree supporting range XOR updates and point queries.
        bit = [0] * (n + 2)

        def update(i: int, value: int) -> None:
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def point_query(i: int) -> int:
            i += 1
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_xor(left: int, right: int, value: int) -> None:
            update(left, value)
            if right + 1 < n:
                update(right + 1, value)

        def get_prefix(u: int) -> int:
            return prefix[u] ^ point_query(tin[u])

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        chars = list(s)
        ans = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                delta = old_mask ^ new_mask

                # A node's character affects prefix masks
                # for every node in its subtree.
                range_xor(tin[u], tout[u], delta)

                chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                # Combine the two root-to-node paths,
                # counting the LCA exactly once.
                mask = (
                    get_prefix(u)
                    ^ get_prefix(v)
                    ^ (1 << (ord(chars[ancestor]) - ord('a')))
                )

                # Zero or one odd-frequency character.
                ans.append((mask & (mask - 1)) == 0)

        return ans