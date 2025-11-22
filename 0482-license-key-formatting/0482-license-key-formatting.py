class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        res = []
        while len(s) > k:
            res.append(s[-k:])
            s = s[:-k]
        
        res.append(s)
        
        res.reverse()
        return "-".join(res)