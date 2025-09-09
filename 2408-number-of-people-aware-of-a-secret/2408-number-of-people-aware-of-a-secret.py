class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        aware = [0] * n
        sharer = 0
        total = 1
        aware[0] = 1

        for day in range(1, n):
            if day >= delay:
                sharer += aware[day - delay]
            if day >= forget:
                forgot = aware[day - forget]
                total -= forgot
                sharer -= forgot
            
            aware[day] = sharer
            total += sharer

        return total % (10 ** 9 + 7)


