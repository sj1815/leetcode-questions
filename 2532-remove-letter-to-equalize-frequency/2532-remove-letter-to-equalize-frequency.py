class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)

        for ch in list(freq.keys()):
            # remove one occurrence of ch
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]

            # check if all frequencies are equal
            if len(set(freq.values())) == 1:
                return True

            # backtrack
            freq[ch] = freq.get(ch, 0) + 1

        return False
        