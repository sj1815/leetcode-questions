class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1])) 
        count = 0
        
        for i in range(len(points) - 1):
            yA = points[i][1]
            max_y = float("-inf")
            
            for j in range(i + 1, len(points)):
                yB = points[j][1]
                if yB <= yA and yB > max_y:
                    count += 1
                    max_y = yB
        
        return count
        