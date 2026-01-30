from typing import List
import math

class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:
        INF = math.inf
        
        # ---- Step 1: index all unique strings ----
        words = set(original + changed)
        idx = {w: i for i, w in enumerate(words)}
        n = len(idx)
        
        # ---- Step 2: Floyd–Warshall on conversion graph ----
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # ---- Step 3: build Trie on original strings ----
        root = TrieNode()
        for o in original:
            node = root
            for ch in o:
                node = node.children.setdefault(ch, TrieNode())
            node.idx = idx[o]
        
        # ---- Step 4: DP ----
        m = len(source)
        dp = [INF] * (m + 1)
        dp[m] = 0
        
        for i in range(m - 1, -1, -1):
            # no conversion
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            
            # try substring conversions
            node = root
            j = i
            while j < m and source[j] in node.children:
                node = node.children[source[j]]
                j += 1
                if node.idx != -1:
                    src_word = node.idx
                    tgt_sub = target[i:j]
                    if tgt_sub in idx:
                        tgt_word = idx[tgt_sub]
                        if dist[src_word][tgt_word] < INF:
                            dp[i] = min(dp[i], dist[src_word][tgt_word] + dp[j])
        
        return -1 if dp[0] == INF else dp[0]
