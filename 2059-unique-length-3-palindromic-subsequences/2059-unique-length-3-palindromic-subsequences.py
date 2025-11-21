class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        
        pref = [[0] * 26 for _ in range(n + 1)]
        
        for i in range(n):
            pref[i + 1] = pref[i].copy()
            pref[i + 1][ord(s[i]) - ord('a')] += 1

        first = [-1] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0

        for c in range(26):
            L, R = first[c], last[c]
            if L == -1 or L == R:
                continue  

            for m in range(26):
                if pref[R][m] - pref[L + 1][m] > 0:
                    ans += 1

        return ans