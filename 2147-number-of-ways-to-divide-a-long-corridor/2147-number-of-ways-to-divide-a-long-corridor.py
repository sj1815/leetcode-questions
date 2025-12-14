class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        seats = []

        for i, c in enumerate(corridor):
            if c == "S": seats.append(i)

        n = len(seats)
        if n < 2 or n % 2 == 1:
            return 0

        res = 1
        i = 1
        while i < (n -1):
            res = (res * (seats[i + 1] - seats[i])) % MOD
            i += 2
        
        return res