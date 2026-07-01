from collections import defaultdict
from typing import List

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr_map = defaultdict(set)
        
        for word in dictionary:
            abbr = self._get_abbr(word)
            self.abbr_map[abbr].add(word)

    def _get_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbr = self._get_abbr(word)
        
        if abbr not in self.abbr_map:
            return True
        
        words = self.abbr_map[abbr]
        
        # unique if only this word exists in set
        return words == {word}

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)