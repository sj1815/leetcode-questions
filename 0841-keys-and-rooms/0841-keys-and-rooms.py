class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()

        def dfs(room: int):
            seen.add(room)
            for key in rooms[room]:
                if key not in seen:
                    dfs(key)

            
        dfs(0)
        return len(seen) == len(rooms)