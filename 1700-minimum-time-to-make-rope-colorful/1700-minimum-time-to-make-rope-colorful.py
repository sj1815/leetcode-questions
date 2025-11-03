class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                ans += min(time, neededTime[i])
                time = max(time, neededTime[i])
            else:
                time = neededTime[i]
        
        return ans

        