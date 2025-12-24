class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        direction = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = n
        LEFT_WALL = -1

        i, j = 0, 0
        num = 1

        while num <= n * n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    matrix[i][j] = num
                    num += 1
                    j += 1
                i, j = i + 1, j - 1
                RIGHT_WALL -= 1
                direction = DOWN

            elif direction == DOWN:
                while i < DOWN_WALL:
                    matrix[i][j] = num
                    num += 1
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > LEFT_WALL:
                    matrix[i][j] = num
                    num += 1
                    j -= 1
                i, j = i - 1, j + 1
                LEFT_WALL += 1
                direction = UP

            else:  # UP
                while i > UP_WALL:
                    matrix[i][j] = num
                    num += 1
                    i -= 1
                i, j = i + 1, j + 1
                UP_WALL += 1
                direction = RIGHT

        return matrix