class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse = True)
        
        heap = []
        total = 0
        ans = 0

        for n2, n1 in pairs:
            heappush(heap, n1)
            total += n1

            if len(heap) > k:
                total -= heappop(heap)

            if len(heap) == k:
                ans = max(ans, total * n2)  

        return ans      