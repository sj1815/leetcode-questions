class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        count = 0

        for i in range(len(points)):
            yi = points[i][1]
            max_y = - 10 ** 9 - 1
            for j in range(i + 1, len(points)):
                yj = points[j][1]
                if yi >= yj > max_y:
                    count += 1
                    max_y = yj
        
        return count


        