class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        substring_len = word_len * total_words
        word_count = Counter(words)
        
        res = []
        
        # We need to check for each offset in [0, word_len)
        for i in range(word_len):
            left = i
            seen = Counter()
            count = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    seen[word] += 1
                    count += 1
                    
                    # Shrink window if word seen too many times
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If all words matched
                    if count == total_words:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len
        
        return res