class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multiplier = 0
        sub_str = ''

        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)
            elif char == '[':
                stack.append((sub_str, multiplier))
                sub_str = ''
                multiplier = 0
            elif char == ']':
                last_str, num = stack.pop()
                sub_str = last_str + sub_str * num
            else:
                sub_str += char
        
        return sub_str
        