class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        DIRECTION = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL= m
        LEFT_WALL = -1

        while len(ans) != m * n:
            if DIRECTION == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                RIGHT_WALL -= 1
                DIRECTION = DOWN
            elif DIRECTION == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1
                DIRECTION = LEFT
            elif DIRECTION == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                LEFT_WALL += 1
                DIRECTION = UP
            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                UP_WALL += 1
                DIRECTION = RIGHT

        return ans

            



        