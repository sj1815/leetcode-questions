class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        regular_cost = 0
        express_cost = expressCost

        ans = []

        for i in range(len(regular)):
            # Cost if we take regular route from either route
            new_regular = min(
                regular_cost + regular[i],
                express_cost + regular[i]
            )

            # Cost if we take express route from either route
            new_express = min(
                express_cost + express[i],
                regular_cost + expressCost + express[i]
            )

            regular_cost = new_regular
            express_cost = new_express

            ans.append(min(regular_cost, express_cost))

        return ans