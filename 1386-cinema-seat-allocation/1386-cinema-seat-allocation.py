class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)

        for r, c in reservedSeats:
            seats[r].add(c)
        
        res = 0

        for row in seats:
            left = all(seat not in seats[row] for seat in [2,3,4,5])
            right = all(seat not in seats[row] for seat in [6,7,8,9])
            middle = all(seat not in seats[row] for seat in [4,5,6,7])

            if left and right:
                res += 2
            elif left or right or middle:
                res += 1

        res += 2 * (n - len(seats))

        return res