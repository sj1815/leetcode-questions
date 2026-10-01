class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_ele = stk.pop() if stk else '#'

                if mapping[char] != top_ele:
                    return False
            else:
                stk.append(char)

        return not stk

        