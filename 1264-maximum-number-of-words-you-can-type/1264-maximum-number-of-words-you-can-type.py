class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_keys = set(brokenLetters)
        ans = 0
        
        for word in text.split():
            if not (set(word) & broken_keys):
                ans += 1
        
        return ans