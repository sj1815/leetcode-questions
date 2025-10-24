class WordDictionary:

    def __init__(self):
        self.dict = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dict[len(word)].add(word)
        
    def search(self, word: str) -> bool:
        n = len(word)
        for d in self.dict[n]:
            i = 0
            while i < n and (d[i] == word[i] or word[i] == "."):
                i += 1
            if i == n:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)