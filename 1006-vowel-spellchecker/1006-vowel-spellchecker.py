class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(word: str) -> str:
            return "".join("*" if ch in vowels else ch for ch in word)

        # Exact-match set
        exact = set(wordlist)

        # Case-insensitive map
        lower_map = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in lower_map:
                lower_map[lw] = w

        # Vowel-error map
        devowel_map = {}
        for w in wordlist:
            key = devowel(w.lower())
            if key not in devowel_map:
                devowel_map[key] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
            elif q.lower() in lower_map:
                ans.append(lower_map[q.lower()])
            elif devowel(q.lower()) in devowel_map:
                ans.append(devowel_map[devowel(q.lower())])
            else:
                ans.append("")
        return ans