class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        n = len(digits)
        ans, res = [], []
        letter_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i = 0):
            if i == n:
                ans.append(''.join(res))
                return
            
            for letter in letter_map[digits[i]]:
                res.append(letter)
                backtrack(i + 1)
                res.pop()

        backtrack(0)
        return ans



        


        