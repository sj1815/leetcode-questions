from typing import List
from collections import defaultdict
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)

        for student_id, score in items:
            heapq.heappush(scores[student_id], score)

            # Keep only the top 5 scores
            if len(scores[student_id]) > 5:
                heapq.heappop(scores[student_id])

        ans = []

        for student_id in sorted(scores):
            avg = sum(scores[student_id]) // 5
            ans.append([student_id, avg])

        return ans