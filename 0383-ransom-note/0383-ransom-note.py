class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransom_note_counts = collections.Counter(ransomNote)
        magazine_counts = collections.Counter(magazine)

        for char, count in ransom_note_counts.items():
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False
        return True