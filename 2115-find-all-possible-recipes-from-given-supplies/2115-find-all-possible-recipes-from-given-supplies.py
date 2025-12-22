class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredients_graph = defaultdict(list)
        recipe_graph = defaultdict(int)

        for recipe, ing_list in zip(recipes, ingredients):
            recipe_graph[recipe] = len(ing_list)
            for ing in ing_list:
                ingredients_graph[ing].append(recipe)

        q = deque(supplies)
        res = []

        while q:
            item = q.popleft()

            for recipe in ingredients_graph[item]:
                recipe_graph[recipe] -= 1
                if recipe_graph[recipe] == 0:
                    res.append(recipe)
                    q.append(recipe)

        return res
