class Solution:
    def maxFreqSum(self, s: str) -> int:
        consonent = 0
        vowel = 0
        char_set = set(s)
        for i in char_set:
            if i in "aeiou":
                vowel = max(vowel, s.count(i))
            else:
                consonent = max(consonent, s.count(i))
        return vowel+consonent
        