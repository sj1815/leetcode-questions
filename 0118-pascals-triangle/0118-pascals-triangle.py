class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        pas_triangle = [[1]]

        for i in range(1, numRows):
            prev_row = pas_triangle[-1]
            next_row = [1]

            for j in range(1, i):
                next_row.append(prev_row[j - 1] + prev_row[j])
            next_row.append(1)
            pas_triangle.append(next_row)
        
        return pas_triangle


        
        