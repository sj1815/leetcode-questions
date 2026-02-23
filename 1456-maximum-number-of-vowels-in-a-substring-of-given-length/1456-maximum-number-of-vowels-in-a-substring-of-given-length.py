class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_count = count = 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i >= k:
                if s[i - k] in vowels:
                    count -= 1
            max_count = max(max_count, count)

        return max_count

            