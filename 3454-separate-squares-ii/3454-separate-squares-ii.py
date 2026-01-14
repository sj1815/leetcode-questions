class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, s in squares:
            events.append((y, x, x + s, 1))
            events.append((y + s, x, x + s, -1))

        events.sort()
        ys = sorted(set(e[0] for e in events))

        def union_length(intervals):
            intervals.sort()
            length = 0
            prev_start, prev_end = -1e9, -1e9
            for s, e in intervals:
                if s > prev_end:
                    length += e - s
                    prev_start, prev_end = s, e
                else:
                    if e > prev_end:
                        length += e - prev_end
                        prev_end = e
            return length

        # Precompute areas between y-levels
        active = []
        idx = 0
        areas = []
        total_area = 0

        for i in range(len(ys) - 1):
            y = ys[i]
            ny = ys[i + 1]

            while idx < len(events) and events[idx][0] == y:
                _, x1, x2, t = events[idx]
                if t == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                idx += 1

            width = union_length(active[:])
            area = width * (ny - y)
            areas.append((y, ny, area))
            total_area += area

        half = total_area / 2
        curr = 0

        for y, ny, area in areas:
            if curr + area >= half:
                return y + (half - curr) / (area / (ny - y))
            curr += area
