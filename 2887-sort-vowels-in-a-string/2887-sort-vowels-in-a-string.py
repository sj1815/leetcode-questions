class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        chars = list(s)
        vowel_list = [ch for ch in chars if ch in vowels]
        vowel_list.sort() 

        j = 0
        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = vowel_list[j]
                j += 1

        return "".join(chars)