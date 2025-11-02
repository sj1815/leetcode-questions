class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop from stack or use dummy value
                if mapping[char] != top_element:  # Check if it matches the expected opening bracket
                    return False
            else:
                stack.append(char)  # Push opening bracket to stack

        return not stack  # Stack should be empty if valid