class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a, b = -1, -1
        result = 0

        for start, end in intervals:
            if start > a:
                result += 2
                b = end - 1
                a = end
            
            elif start > b:
                result += 1
                b = a
                a = end


        return result