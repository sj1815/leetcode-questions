class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        row_index = 0

        for i, row in enumerate(mat):
            ones = sum(row)
            if ones > max_ones:
                max_ones = ones
                row_index = i

        return [row_index, max_ones]