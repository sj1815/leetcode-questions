class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for w in range(n - m + 1):
            for i in range(n):
                if needle[i] != haystack[w + i]:
                    break
                if i == m - 1:
                    return w
        return -1
        