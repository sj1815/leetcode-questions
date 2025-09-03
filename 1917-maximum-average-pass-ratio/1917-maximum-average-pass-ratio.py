class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            gain = (p + 1)/ (t + 1) - p / t
            heap.append((-gain, p, t))
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t= heapq.heappop(heap)
            p, t = p + 1, t + 1
            gain = (p + 1)/ (t + 1) - p / t
            heapq.heappush(heap, (-gain, p ,t))
        return sum(p / t for _, p, t in heap) / len(classes)
        