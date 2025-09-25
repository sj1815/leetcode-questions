class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        board.reverse()
        def board_pos(pos):
            r = (pos - 1) // n
            c = (pos - 1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]
        
        q = deque()
        q.append([1, 0]) #[pos, moves]
        visit = set()
        while q:
            pos, moves = q.popleft()

            for dice in range(1, 7):
                next_pos = pos + dice
                r, c = board_pos(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos == n * n:
                    return moves + 1
                if next_pos not in visit:
                    visit.add(next_pos)
                    q.append([next_pos, moves + 1])
        
        return -1
        