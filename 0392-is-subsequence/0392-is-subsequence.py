class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn = len(s)
        tn = len(t)

        if s == "": return True
        if sn > tn: return False

        j = 0
        for i in range(tn):
            if t[i] == s[j]:
                if j == sn - 1:
                    return True
                j += 1
                
        return False
