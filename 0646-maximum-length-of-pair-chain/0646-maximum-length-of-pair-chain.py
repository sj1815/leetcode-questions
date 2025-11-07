class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        curr_end = float('-inf')
        chain = 0

        for a, b in pairs:
            if a > curr_end:
                chain += 1
                curr_end = b
        return chain