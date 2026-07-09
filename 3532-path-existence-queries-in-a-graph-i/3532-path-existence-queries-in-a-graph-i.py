from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
        
        # Step 1: sort indices by values
        sorted_indices = sorted(range(n), key=lambda i: nums[i])
        
        # Step 2: union adjacent indices if diff <= maxDiff
        for i in range(1, n):
            prev = sorted_indices[i - 1]
            curr = sorted_indices[i]
            
            if nums[curr] - nums[prev] <= maxDiff:
                union(prev, curr)
        
        # Step 3: answer queries
        result = []
        for u, v in queries:
            result.append(find(u) == find(v))
        
        return result