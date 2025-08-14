class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for char in reversed(s):
            if char != " ":
                l += 1
            elif l > 0:
                break

        return l
            

        