class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        
        while len(blocks) > 1:
            x = heapq.heappop(blocks)
            y = heapq.heappop(blocks)
            
            merged = max(x, y) + split
            heapq.heappush(blocks, merged)
        
        return blocks[0]