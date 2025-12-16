import heapq
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adj_list[src], dst)

        res = []

        def dfs(src):
            while adj_list[src]:
                next_dst = heapq.heappop(adj_list[src])
                dfs(next_dst)
            res.append(src)
            
        dfs("JFK")
        return res[::-1]
        