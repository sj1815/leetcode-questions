class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        # build graph with min-heap for lexicographic order
        for src, dest in tickets:
            heapq.heappush(adj_list[src], dest)

        res = []
        def dfs(src):
            while adj_list[src]:
                next_dest = heapq.heappop(adj_list[src])
                dfs(next_dest)
            res.append(src)

        dfs("JFK")
        return res[::-1]