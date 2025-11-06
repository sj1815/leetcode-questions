class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        
        word_map = {w[::-1]: i for i, w in enumerate(words)}
        res = []
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):  
                prefix = word[:j]
                suffix = word[j:]
                
                if is_palindrome(prefix) and suffix in word_map and word_map[suffix] != i:
                    res.append([word_map[suffix], i])
                
                if j < len(word) and is_palindrome(suffix) and prefix in word_map and word_map[prefix] != i:
                    res.append([i, word_map[prefix]])
        
        return res