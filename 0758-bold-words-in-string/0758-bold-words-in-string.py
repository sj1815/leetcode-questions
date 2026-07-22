class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        bold = [False] * n
        
        # Step 1: Mark bold positions
        for i in range(n):
            for w in words:
                if s.startswith(w, i):
                    for j in range(i, i + len(w)):
                        bold[j] = True
        
        # Step 2: Build result
        res = []
        i = 0
        
        while i < n:
            if not bold[i]:
                res.append(s[i])
                i += 1
            else:
                res.append("<b>")
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")
        
        return "".join(res)