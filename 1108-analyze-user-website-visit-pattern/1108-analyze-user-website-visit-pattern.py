class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            user_visits[u].append(w)
        
        pattern_users = defaultdict(set)
        for user, sites in user_visits.items():
            n = len(sites)
            seen = set()
            for i in range(n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        pattern = (sites[i], sites[j], sites[k])
                        if pattern not in seen:
                            seen.add(pattern)
                            pattern_users[pattern].add(user)
        
        return min(pattern_users.keys(), key=lambda p: (-len(pattern_users[p]), p))
        