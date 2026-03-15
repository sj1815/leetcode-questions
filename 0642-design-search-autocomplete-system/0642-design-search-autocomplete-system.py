from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.counts = defaultdict(int)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.cur_node = self.root
        self.prefix = ""

        for s, t in zip(sentences, times):
            self._add_sentence(s, t)

    def _add_sentence(self, sentence, count):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.counts[sentence] += count

    def input(self, c: str) -> List[str]:

        if c == "#":
            self._add_sentence(self.prefix, 1)
            self.prefix = ""
            self.cur_node = self.root
            return []

        self.prefix += c

        if self.cur_node and c in self.cur_node.children:
            self.cur_node = self.cur_node.children[c]

            items = list(self.cur_node.counts.items())

            items.sort(key=lambda x: (-x[1], x[0]))

            return [s for s, _ in items[:3]]

        else:
            self.cur_node = None
            return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)