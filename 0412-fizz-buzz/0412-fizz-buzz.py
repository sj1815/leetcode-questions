class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for num in range(1, n + 1):
            div_by_3 = (num % 3 == 0)
            div_by_5 = (num % 5 == 0)

            ans = ""

            if div_by_3:
                ans += "Fizz"
            if div_by_5:
                ans += "Buzz"
            if not ans:
                ans = str(num)
            
            res.append(ans)
        
        return res
        