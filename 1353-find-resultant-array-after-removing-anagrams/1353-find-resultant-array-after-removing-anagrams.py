class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]

        for i in range(1,len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                result.append(words[i])
        return result

        