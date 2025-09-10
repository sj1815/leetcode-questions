class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        candidates = set()
        lang_sets = [set(langs) for langs in languages]

        for u, v in friendships:
            u -= 1
            v -= 1
            if not (lang_sets[u] & lang_sets[v]):  
                candidates.add(u)
                candidates.add(v)

        if not candidates:
            return 0

        min_teachers = float("inf")
        for language in range(1, n + 1):
            count = 0
            for person in candidates:
                if language not in lang_sets[person]:
                    count += 1
            min_teachers = min(min_teachers, count)

        return min_teachers

         