class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))
        
        n = len(parsed)
        invalid = [False] * n  # track invalids by index

        for i in range(n):
            name1, time1, amount1, city1 = parsed[i]
            if amount1 > 1000:
                invalid[i] = True
            for j in range(n):
                if i == j:
                    continue
                name2, time2, amount2, city2 = parsed[j]
                if name1 == name2 and city1 != city2 and abs(time1 - time2) <= 60:
                    invalid[i] = True
                    invalid[j] = True
        
        # return all invalid transactions by index
        return [transactions[i] for i in range(n) if invalid[i]]