class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        r_set, c_set = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r_set.add(i)
                    c_set.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in r_set or j in c_set:
                    matrix[i][j] = 0