class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])  # (combination, moves)
        visited = {"0000"}

        while q:
            comb, moves = q.popleft()
            if comb == target:
                return moves

            for i in range(4):
                digit = int(comb[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    new_comb = comb[:i] + str(new_digit) + comb[i+1:]

                    if new_comb not in visited and new_comb not in dead:
                        visited.add(new_comb)
                        q.append((new_comb, moves + 1))

        return -1