class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(i)

        visited_buses = set()
        visited_stops = set([source])
        queue = deque()
        
        # initialize BFS with buses from source
        for bus in stop_to_buses[source]:
            queue.append((bus, 1))
            visited_buses.add(bus)

        while queue:
            bus, buses_taken = queue.popleft()
            
            for stop in routes[bus]:
                if stop == target:
                    return buses_taken
                
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_bus in stop_to_buses[stop]:
                        if next_bus not in visited_buses:
                            visited_buses.add(next_bus)
                            queue.append((next_bus, buses_taken + 1))

        return -1