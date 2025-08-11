class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell

            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if potions[m] >= min_potion:
                    r = m - 1
                else:
                    l = m + 1

            res.append(n - l)
        
        return res

