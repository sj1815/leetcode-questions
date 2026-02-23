class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ans = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while len(stack) > 0 and stack[-1] < abs(a):
                    stack.pop()
                if len(stack) == 0:
                    ans.append(a)
                else:
                    if stack[-1] == abs(a):
                        stack.pop()

        ans += stack
        return ans