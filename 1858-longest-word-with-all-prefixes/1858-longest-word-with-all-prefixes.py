class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        self.result = ""

        def dfs(node, path):
            for ch in sorted(node.children.keys()):
                child = node.children[ch]
                
                if child.is_end:
                    path.append(ch)
                    
                    word = "".join(path)
                
                    if (len(word) > len(self.result) or
                       (len(word) == len(self.result) and word < self.result)):
                        self.result = word
                    
                    dfs(child, path)
                    
                    path.pop()
        
        dfs(root, [])
        return self.result

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False



