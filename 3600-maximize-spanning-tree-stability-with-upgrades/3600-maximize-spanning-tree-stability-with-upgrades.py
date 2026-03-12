from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        self.parent[pb] = pa
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0

            optional = []

            for u,v,s,m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if not dsu.union(u,v):
                        return False     # cycle among must edges
                    used += 1
                else:
                    optional.append((u,v,s))

            no_up = []
            need_up = []

            for u,v,s in optional:
                if s >= x:
                    no_up.append((u,v))
                elif s*2 >= x:
                    need_up.append((u,v))

            for u,v in no_up:
                if dsu.union(u,v):
                    used += 1

            for u,v in need_up:
                if upgrades == k:
                    break
                if dsu.union(u,v):
                    upgrades += 1
                    used += 1

            return used == n-1


        lo, hi = 0, max(s for _,_,s,_ in edges)*2
        ans = -1

        while lo <= hi:
            mid = (lo+hi)//2
            if can(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1

        return ans