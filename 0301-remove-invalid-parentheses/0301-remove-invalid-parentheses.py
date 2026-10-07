class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s):
            count = 0

            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = {s}
        result = []

        while queue:
            # Check current level first
            for curr in queue:
                if is_valid(curr):
                    result.append(curr)

            # If we found valid strings, this is the minimum
            # number of removals, so stop.
            if result:
                return result

            # Generate next level by removing one parenthesis
            next_level = set()

            for curr in queue:
                for i in range(len(curr)):
                    if curr[i] in '()':
                        next_level.add(curr[:i] + curr[i + 1:])

            queue = next_level

        return result