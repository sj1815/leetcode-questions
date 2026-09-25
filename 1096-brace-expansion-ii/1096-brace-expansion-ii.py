class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def add(a, b):
            return a | b

        def multiply(a, b):
            return {x + y for x in a for y in b}

        def parse(i):
            result = set()
            current = {""}

            while i < n and expression[i] != '}':
                ch = expression[i]

                if ch == ',':
                    result |= current
                    current = {""}
                    i += 1

                elif ch == '{':
                    group, i = parse(i + 1)
                    current = multiply(current, group)

                else:
                    current = {x + ch for x in current}
                    i += 1

            result |= current

            return result, i + 1 if i < n and expression[i] == '}' else i

        result, _ = parse(0)
        return sorted(result)