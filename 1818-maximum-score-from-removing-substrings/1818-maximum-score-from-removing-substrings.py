class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removePairs(s, first, second, val):
            stk = []
            score = 0
            for ch in s:
                if stk and stk[-1] == first and ch == second:
                    stk.pop()
                    score += val
                else:
                    stk.append(ch)

            return ''.join(stk), score

        total = 0
        if x > y:
            s, score1 = removePairs(s, 'a', 'b', x)
            _, score2 = removePairs(s, 'b', 'a', y)
        else:
            s, score1 = removePairs(s, 'b', 'a', y)
            _, score2 = removePairs(s, 'a', 'b', x)

        total = score1 + score2
        return total